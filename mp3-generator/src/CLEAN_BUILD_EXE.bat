@echo off
echo Cleaning old build...
rmdir /s /q build
rmdir /s /q dist
del /q wt_mandarin_mp3_generator_gui.spec
echo.
echo Building WT Mandarin MP3 Generator EXE...
py -m PyInstaller --onefile --windowed wt_mandarin_mp3_generator_gui.py
echo.
echo Clean build selesai. EXE ada di folder dist.
pause
