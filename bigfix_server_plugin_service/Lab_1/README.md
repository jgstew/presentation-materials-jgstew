# Lab 1

[Lab 1 Folder](../Lab_1/)

Setup fake example plugin

NOTE: if you are not doing this from a root server already configured for the Plugin Service, you may need to do some prerequisites. See [Lab 0](../Lab_0/README.md)

## For Windows Root Servers:

Copy [`fake_example_win.xml`](fake_example_win.xml) file to `C:\Program Files (x86)\BigFix Enterprise\BES Server\Applications\Config` folder

Wait for fake example plugin to run, which should be quick.

Check MFS log here: `C:\Program Files (x86)\BigFix Enterprise\BES Server\Applications\Logs\MFS.log`

Once it has run, check the contents of file `C:\tmp\bigfix_example_plugin_output.txt`

Notice in [`fake_example_win.xml`](fake_example_win.xml) in the `<Command>` section, you see `%BESHTTP%` but

Notice in `C:\tmp\bigfix_example_plugin_output.txt` you instead see `http://besfndwinroot:52311` or similar.

This is because the BigFix Server Plugin Service knows to substitute those special variables for you.

## Next Lab:

[Lab 2](../Lab_2/README.md)
