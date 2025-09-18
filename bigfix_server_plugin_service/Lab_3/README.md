# Lab 3

Setup [computer_group_output.py](../Lab_2/computer_group_output.py) as a BigFix Server Plugin Service

## Setup Plugin

Open the folder `C:\Program Files (x86)\BigFix Enterprise\BES Server\Applications`

Create a folder called `computer_group_output`

Copy [computer_group_output.py](../Lab_2/computer_group_output.py) into the folder `C:\Program Files (x86)\BigFix Enterprise\BES Server\Applications\computer_group_output`

The python script should now be located: `C:\Program Files (x86)\BigFix Enterprise\BES Server\Applications\computer_group_output\computer_group_output.py`

Now open the folder `C:\Program Files (x86)\BigFix Enterprise\BES Server\Applications\Config`

Copy [computer_group_output.xml](computer_group_output.xml) to the folder.

It should now be located: `C:\Program Files (x86)\BigFix Enterprise\BES Server\Applications\Config\computer_group_output.xml`

Now check the end of the `MFS.log` file in this folder: `C:\Program Files (x86)\BigFix Enterprise\BES Server\Applications\Logs`

You should see that the plugin service loaded the new plugin configuration and is running it.

You should check the `computer_group_output.log` file in the folder: `C:\Program Files (x86)\BigFix Enterprise\BES Server\Applications\computer_group_output`

If `computer_group_output.log` does not exist, then that means the plugin service hasn't run it yet, or there is a problem.

The `computer_group_output.log` should show messages of the `computer_group_output.py` plugin running.
