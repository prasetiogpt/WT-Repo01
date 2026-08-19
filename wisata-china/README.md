# Wisata China — source of truth ada di Git

Folder ini adalah **source of truth (SOT)** untuk itinerary trip China: `.md` itinerary dan
`Wisata.html` (+ generator-nya). Sudah dipindahkan dari laptop ke repo Git ini supaya tidak ada
lagi kebingungan versi antara laptop dan HP.

**Google Drive laptop sekarang cuma mirror/working-copy lokal:**
- `I:\My Drive\Travelling\China\Itinerary\*.md`
- `I:\My Drive\Travelling\HTML Wisata\Wisata.html`, `generate_wisata.py`, `Update Wisata.bat`

**Alur kerja (Git = sumber kebenaran, selalu commit+push dari sini):**
- Dari HP atau laptop lewat Claude Code: revisi `.md` di folder `Itinerary/` di repo ini,
  jalankan `generate_wisata.py` untuk regenerate `Wisata.html`, lalu commit+push ke GitHub.
  **Jangan edit langsung di Drive** — supaya tidak ada dua versi yang beda.
- Di laptop (kalau perlu edit manual atau pakai `Update Wisata.bat`): jalankan `git pull` dulu
  di folder repo, lalu jalankan `sync-from-git-to-drive.bat` untuk menyalin versi terbaru dari
  Git ke folder Drive sebelum mulai kerja. Setelah selesai edit + regenerate di laptop, salin
  hasilnya balik ke folder ini di repo dan `git push` — Drive tidak pernah jadi sumber yang
  di-push duluan.
- `sync-from-git-to-drive.bat` sudah otomatis `git pull` lalu copy `Itinerary/*.md` dan file
  `HTML-Wisata/*` terbaru dari repo ke folder Drive — jalankan ini di laptop kapan pun sebelum
  mulai kerja di sana, supaya Drive selalu selaras dengan Git.

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
