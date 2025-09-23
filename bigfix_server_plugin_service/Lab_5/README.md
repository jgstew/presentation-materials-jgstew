# Lab 5

[Lab 5 Folder](../Lab_5/)

Advanced: Make your own Server Plugin Service from a plugin starter example template.

## Run as python script:

Run the script:

`python bigfix_server_plugin_service/Lab_5/plugin_example_template.py -v`

See log file:

Look at the contents of the log file: [plugin_example_template.log](plugin_example_template.log)

## Make changes:

Change the session relevance.

Change Line 111 to:

`session_relevance_computers = """(ids of it, names of it, operating systems of it) of bes computers whose(now - last report time of it < 60 * day)"""`

## Run again:

Run the script again:

`python bigfix_server_plugin_service/Lab_5/plugin_example_template.py -v`

And compare the output.

## Run as plugin:

Once satisfied with your changes, you can copy it over to be a plugin same as in Lab 3.

Open the folder `C:\Program Files (x86)\BigFix Enterprise\BES Server\Applications`

Create a folder called `plugin_example_template`

Copy [plugin_example_template.py](plugin_example_template.py) into the folder `C:\Program Files (x86)\BigFix Enterprise\BES Server\Applications\plugin_example_template`

The python script should now be located: `C:\Program Files (x86)\BigFix Enterprise\BES Server\Applications\plugin_example_template\plugin_example_template.py`

Now open the folder `C:\Program Files (x86)\BigFix Enterprise\BES Server\Applications\Config`

Copy [plugin_example_template.xml](plugin_example_template.xml) to the folder.

It should now be located: `C:\Program Files (x86)\BigFix Enterprise\BES Server\Applications\Config\plugin_example_template.xml`

Now check the end of the `MFS.log` file in this folder: `C:\Program Files (x86)\BigFix Enterprise\BES Server\Applications\Logs` to see this new plugin being invoked.

You should check the `plugin_example_template.log` file in the folder: `C:\Program Files (x86)\BigFix Enterprise\BES Server\Applications\plugin_example_template`

## See other examples:

You can look here for more examples of things that can be done with the BigFix REST API and the BESAPI python module:

- https://github.com/jgstew/besapi/tree/master/examples

Some of these examples are already setup to be run as plugins, while others could be adjusted in order to do so.
