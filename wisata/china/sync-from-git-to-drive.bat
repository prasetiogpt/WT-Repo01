@echo off
setlocal

set "REPO=C:\Users\admin\git-repos\wt-repo01"
set "DRIVE_ITIN=I:\My Drive\Travelling\China\Itinerary"
set "DRIVE_HTML=I:\My Drive\Travelling\HTML Wisata"
set "LOG=%REPO%\wisata\china\sync.log"

echo [%date% %time%] Starting wisata git sync... >> "%LOG%"

cd /d "%REPO%"
git pull origin main >> "%LOG%" 2>&1

if exist "%DRIVE_ITIN%" (
  copy /Y "%REPO%\wisata\china\Itinerary\*.md" "%DRIVE_ITIN%\" >> "%LOG%" 2>&1
  echo   - Itinerary .md copied to Drive >> "%LOG%"
) else (
  echo   - SKIPPED: Drive Itinerary folder not found, ^(mount offline?^) >> "%LOG%"
)

if exist "%DRIVE_HTML%" (
  copy /Y "%REPO%\wisata\china\HTML-Wisata\Wisata.html" "%DRIVE_HTML%\" >> "%LOG%" 2>&1
  copy /Y "%REPO%\wisata\china\HTML-Wisata\generate_wisata.py" "%DRIVE_HTML%\" >> "%LOG%" 2>&1
  copy /Y "%REPO%\wisata\china\HTML-Wisata\Update Wisata.bat" "%DRIVE_HTML%\" >> "%LOG%" 2>&1
  echo   - HTML Wisata files copied to Drive >> "%LOG%"
) else (
  echo   - SKIPPED: Drive HTML Wisata folder not found ^(mount offline?^) >> "%LOG%"
)

echo [%date% %time%] Sync done. >> "%LOG%"
echo. >> "%LOG%"

endlocal
