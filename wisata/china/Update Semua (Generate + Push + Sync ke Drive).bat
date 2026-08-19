@echo off
setlocal

set "REPO=C:\Users\admin\git-repos\wt-repo01"
set "DRIVE_ITIN=I:\My Drive\Travelling\China\Itinerary"
set "DRIVE_HTML=I:\My Drive\Travelling\HTML Wisata"

echo ============================================
echo   1/5 - Tarik perubahan terbaru dari GitHub
echo ============================================
cd /d "%REPO%"
git pull origin main
if errorlevel 1 (
    echo.
    echo [!] git pull GAGAL - cek koneksi internet / konflik dulu sebelum lanjut.
    pause
    exit /b 1
)

echo.
echo ============================================
echo   2/5 - Generate Wisata.html dari .md terbaru
echo ============================================
cd /d "%REPO%\wisata\china"
py ..\HTML-Wisata\generate_wisata.py china
if errorlevel 1 (
    echo.
    echo [!] Generate GAGAL - cek pesan error di atas. Wisata.html BELUM diupdate.
    pause
    exit /b 1
)

echo.
echo ============================================
echo   3/5 - Commit + push ke GitHub
echo ============================================
cd /d "%REPO%"
git add wisata\china
git diff --cached --quiet
if errorlevel 1 (
    git commit -m "Update itinerary (self-serve dari laptop)"
    git push origin main
    echo   - Berhasil push ke GitHub.
) else (
    echo   - Tidak ada perubahan baru untuk di-commit, skip push.
)

echo.
echo ============================================
echo   4/5 - Copy ke folder Drive
echo ============================================
if exist "%DRIVE_ITIN%" (
    copy /Y "%REPO%\wisata\china\Itinerary\*.md" "%DRIVE_ITIN%\"
    echo   - Itinerary .md ter-copy ke Drive.
) else (
    echo   - SKIPPED: folder Drive Itinerary tidak ditemukan.
)
if exist "%DRIVE_HTML%" (
    copy /Y "%REPO%\wisata\china\Wisata.html" "%DRIVE_HTML%\"
    echo   - Wisata.html ter-copy ke Drive.
) else (
    echo   - SKIPPED: folder Drive HTML Wisata tidak ditemukan.
)

echo.
echo ============================================
echo   5/5 - Selesai!
echo ============================================
echo Semua sudah diperbarui: git (GitHub) + Drive.
echo Jangan lupa republish Artifact-nya kalau perlu link yang sama tetap update.
pause

endlocal
