# wisata/ — itinerary trip, source of truth di Git

Payung untuk semua itinerary trip pribadi (bukan cuma China). Repo Git ini adalah **source of
truth** untuk data trip (Markdown itinerary + HTML generator-nya), bukan Google Drive — supaya
tidak ada kebingungan versi laptop vs HP.

**Konvensi struktur:**
```
wisata/
  HTML-Wisata/          <- generator SHARED, dipakai semua negara (bukan per-negara)
    generate_wisata.py
    Update Wisata.bat
  china/
    Itinerary/*.md
    Wisata.html          <- output generator, khusus punya negara ini
    sync-from-git-to-drive.bat
    README.md
  <negara-lain>/
    Itinerary/*.md
    Wisata.html
    ...pola yang sama...
```

`generate_wisata.py` di `wisata/HTML-Wisata/` cuma parser Markdown generic (tidak ada logika
khusus China di dalamnya) — dipakai untuk SEMUA negara, satu file, tidak digandakan per-negara.
Jalankan dengan nama folder negara sebagai argumen:
```
py wisata/HTML-Wisata/generate_wisata.py china
```
Ini membaca `wisata/china/Itinerary/*.md` dan menulis ulang blok data di `wisata/china/Wisata.html`
(file `Wisata.html` itu sendiri harus sudah ada duluan di folder negara itu — untuk negara baru,
copy `Wisata.html` dari negara yang sudah ada sebagai starting shell, lalu isi `Itinerary/`-nya).
`Update Wisata.bat` di folder yang sama adalah wrapper interaktif yang tanya nama folder negara.

Trip baru (negara lain, dsb.) dapat subfolder sendiri di `wisata/`, bukan dicampur ke dalam
`china/`. Detail alur kerja dan catatan khusus tiap trip ada di README masing-masing subfolder.

Untuk pembuatan itinerary baru (bukan revisi file yang sudah ada), lihat skill account-level
`wisata-itinerary-planner` — itu skill terpisah yang mengatur gaya/preferensi itinerary
(budget, makanan, transportasi, dll), dengan catatan sumber peta khusus per negara (Amap untuk
China, Google Maps di luar China). Skill itu tidak tahu soal struktur repo/git ini — kalau hasil
itinerary dari skill itu mau disimpan permanen, taruh di subfolder trip yang sesuai di sini dan
commit+push.

Repo ini **private** — hindari commit data sangat sensitif (nomor paspor, dll) kalau ada di
catatan itinerary.
