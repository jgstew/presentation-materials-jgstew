"""
Example Template for BigFix Server Plugin Service.

requires `besapi`, install with command `pip install besapi`

Example Usage:
python plugin_example_template.py -r https://localhost:52311/api -u API_USER -p API_PASSWORD

References:
- https://developer.bigfix.com/rest-api/api/admin.html
- https://github.com/jgstew/besapi/blob/master/examples/rest_cmd_args.py
- https://github.com/jgstew/tools/blob/master/Python/locate_self.py
"""

import json
import logging
import ntpath
import os
import platform
import sys

import besapi
import besapi.plugin_utilities

__version__ = "1.1.2"
verbose = 0
bes_conn = None
invoke_folder = None


def get_invoke_folder(verbose=0):
    """Get the folder the script was invoked from."""
    # using logging here won't actually log it to the file:

    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        if verbose:
            print("running in a PyInstaller bundle")
        invoke_folder = os.path.abspath(os.path.dirname(sys.executable))
    else:
        if verbose:
            print("running in a normal Python process")
        invoke_folder = os.path.abspath(os.path.dirname(__file__))

    if verbose:
        print(f"invoke_folder = {invoke_folder}")

    return invoke_folder


def get_invoke_file_name(verbose=0):
    """Get the filename the script was invoked from."""
    # using logging here won't actually log it to the file:

    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        if verbose:
            print("running in a PyInstaller bundle")
        invoke_file_path = sys.executable
    else:
        if verbose:
            print("running in a normal Python process")
        invoke_file_path = __file__

    if verbose:
        print(f"invoke_file_path = {invoke_file_path}")

    # get just the file name, return without file extension:
    return os.path.splitext(ntpath.basename(invoke_file_path))[0]


def string_truncate(text, max_length=70):
    """Truncate a string to a maximum length and append ellipsis if truncated."""
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text


def main():
    """Execution starts here."""
    print("main() start")

    parser = besapi.plugin_utilities.setup_plugin_argparse()

    # allow unknown args to be parsed instead of throwing an error:
    args, _unknown = parser.parse_known_args()

    # allow set global scoped vars
    global bes_conn, verbose, invoke_folder
    verbose = args.verbose

    # get folder the script was invoked from:
    invoke_folder = get_invoke_folder(verbose)

    log_file_path = os.path.join(invoke_folder, get_invoke_file_name(verbose) + ".log")

    logging_config = besapi.plugin_utilities.get_plugin_logging_config(
        log_file_path, verbose, args.console
    )

    logging.basicConfig(**logging_config)
    logging.log(99, "---------- Starting New Session -----------")
    logging.debug("invoke folder: %s", invoke_folder)
    logging.debug("%s's version: %s", get_invoke_file_name(verbose), __version__)
    logging.debug("BESAPI Module version: %s", besapi.besapi.__version__)
    logging.debug("Python version: %s", platform.sys.version)
    logging.warning(
        "Results may be incorrect if not run as a MO or an account without scope of all computers"
    )

    bes_conn = besapi.plugin_utilities.get_besapi_connection(args)

    session_relevance_computers = """(ids of it, names of it) of bes computers whose(now - last report time of it < 60 * day)"""

    results = bes_conn.session_relevance_json(session_relevance_computers)

    json_string = json.dumps(results["result"], indent=2)

    logging.log(99, "Computer Results:\n%s", json_string)

    session_relevance_actions = """(ids of it, names of it) of bes actions whose(now - time issued of it < 60 * day)"""

    results = bes_conn.session_relevance_string(session_relevance_actions)

    logging.log(99, "Action Results:\n%s", results)

    logging.log(99, "---------- Ending Session -----------")


if __name__ == "__main__":
    main()
