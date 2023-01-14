import sys, os
from cx_Freeze import setup, Executable

py_package = ["os", "sys", "PyQt6", "requests", "pynput", "src"]

# base="Win32GUI" should be used only for Windows GUI app
base = None
exes = None
PATH = os.path.dirname(os.path.realpath(__file__))

themeDir = os.path.join(PATH, "src", "theme")
outputDir = os.path.join(PATH, "Output")
LICENSE = os.path.join(PATH, "LICENSE")

if sys.platform == "win32":
    base = "Win32GUI"
    copy_path = "src"
    src_files = [(themeDir, os.path.join("src", "theme")), (outputDir, "Output"), (LICENSE, "LICENSE")]
    build_exe_options = {"packages": py_package,
     "include_files": src_files,
      "excludes": ["tkinter", "numpy", "pydoc_data", "distutils", "setuptools"],
      "optimize": 2,
      "replace_paths": [(PATH, "*")]
      }


exes = [Executable("src/main.py",
                    base=base,
                    icon=os.path.join(PATH, "src", "resources", "icon.ico"),
                    shortcut_dir="ProgramMenuFolder",
                    target_name="TeleScore")]

setup(
    name="TeleScore",
    version="1.0",
    description="TeleScore - Open Source Scoreboard Software",
    options={"build_exe": build_exe_options},
    executables=exes,
)
