# Lab 4

[Lab 4 Folder](../Lab_4/)

Compile a python BigFix Server Plugin Service to a binary using PyInstaller

## Setup Environment

Install pyinstaller:

Run the command:

```
python -m pip install --upgrade pyinstaller
```

## Run pyinstaller to build script:

```
pyinstaller --clean --noconfirm --one-file --distpath Lab_4 --collect-all besapi Lab_4/baseline_sync_plugin.py
```
