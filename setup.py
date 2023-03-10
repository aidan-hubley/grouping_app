import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    'Grouping-%s%' 'main.py',
    '--onefile',
    '--noconsole',
    os.path.join('', 'main.py'), """your script and path to the script"""
])