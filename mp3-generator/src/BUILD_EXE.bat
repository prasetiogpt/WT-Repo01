@echo off
echo Building WT Mandarin MP3 Generator EXE...
echo.
py -m PyInstaller --onefile --windowed wt_mandarin_mp3_generator_gui.py
echo.
echo Build selesai. EXE ada di folder dist.
pause
