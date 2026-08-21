@echo off
setlocal enabledelayedexpansion

set "REPO=C:\Users\admin\git-repos\wt-repo01"
set "DRIVE_ITIN=I:\My Drive\Travelling\China\Itinerary"
set "DRIVE_HTML=I:\My Drive\Travelling\HTML Wisata"

echo ============================================
echo   1/6 - Tarik perubahan terbaru dari GitHub
echo ============================================
cd /d "%REPO%"
git pull origin main
if errorlevel 1 (
    echo.
    echo [X] git pull GAGAL - cek koneksi internet / konflik dulu sebelum lanjut.
    pause
    exit /b 1
)

echo.
echo ============================================
echo   2/6 - Cek revisi dari sesi HP/cloud ^(branch terpisah^)
echo ============================================
echo   Sesi Claude di HP kadang push ke branch sendiri, BUKAN main -
echo   git pull di atas TIDAK menangkap ini. Cek branch yang relevan ke wisata\china.
git fetch origin >nul 2>&1
set FOUND_BRANCH=0
for /f "tokens=*" %%b in ('git branch -r ^| findstr /c:"origin/claude/"') do (
    set "BR=%%b"
    set "BR=!BR: =!"
    set "BR=!BR:origin/=!"
    git merge-base --is-ancestor origin/!BR! main >nul 2>&1
    if errorlevel 1 (
        git diff --quiet main origin/!BR! -- wisata\china >nul 2>&1
        if errorlevel 1 (
            set FOUND_BRANCH=1
            echo   - Branch relevan ditemukan: !BR!
            git merge --ff-only origin/!BR!
            if errorlevel 1 (
                echo   [X] Tidak bisa digabung otomatis ^(bukan fast-forward, ada percabangan^).
                echo       Minta bantuan Claude di sesi ini untuk merge manual - JANGAN dipaksa.
            ) else (
                echo   - Berhasil digabung ke main.
            )
        )
    )
)
if "%FOUND_BRANCH%"=="0" echo   - Tidak ada branch sesi lain yang relevan, lanjut seperti biasa.
git push origin main >nul 2>&1

echo.
echo ============================================
echo   3/6 - Generate Wisata.html dari .md terbaru
echo ============================================
cd /d "%REPO%\wisata\china"
py ..\HTML-Wisata\generate_wisata.py china
if errorlevel 1 (
    echo.
    echo [X] Generate GAGAL - cek pesan error di atas. Wisata.html BELUM diupdate.
    pause
    exit /b 1
)

echo.
echo ============================================
echo   4/6 - Commit + push ke GitHub
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
echo   5/6 - Copy ke folder Drive
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
echo   6/6 - Selesai!
echo ============================================
echo Semua sudah diperbarui: git (GitHub) + Drive.
echo Jangan lupa republish Artifact-nya kalau perlu link yang sama tetap update.
pause

endlocal
