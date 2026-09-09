# Wisata China — source of truth ada di Git

Ini adalah subfolder khusus trip **China** di bawah `wisata/` (lihat `../README.md` untuk
konvensi umum lintas negara, termasuk generator `Wisata.html` yang SHARED lintas negara — bukan
punya sendiri per negara). Folder ini adalah **source of truth (SOT)** untuk itinerary trip
China: `.md` itinerary dan `Wisata.html`. Sudah dipindahkan dari laptop ke repo Git ini supaya
tidak ada lagi kebingungan versi antara laptop dan HP.

**Google Drive laptop sekarang cuma mirror/working-copy lokal (view-only):**
- `I:\My Drive\Travelling\China\Itinerary\*.md`
- `I:\My Drive\Travelling\HTML Wisata\Wisata.html`

**Repo ini publik sejak 2026-09-06, dan `Wisata.html` dibuka lewat GitHub Pages di HP:**
```
https://prasetiogpt.github.io/WT-Repo01/wisata/china/Wisata.html
```
Pages serve langsung dari branch **`main`** (Deploy from a branch, root `/`) — sama seperti HTML
Mandarin Player. Artinya: **revisi apapun baru kelihatan di HP kalau sudah ada di `main`**, bukan
cukup di-commit ke branch lain. Kalau sesi kerja (mis. Claude Code on the web) diwajibkan develop
di branch terpisah, WAJIB tambahan langkah merge/fast-forward branch itu ke `main` lalu push
`main` sebelum dianggap selesai — jangan berhenti di commit+push ke branch kerja saja.

**Alur kerja (Git = sumber kebenaran, selalu commit+push dari sini):**
- Dari HP atau laptop lewat Claude Code: revisi `.md` di folder `Itinerary/` di repo ini,
  jalankan `py ../HTML-Wisata/generate_wisata.py china` (dari folder ini) untuk regenerate
  `Wisata.html`, lalu commit+push ke GitHub — **pastikan sampai di `main`** (lihat paragraf di
  atas). **Jangan edit langsung di Drive** — supaya tidak ada dua versi yang beda.
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

**Itinerary custom-test (bukan revisi trip aktual — skill `wisata-itinerary-planner` poin 13
Mode Itinerary Kustom, khusus dipakai untuk sekadar coba mekanisme skill):** nama file pakai
`<nomor unik lebih besar dari nomor kota manapun> <Kota> xia<N>.md` (mis. `9 Xiamen xia1.md`,
test berikutnya `10 Xiamen xia2.md`, dst — angka boleh naik bebas, generator sort by nama file
jadi angka lebih besar otomatis render sebagai tab paling belakang). **Bukan** konvensi
`C<Angka>` default skill (itu untuk revisi custom yang memang menempel ke jadwal kota asli) —
`xia1`/`xia2` khusus supaya (a) selalu di tab paling belakang, (b) nama/id destinasi beda dari
kota aslinya jadi tidak ketuker di tab bar (tambahkan juga entri `AIRPORT_CODES` di
`Wisata.html` kalau kode 3-huruf fallback-nya bentrok dengan tab lain, lihat contoh
`xiamenxia1:'XIA1'`).

Repo ini **publik** (lihat catatan Pages di atas) — hindari commit data sangat sensitif (nomor
paspor, dll) kalau ada di catatan itinerary.
