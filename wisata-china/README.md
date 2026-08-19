# Wisata China — mirror untuk revisi via HP

Folder ini adalah **mirror/cadangan** untuk revisi itinerary trip China dari HP (tanpa laptop), lewat Claude Code.

**Sumber utama tetap di Google Drive laptop:**
- `I:\My Drive\Travelling\China\Itinerary\*.md`
- `I:\My Drive\Travelling\HTML Wisata\Wisata.html`, `generate_wisata.py`, `Update Wisata.bat`

**Alur kerja:**
- Di laptop: tetap edit `.md` di Drive seperti biasa, jalankan `Update Wisata.bat` untuk regenerate `Wisata.html`. Setelah itu, salin hasil terbaru ke folder ini dan `git push` (Claude bisa bantu langkah ini).
- Dari HP (tanpa laptop): minta Claude Code revisi `.md` di folder `Itinerary/` di sini, jalankan `generate_wisata.py` langsung (setara isi `Update Wisata.bat`), commit+push ke GitHub.
- **Begitu laptop nyala lagi:** jalankan `git pull` di folder Drive supaya perubahan dari HP masuk balik ke sumber utama — lihat memory `pending-git-setup-for-mobile-access` untuk detail skrip `.bat` auto-pull (belum dibuat, menyusul).

**Struktur:**
```
wisata-china/
  Itinerary/
    1 Nanjing.md
    2 Wuxi Itinerary.md
    3 Suzhou Itinerary.md
  HTML-Wisata/
    Wisata.html
    generate_wisata.py
    Update Wisata.bat
```

Repo ini **private** — hindari commit data sangat sensitif (nomor paspor, dll) kalau ada di catatan itinerary.
