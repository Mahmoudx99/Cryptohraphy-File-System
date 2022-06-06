import sys, os
from cx_Freeze import setup, Executable

os.environ["TCL_LIBRARY"] = "C:/Users/Dell/anaconda3/envs/security/tcl/tcl8.6"
os.environ["TK_LIBRARY"] = "C:/Users/Dell/anaconda3/envs/security/tcl/tk8.6"

base = None
include_files = [
    "./assets",
    "C:/Users/Dell/anaconda3/envs/security/DLLs/tcl86t.dll",
    "C:/Users/Dell/anaconda3/envs/security/DLLs/tk86t.dll"
]

if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="File Encryption",
    version="1.4",
    description="File Encryption App",
    options={
        "build_exe": {
            "include_files": include_files
            }
    },
    executables=[
        Executable(
            "FileCryptoSystem.py",
            base=base,
            targetName="FileCryptoSystem.exe",
            icon="./assets/icon.ico"
        )
    ]
)
