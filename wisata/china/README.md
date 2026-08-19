# Wisata China — source of truth ada di Git

Ini adalah subfolder khusus trip **China** di bawah `wisata/` (lihat `../README.md` untuk
konvensi umum lintas negara, termasuk generator `Wisata.html` yang SHARED lintas negara — bukan
punya sendiri per negara). Folder ini adalah **source of truth (SOT)** untuk itinerary trip
China: `.md` itinerary dan `Wisata.html`. Sudah dipindahkan dari laptop ke repo Git ini supaya
tidak ada lagi kebingungan versi antara laptop dan HP.

**Google Drive laptop sekarang cuma mirror/working-copy lokal (view-only):**
- `I:\My Drive\Travelling\China\Itinerary\*.md`
- `I:\My Drive\Travelling\HTML Wisata\Wisata.html`

**Alur kerja (Git = sumber kebenaran, selalu commit+push dari sini):**
- Dari HP atau laptop lewat Claude Code: revisi `.md` di folder `Itinerary/` di repo ini,
  jalankan `py ../HTML-Wisata/generate_wisata.py china` (dari folder ini) untuk regenerate
  `Wisata.html`, lalu commit+push ke GitHub. **Jangan edit langsung di Drive** — supaya tidak ada
  dua versi yang beda.
- Di laptop (kalau perlu edit manual atau pakai `../HTML-Wisata/Update Wisata.bat`): jalankan
  `git pull` dulu di folder repo (bukan di Drive — generate selalu dari clone repo, Drive cuma
  tujuan sync satu arah), edit/generate dari situ, lalu commit+push. Setelah itu jalankan
  `sync-from-git-to-drive.bat` untuk menyalin versi terbaru dari Git ke folder Drive supaya Drive
  ikut ter-update (buat dibuka/dilihat saja, bukan buat diedit).
- `sync-from-git-to-drive.bat` otomatis `git pull` lalu copy `Itinerary/*.md` dan `Wisata.html`
  terbaru dari repo ke folder Drive — jalankan ini di laptop kapan pun sebelum mau lihat versi
  terbaru di Drive.

**Struktur:**
```
wisata/china/
  Itinerary/
    1 Nanjing.md
    2 Wuxi Itinerary.md
    3 Suzhou Itinerary.md
  Wisata.html            <- output generator (generator-nya sendiri ada di ../HTML-Wisata/, shared)
  sync-from-git-to-drive.bat
  README.md   (file ini)
```

Repo ini **private** — hindari commit data sangat sensitif (nomor paspor, dll) kalau ada di catatan itinerary.
