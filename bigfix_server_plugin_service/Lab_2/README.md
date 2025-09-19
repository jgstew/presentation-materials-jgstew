# Lab 2

[Lab 2 Folder](../Lab_2/)

Run this as a python script. Will run it as a BigFix Server Plugin Service in the next lab.

## Install BESAPI Python Module

Run the command:

```
python -m pip install --upgrade besapi
```

Might also need to run this on windows:

```
python -m pip install --upgrade pywin32
```

## Run example computer_group_output.py

Run:

```
python Lab_2/computer_group_output.py
```

Notice the files created. Should be some starting with `Automatic - `

Look at the contents of `Automatic - MasterClass_Computers.txt` and see that it reflects the computers reporting in the console.

Look at the contents of the log file: [computer_group_output.log](computer_group_output.log)

Now run the command again with more verbose output:

```
python Lab_2/computer_group_output.py -v
```

Look at the contents of the log file again: [computer_group_output.log](computer_group_output.log)

See how there is more info in the log output.

Now do this again with even more verbose output:

```
python Lab_2/computer_group_output.py -vv
```
