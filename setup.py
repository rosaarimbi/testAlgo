import sys 
from cx_Freeze import setup, Executable


my_options = {"packages": ["os"], "excludes": ["tkinter"]}

base =  None
if sys.platform == "win32":
    base = "Win32GUI"
setup(
    name = "Shooter Game",
    version = "2.0",
    description = "Game Shooter By Gabut",
    options = {"build_exe": my_options},
    executables = [Executable("result.py", base=base)]
)
