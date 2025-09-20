# Lab 4

[Lab 4 Folder](../Lab_4/)

Compile a python BigFix Server Plugin Service to a binary using PyInstaller

## Setup Environment

Install pyinstaller:

Run the command:

```
python -m pip install --upgrade pyinstaller
```

## Run pyinstaller to build script into EXE:

From the `bigfix_server_plugin_service` folder run:

```
pyinstaller --clean --noconfirm --onefile --distpath Lab_4 --collect-all besapi Lab_4/baseline_sync_plugin.py
```

<details><summary>NOTE: for production use:</summary>

don't use `--onefile` with pyinstaller

This will build the baseline_sync_plugin.exe but also an `_internal` folder.

You have to copy both of them into the `Applications\baseline_sync_plugin` folder on the root server.

</details>

## Setup the built EXE to run as a plugin:

From the folder `C:\Program Files (x86)\BigFix Enterprise\BES Server\Applications` create a subfolder `baseline_sync_plugin`

Copy the `baseline_sync_plugin.exe` file to the created folder: `C:\Program Files (x86)\BigFix Enterprise\BES Server\Applications\baseline_sync_plugin`

Copy the `baseline_sync_plugin.xml` file to the config folder: `C:\Program Files (x86)\BigFix Enterprise\BES Server\Applications\Config`
