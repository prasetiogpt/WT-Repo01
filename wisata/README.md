# wisata/ — itinerary trip, source of truth di Git

Payung untuk semua itinerary trip pribadi (bukan cuma China). Repo Git ini adalah **source of
truth** untuk data trip (Markdown itinerary + HTML generator-nya), bukan Google Drive — supaya
tidak ada kebingungan versi laptop vs HP.

**Konvensi struktur — satu subfolder per trip/negara:**
```
wisata/
  china/
    Itinerary/*.md
    HTML-Wisata/  (Wisata.html, generate_wisata.py, Update Wisata.bat)
    sync-from-git-to-drive.bat
    README.md
  <negara-lain>/
    ...pola yang sama...
```

Trip baru (negara lain, dsb.) dapat subfolder sendiri di sini, bukan dicampur ke dalam
`china/`. Detail alur kerja dan catatan khusus tiap trip ada di README masing-masing subfolder.

Untuk pembuatan itinerary baru (bukan revisi file yang sudah ada), lihat skill account-level
`wisata-itinerary-planner` — itu skill terpisah yang mengatur gaya/preferensi itinerary
(budget, makanan, transportasi, dll), dengan catatan sumber peta khusus per negara (Amap untuk
China, Google Maps di luar China). Skill itu tidak tahu soal struktur repo/git ini — kalau hasil
itinerary dari skill itu mau disimpan permanen, taruh di subfolder trip yang sesuai di sini dan
commit+push.

Repo ini **private** — hindari commit data sangat sensitif (nomor paspor, dll) kalau ada di
catatan itinerary.
