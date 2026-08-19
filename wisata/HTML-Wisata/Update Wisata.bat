@echo off
cd /d "%~dp0"
echo ============================================
echo   Update Wisata.html dari file Markdown
echo ============================================
echo.
set /p COUNTRY="Nama folder negara (mis. china): "
py generate_wisata.py %COUNTRY%
echo.
echo ============================================
if errorlevel 1 (
    echo Ada masalah di atas -- Wisata.html BELUM diupdate.
) else (
    echo Selesai. Wisata.html sudah diupdate.
)
echo ============================================
pause
