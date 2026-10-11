#!/bin/bash
# Versi Mac dari "Update Wisata.bat"
# Regenerate Wisata.html dari file Markdown untuk 1 folder negara.

cd "$(dirname "$0")" || exit 1
echo "============================================"
echo "  Update Wisata.html dari file Markdown"
echo "============================================"
echo
read -p "Nama folder negara (mis. china): " COUNTRY
python3 generate_wisata.py "$COUNTRY"
RESULT=$?
echo
echo "============================================"
if [ $RESULT -ne 0 ]; then
    echo "Ada masalah di atas -- Wisata.html BELUM diupdate."
else
    echo "Selesai. Wisata.html sudah diupdate."
fi
echo "============================================"
read -p "Tekan Enter untuk keluar..."
