#!/bin/bash
# Versi Mac dari "Update Semua (Generate + Push + Sync ke Drive).bat"
# Generate Wisata.html dari .md terbaru, commit+push ke GitHub, lalu copy ke folder Drive.

set -uo pipefail

REPO="$HOME/git-repos/wt-repo01"
DRIVE_ITIN="$HOME/Library/CloudStorage/GoogleDrive-prasetiogpt@gmail.com/My Drive/Travelling/China/Itinerary"
DRIVE_HTML="$HOME/Library/CloudStorage/GoogleDrive-prasetiogpt@gmail.com/My Drive/Travelling/HTML Wisata"

echo "============================================"
echo "  1/6 - Tarik perubahan terbaru dari GitHub"
echo "============================================"
cd "$REPO" || { echo "[X] Folder repo tidak ditemukan: $REPO"; exit 1; }
if ! git pull origin main; then
    echo
    echo "[X] git pull GAGAL - cek koneksi internet / konflik dulu sebelum lanjut."
    read -p "Tekan Enter untuk keluar..."
    exit 1
fi

echo
echo "============================================"
echo "  2/6 - Cek revisi dari sesi HP/cloud (branch terpisah)"
echo "============================================"
echo "  Sesi Claude di HP kadang push ke branch sendiri, BUKAN main -"
echo "  git pull di atas TIDAK menangkap ini. Cek branch yang relevan ke wisata/china."
git fetch origin >/dev/null 2>&1

FOUND_BRANCH=0
for BR in $(git branch -r | grep "origin/claude/" | sed 's/^[[:space:]]*origin\///'); do
    if ! git merge-base --is-ancestor "origin/$BR" main >/dev/null 2>&1; then
        if ! git diff --quiet main "origin/$BR" -- wisata/china >/dev/null 2>&1; then
            FOUND_BRANCH=1
            echo "  - Branch relevan ditemukan: $BR"
            if git merge --ff-only "origin/$BR"; then
                echo "  - Berhasil digabung ke main."
            else
                echo "  [X] Tidak bisa digabung otomatis (bukan fast-forward, ada percabangan)."
                echo "      Minta bantuan Claude di sesi ini untuk merge manual - JANGAN dipaksa."
            fi
        fi
    fi
done
if [ "$FOUND_BRANCH" = "0" ]; then
    echo "  - Tidak ada branch sesi lain yang relevan, lanjut seperti biasa."
fi
git push origin main >/dev/null 2>&1

echo
echo "============================================"
echo "  3/6 - Generate Wisata.html dari .md terbaru"
echo "============================================"
cd "$REPO/wisata/china" || exit 1
if ! python3 ../HTML-Wisata/generate_wisata.py china; then
    echo
    echo "[X] Generate GAGAL - cek pesan error di atas. Wisata.html BELUM diupdate."
    read -p "Tekan Enter untuk keluar..."
    exit 1
fi

echo
echo "============================================"
echo "  4/6 - Commit + push ke GitHub"
echo "============================================"
cd "$REPO" || exit 1
git add wisata/china
if ! git diff --cached --quiet; then
    git commit -m "Update itinerary (self-serve dari laptop)"
    git push origin main
    echo "  - Berhasil push ke GitHub."
else
    echo "  - Tidak ada perubahan baru untuk di-commit, skip push."
fi

echo
echo "============================================"
echo "  5/6 - Copy ke folder Drive"
echo "============================================"
if [ -d "$DRIVE_ITIN" ]; then
    cp -f "$REPO/wisata/china/Itinerary/"*.md "$DRIVE_ITIN/"
    echo "  - Itinerary .md ter-copy ke Drive."
else
    echo "  - SKIPPED: folder Drive Itinerary tidak ditemukan (cek path di script ini)."
fi
if [ -d "$DRIVE_HTML" ]; then
    cp -f "$REPO/wisata/china/Wisata.html" "$DRIVE_HTML/"
    echo "  - Wisata.html ter-copy ke Drive."
else
    echo "  - SKIPPED: folder Drive HTML Wisata tidak ditemukan (cek path di script ini)."
fi

echo
echo "============================================"
echo "  6/6 - Selesai!"
echo "============================================"
echo "Semua sudah diperbarui: git (GitHub) + Drive."
echo "Jangan lupa republish Artifact-nya kalau perlu link yang sama tetap update."
read -p "Tekan Enter untuk keluar..."
