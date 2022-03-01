:: Reset the build folder
if exist build rmdir /s /q build
mkdir build
cd build

:: Run the python build script
python3 -m PyInstaller --name "videoDeduper" --hidden-import=pkg_resources --onefile --icon ../icons/mov.ico ../main.py

:: Copy the readme and licence
copy ..\LICENSE dist\LICENSE
copy ..\README.md dist\README.md

:: Exit out of the build dir
cd ../