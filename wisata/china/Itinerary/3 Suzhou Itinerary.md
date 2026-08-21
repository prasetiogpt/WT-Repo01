# Itinerary Perjalanan Suzhou
10 – 14 Oktober · 4 Malam · Direncanakan Independen (bukan sambungan kota lain)

> **Master file** — edit di sini dulu untuk revisi cepat. PDF (`Suzhou Itinerary.pdf`) di-generate ulang dari file ini hanya saat diminta.
>
> ⚠️ Riwayat revisi: (1) **Sinkronisasi format ke standar Nanjing/Wuxi** — kolom Kegiatan di semua tabel itinerary (Hari 1-4, Opsional A/B) sekarang bold selektif, hanya nama destinasi wisata yang di-`**bold**` (baris transit/logistik/makan polos dibiarkan tanpa bold); (2) seluruh 30 entri Lampiran (termasuk Cadangan & Plan-B) dilengkapi Hanzi + badge verifikasi, `**Akses:**` (jalur MRT/exit/jarak jalan kaki), `**Jam Operasional:**`, dan `**Tiket:**` (CNY+IDR, kurs tetap Rp2.650/CNY) — diriset via web search, ditandai ⚠️ kalau tidak ditemukan sumber resmi/pasti, bukan tebakan; (3) "Guanqian Street & Xuanmiao Temple" dan "Zhouzhuang / Tongli Water Town" dipecah masing-masing jadi 2 entri terpisah (satu `###` = satu tempat, sesuai aturan parser); (4) dikoreksi kerancuan penamaan di entri "Suzhou Amusement Land / Window of the World" — "Window of the World" sebenarnya taman berbeda di Shenzhen, bukan bagian dari Suzhou Amusement Land (苏州乐园); entri diganti jadi murni Suzhou Amusement Land dengan catatan koreksi; (5) diperbaiki bug parser `generate_wisata.py` — heading Lampiran "## Opsional A" dan "## Opsional B" sebelumnya tidak dikenali parser (entrinya diam-diam ter-skip dari Wisata.html); ditambahkan pengenalan generik untuk heading `## Opsional <label>` di parser; (6) **Revisi besar 2026-08-19** — tanggal digeser jadi **10–14 Oktober (4 malam, 5 hari)** sesuai jadwal baru; **hotel dikoreksi** ke Suzhou City Holiday Hotel (Shiquan Street·Wangshi Garden), Gusu District, dengan anchor MRT **Nanyuanbeilu (Line 5)** — SELURUH rute harian & moda transportasi disusun ulang dari titik ini (bukan lagi asumsi hotel lama); **city independence diterapkan** — Hari 1 & Hari 5 tidak lagi menyambung jadwal transportasi aktual kota sebelumnya (`[[itinerary-continuity]]` sudah SUPERSEDED), dipakai default kedatangan 17:00/kepulangan pola skill terbaru, dengan pengecualian Hari 5 yang pakai data riil jadwal HSR Suzhou→Ningbo; **Opsional A (Taihu Lake) & Opsional B (Jinji Lake malam/Music Fountain) diaktifkan kembali ke badan itinerary utama** (Hari 5 & Hari 4) karena durasi Suzhou diperpanjang jadi 5 hari — section "## Opsional" dihapus, entri Lampiran-nya dipindah ke grup Hari terkait; **rute Panmen & Wumen Bridge disederhanakan** karena sekarang persis 1 halte MRT dari hotel (dulu perlu perjalanan lebih jauh); **leg pulang dikoreksi** dari asumsi lama ke **HSR Suzhou → Ningbo** via Suzhou Railway Station (bukan Guangzhou — itu leg trip terpisah yang belum diputuskan); seluruh tabel budget dihitung ulang untuk struktur 5 hari; (7) **2026-08-21** — ditambahkan rating hotel (⭐⭐⭐⭐, 9.4/10, 17.650 ulasan) dan info stasiun tambahan **Suzhou Industrial Park Railway Station** (11,4km/±30 menit) dari screenshot Amap pengguna; (8) **2026-08-21 — bug fix parser**: sempat dicoba format tabel terpisah "## Hotel & Transportasi" — ternyata bikin info hotel HILANG dari Wisata.html, karena `generate_wisata.py` cuma mengenali heading persis `## Informasi Penerbangan`/`## Informasi Transportasi` (tidak match dengan varian "(Kedatangan)" yang dipakai di sini) dan tidak punya handler untuk heading `##` custom apa pun di luar daftar yang dikenali (di-skip diam-diam, bukan error) — heading "Informasi Transportasi (Kedatangan)" dikembalikan jadi persis "Informasi Transportasi", dan info hotel dikembalikan jadi prose (bukan tabel terpisah) menyatu di section yang sama, sesuai konvensi Nanjing/Wuxi (`### Hotel` sebagai sub-heading H3 tetap ikut ter-parse sebagai prose dalam section H2 induknya — H3 TIDAK memulai section baru, beda dari H2); (9) **2026-08-21 — dipangkas info berulang/kurang relevan**: paragraf "Kenapa Hari 1 dimulai sore" dan "Prioritas transportasi lokal" dihapus (sudah default skill, tidak perlu diulang per file), blockquote "Kota disusun independen" dihapus (duplikat), tabel Informasi Transportasi Pulang dipadatkan (alasan pemilihan stasiun/detail teknis dipangkas jadi 1 kalimat inti) — tujuan: layar lebih fokus ke info yang benar-benar spesifik trip ini.

> **✅ Sudah lewat Golden Week:** Golden Week resmi 1–8 Oktober. Trip Suzhou 10–14 Oktober ini sepenuhnya di luar periode itu — jauh lebih tenang. Sabtu (11 Okt) tetap akhir pekan domestik biasa, jadi mungkin sedikit lebih ramai dari hari kerja tapi tidak sebanding puncak Golden Week.

## Informasi Transportasi

| | |
|---|---|
| Tanggal & Jam Kedatangan | Jumat, 10 Oktober, **±17:00** |
| Titik kedatangan → Hotel | Taksi/Didi singkat ke hotel |

**Catatan biaya:** semua angka CNY/IDR di bawah untuk **2 orang (dewasa)**. Kurs dipakai: **Rp2.650/CNY** (kurs tetap, lihat [[exchange-rates]]). Tanda — berarti gratis/tidak ada biaya. Ongkos transportasi MASUK ke Suzhou (dari kota/titik sebelumnya) TIDAK dihitung di sini (di luar scope budget Suzhou, konsisten dengan prinsip kota independen).

**Hotel:** Suzhou City Holiday Hotel (Shiquan Street·Wangshi Garden) — 苏州城市假日酒店(十全街网师园店), ⭐⭐⭐⭐ rating 9.4/10 (17.650 ulasan). No. 77 North Nanyuan Road (北南园路77号), Canglang Subdistrict, Gusu District, Suzhou. ±4,8km (garis lurus) dari pusat kota. Anchor MRT: **Nanyuanbeilu Station (南园北路, Line 5)**, ±140m/±2 menit jalan kaki — dipakai sebagai basis SEMUA rute harian di bawah. Stasiun/terminal lain di sekitar hotel: Nanmen Metro Station (1,2km/±17 menit jalan kaki), Suzhou South Gate Passenger Transport Terminal (bus, 1,4km/±20 menit jalan kaki), Suzhou Railway Station (苏州站, stasiun HSR utama — 5,9km/±27 menit naik mobil, TIDAK dekat/jalan kaki), Suzhou Industrial Park Railway Station (苏州工业园区站, 11,4km/±30 menit naik mobil, relevan hanya untuk leg dari arah timur/Jinji Lake).

Line 5 membentang barat daya–timur laut melewati 34 stasiun, dan kebetulan strategis untuk hotel ini karena: **1 halte ke arah barat daya → Nanmen (南门)**, interchange ke **Line 4** — juga stasiun MRT untuk kawasan **Panmen Scenic Spots**, jadi kluster selatan kota tua praktis di depan hotel; **3 halte ke arah barat daya → Laodonglu (劳动路)**, interchange ke **Line 2** — jalur ke kawasan Hanshan Temple/Shantang Street; **Line 5 langsung TANPA transfer ke Taihu Xiangshan (太湖香山)**, terminus barat daya, persis di kawasan resor Danau Taihu — jadi Taihu tidak perlu taksi PP penuh, cukup naik Line 5 lurus lalu taksi/bus pendek dari stasiun ke titik wisatanya. Transportasi ke Suzhou Railway Station (Hari 5) pakai taksi/Didi langsung ATAU Line 5→Nanmen/Laodonglu→transfer Line 2/4 (interchange Line 2 & Line 4).

## Informasi Transportasi Pulang

| | |
|---|---|
| Rute | Suzhou → Ningbo via HSR (kereta cepat) |
| Stasiun keberangkatan | **Suzhou Railway Station (苏州站 · Sūzhōu Zhàn)** — lebih dekat dari hotel dibanding Suzhou North (5,9km vs ±16km) |
| Tanggal & jam berangkat (rencana) | Selasa, 14 Oktober, **±15:00** (belum jadwal terkunci — ±19 kereta G/D per hari 07:15–18:08, cek nomor kereta persis di 12306/Trip.com H-7) |
| Durasi HSR | ±2 jam 27 menit – 3,5 jam (tergantung kereta) |
| Estimasi biaya HSR | ±CNY 147–218/org kelas 2 (masuk budget Ningbo, tidak dihitung di sini) |
| Hotel → Stasiun | Taksi/Didi langsung, ±27 menit |

---

## Ringkasan Cuaca & Persiapan (Oktober di Suzhou)

- Suhu siang rata-rata **±23°C**, malam **±14–16°C** — sejuk & nyaman, salah satu periode terbaik untuk berjalan kaki jauh di kota tua.
- Kelembapan ±71%, hujan ringan ±9-10 hari sepanjang bulan (±25mm total) — relatif kering dibanding musim panas. ⚠️ September-Oktober juga musim topan paling mungkin di area ini — tetap cek forecast H-7, bawa payung lipat untuk jaga-jaga.
- Rekomendasi bawaan: jaket tipis/cardigan untuk malam, payung lipat, sepatu jalan yang nyaman (banyak jalur taman & pedestrian street kanal berbatu), sunblock ringan untuk siang.

---

## Hari 1 — Jumat, 10 Oktober (Kedatangan Sore — Ringan)

| Jam | Kegiatan | Catatan | CNY | IDR |
|---|---|---|---|---|
| 17:00 | Tiba di Suzhou (titik kedatangan tergantung kondisi aktual), taksi/Didi ke hotel | Estimasi umum, moda transportasi masuk kota tidak dihitung terpisah | 30 | Rp79.500 |
| 17:00–17:30 | Check-in, taruh barang, istirahat | — | — | — |
| 17:30–19:00 | Makan malam santai di **Shiquan Street** (十全街 · Shíquán Jiē) | Persis di depan hotel — jalan kuliner & bar klasik Suzhou. Makan ±CNY 25/org | 50 | Rp132.500 |
| 19:00–20:00 | Jalan santai sekitar Shiquan Street / area hotel | Opsional: **Master of Nets Garden (网师园 · Wǎngshī Yuán) versi Night Garden** literally sebelah hotel kalau masih fit — CNY 100/org (±Rp265.000/org), TIDAK dihitung di total default hari ini, lihat entri Lampiran untuk detail | — | — |
| | **TOTAL HARI 1** | | **80** | **Rp212.000** |

**Plan-B hari ini:** kalau kedatangan lebih malam dari rencana — langsung istirahat penuh di hotel, makan malam di resto terdekat hotel saja (Shiquan Street tetap buka larut, banyak pilihan santai).

---

## Hari 2 — Sabtu, 11 Oktober (Kota Tua Bagian Tengah)

> **Rute:** dari hotel naik Line 5 (Nanyuanbeilu) 1 halte ke **Nanmen**, transfer **Line 4** menuju **Beisita** — kluster museum/taman/kelenteng di utara kota tua, ditutup jalan malam di Pingjiang Road.

| Jam | Kegiatan | Catatan | CNY | IDR |
|---|---|---|---|---|
| 08:00 | Sarapan di sekitar hotel | Bubur/baozi kukus, ±CNY 12/org | 24 | Rp63.600 |
| 08:30–09:00 | Metro: Nanyuanbeilu (Line 5) → Nanmen → transfer Line 4 → Beisita | ±25-30 menit termasuk transfer | 12 | Rp31.800 |
| 09:00–10:30 | **Suzhou Museum** | Gratis (reservasi online/tunjukkan paspor) | — | — |
| 10:30–11:15 | **Baoen Temple / North Pagoda (Beisi Ta)** | Jalan kaki dari museum. **Gratis** — cukup nikmati taman & pagoda dari luar, tidak perlu naik ke atas | — | — |
| 11:15–12:15 | Makan siang: Yangchun mian (mie kuah polos) | ±CNY 20/org | 40 | Rp106.000 |
| 12:15–13:30 | **Guanqian Street** & **Xuanmiao Temple** | Jalan kaki singkat dari Beisita, pedestrian street. Pelataran gratis, masuk aula utama Xuanmiao opsional ±CNY 20/org | 40 | Rp106.000 |
| 13:30–16:00 | **Humble Administrator's Garden** | Via Stasiun Zhuozhengyuan·Suzhou Museum (Line 6), searah/berdekatan dengan Beisita & Museum. Tiket ±CNY 80/org | 160 | Rp424.000 |
| 16:15–16:45 | Metro ke **Pingjiang Road** (transfer ke Line 1, Stasiun Xiangmen) | — | 12 | Rp31.800 |
| 18:00–19:30 | Makan malam + jalan malam **Pingjiang Road** | Kanal bersejarah, gratis. Makan ±CNY 25/org | 50 | Rp132.500 |
| 20:00 | Kembali ke hotel (metro, transfer di Nanmen) | — | 12 | Rp31.800 |
| | **TOTAL HARI 2** | | **350** | **Rp927.500** |

**Plan-B hari ini:** **Huqiu Wetland Park** — gratis, alternatif kalau ingin ganti salah satu spot berbayar dengan opsi gratis (searah, sekitar Beisita). Atau **Master of Nets Garden** versi siang (±CNY 40/org) kalau ingin mengganti Humble Administrator's Garden — meski secara lokasi lebih dekat hotel (lihat Hari 1), jadi lebih pas dijadikan alternatif Hari 1 malam kalau Hari 2 kepadatan.

---

## Hari 3 — Minggu, 12 Oktober (Panmen di Depan Hotel → Hanshan → Shantang)

> Akhir pekan domestik terakhir sebelum hari kerja — sedikit lebih ramai dari hari kerja biasa, tapi jauh dari level Golden Week. **Rute:** Panmen sekarang persis 1 halte dari hotel (koreksi dari draft lama yang mengasumsikan perlu perjalanan jauh) — mulai pagi di sini dulu sebelum lanjut ke kluster barat (Hanshan Temple/Shantang, via Line 5→Laodonglu→transfer Line 2).

| Jam | Kegiatan | Catatan | CNY | IDR |
|---|---|---|---|---|
| 08:00 | Sarapan | ±CNY 12/org | 24 | Rp63.600 |
| 08:15–08:30 | Metro 1 halte: Nanyuanbeilu → Nanmen | Bisa juga jalan kaki ±1,2km/17 menit kalau ingin pemanasan pagi | 8 | Rp21.200 |
| 08:45–10:00 | **Wumen Bridge** (gratis) + **Panmen Scenic Spots** | Tiket Panmen ±CNY 40/org — persis di depan hotel sekarang, tidak perlu perjalanan jauh seperti draft lama | 80 | Rp212.000 |
| 10:00–11:00 | Makan siang sekitar Panmen | ±CNY 25/org | 50 | Rp132.500 |
| 11:00–11:45 | Metro: Nanmen → Laodonglu (Line 5, 2 halte) → transfer Line 2 → Shantangjie | ±30-35 menit termasuk transfer | 20 | Rp53.000 |
| 11:45–13:45 | **Hanshan Temple** (±CNY 20/org) + **Fengqiao Scenic Area** (gratis, jalan sekitar) | Situs kuil terkenal lewat puisi kuno, bersebelahan | 40 | Rp106.000 |
| 14:00–16:00 | **Shantang Street** | "Jalan Kuno No.1 Suzhou", kanal & jembatan tua, gratis | — | — |
| 16:00–17:30 | Makan malam sekitar Shantang | ±CNY 20/org | 40 | Rp106.000 |
| 17:30 | Kembali ke hotel (Line 2 → Laodonglu → transfer Line 5 → Nanyuanbeilu) | ±30-35 menit | 20 | Rp53.000 |
| | **TOTAL HARI 3** | | **282** | **Rp747.300** |

**Plan-B hari ini:** **Xiyuan Temple (kelenteng kucing)** — ±CNY 10/org (±Rp53.000 untuk 2 orang), dekat Shantang Street, alternatif tenang kalau Hanshan Temple/Fengqiao terlalu ramai atau rute terasa memutar.

---

## Hari 4 — Senin, 13 Oktober (Jinji Lake Penuh + Music Fountain Malam)

> **Rute:** dari hotel ke kawasan Jinji Lake (Line 1, Stasiun Dongfangzhimen), lewat 2x transfer (Line 5→Nanmen/Laodonglu→Line 4/2→interchange ke Line 1). Ini hari **Opsional B (Jinji Lake versi malam) diaktifkan kembali** sebagai hari penuh, bukan lagi tambahan singkat.

| Jam | Kegiatan | Catatan | CNY | IDR |
|---|---|---|---|---|
| 08:00 | Sarapan | ±CNY 12/org | 24 | Rp63.600 |
| 08:30–09:15 | Metro ke area Jinji Lake (Dongfangzhimen, Line 1) | ±35-40 menit termasuk transfer | 20 | Rp53.000 |
| 09:15–10:15 | **The Oriental Gate / Gate of the Orient** | Gratis, lihat dari luar — landmark arsitektur ikonik Suzhou modern | — | — |
| 10:15–12:00 | **Jinji Lake Walking Tour** (versi penuh) | Gratis, jalur sangat datar. Sewa sepeda opsional ±CNY 17/jam/org, tidak dihitung | — | — |
| 12:00–13:00 | Makan siang di tepi danau | ±CNY 25/org | 50 | Rp132.500 |
| 13:00–16:00 | Santai lanjut promenade danau | Gratis | — | — |
| 17:00–18:30 | Makan malam ringan sekitar Jinji Lake | ±CNY 40/org | 80 | Rp212.000 |
| 19:00–19:30 | **Jinji Lake Music Fountain** *(kalau tayang)* | Gratis. ⚠️ Sumber terbaru sebut jadwal hanya Jumat & Sabtu 19:30 — Senin kemungkinan TIDAK tayang, cek jadwal WeChat/website resmi H-1; kalau tidak tayang, cukup nikmati promenade malam tanpa fountain | — | — |
| 20:00–20:30 | Metro kembali ke hotel | ±35-40 menit | 20 | Rp53.000 |
| | **TOTAL HARI 4** | | **194** | **Rp514.100** |

**Plan-B hari ini:** **Suzhou Centre Plaza (Mall)** — indoor, satu kawasan dengan Jinji Lake, kalau hujan deras. Kalau ingin pasti dapat pertunjukan Music Fountain dan jadwal fleksibel, pertimbangkan menukar hari ini ke malam Sabtu (Hari 2) — tapi Hari 2 sudah cukup padat dengan kota tua, jadi tetap disusun di Hari 4 sebagai default dengan catatan ketidakpastian di atas.

---

## Hari 5 — Selasa, 14 Oktober (Taihu Lake Singkat Pagi, Checkout, HSR ke Ningbo)

> **Rute & kenapa ini bisa jadi "hari ringan":** Taihu Lake sekarang bisa dicapai **LANGSUNG lewat Line 5 tanpa transfer** (stasiun ujung Nanyuanbeilu ada di jalur yang sama dengan Taihu Xiangshan) — upgrade besar dari draft lama yang perlu taksi PP penuh. Karena aksesnya jadi jauh lebih cepat & murah, versi singkat Taihu ini muat sebagai aktivitas pagi sebelum checkout, menggantikan default kepulangan generik dengan jadwal HSR riil ke Ningbo.

| Jam | Kegiatan | Catatan | CNY | IDR |
|---|---|---|---|---|
| 08:00 | Sarapan | ±CNY 12/org | 24 | Rp63.600 |
| 08:15–09:00 | Metro LANGSUNG (tanpa transfer): Nanyuanbeilu → Taihu Xiangshan (Line 5, ujung jalur) | ±40-45 menit, jarak jauh jadi tarif lebih tinggi ±CNY 13/org | 26 | Rp68.900 |
| 09:00–09:15 | Taksi/bus singkat dari stasiun ke pintu masuk **Taihu Lake Wetland Park** | Jauh lebih pendek dari taksi PP penuh versi draft lama | 20 | Rp53.000 |
| 09:15–10:45 | **Suzhou Taihu Lake Wetland Park** | Jalur datar tepi danau, cocok untuk lutut. Tiket ±CNY 60/org | 120 | Rp318.000 |
| 10:45–11:00 | Taksi/bus balik ke stasiun + metro balik ke hotel | — | 46 | Rp121.900 |
| 11:00–12:00 | Checkout hotel, siap-siap | — | — | — |
| 12:00–13:00 | Makan siang dekat hotel | ±CNY 27/org | 54 | Rp143.100 |
| 13:00–14:00 | Waktu buffer / santai | — | — | — |
| 14:00–14:30 | Taksi/Didi ke **Suzhou Railway Station** | ±27 menit, dengan koper lebih praktis daripada MRT+transfer | 40 | Rp106.000 |
| 15:00 | HSR Suzhou → Ningbo | ±2,5-3,5 jam, tiket ±CNY 147-218/org | — | *(masuk budget Ningbo)* |
| | **TOTAL HARI 5** | | **330** | **Rp874.500** |

**Plan-B hari ini:** kalau cuaca buruk atau waktu mepet — skip Taihu Lake sepenuhnya, ganti dengan **Guanqian Street** (kunjungan ulang santai, sudah dikenal dari Hari 2, searah dengan rute pagi via Line 4) sebagai pengganti yang lebih dekat & singkat. Atau kalau masih ingin nuansa alam tapi lebih dekat: **Dayangshan National Forest Park** / **Tianpingshan** (lihat Lampiran) sebagai alternatif — keduanya tetap butuh taksi terpisah, jadi kurang praktis dibanding Taihu via Line 5 langsung.

---

## Ringkasan Budget Total (2 Orang, 4 Malam / 5 Hari di Suzhou)

Belum termasuk harga hotel & tiket HSR Suzhou→Ningbo (masuk budget Ningbo, lihat "Informasi Transportasi Pulang"). Angka di bawah murni biaya aktivitas harian (tiket masuk, makan, transport lokal). Kurs: Rp2.650/CNY.

| Hari | CNY | IDR |
|---|---|---|
| Hari 1 (10 Okt) | 80 | Rp212.000 |
| Hari 2 (11 Okt) | 350 | Rp927.500 |
| Hari 3 (12 Okt) | 282 | Rp747.300 |
| Hari 4 (13 Okt) | 194 | Rp514.100 |
| Hari 5 (14 Okt) | 330 | Rp874.500 |
| **GRAND TOTAL** | **1.236** | **Rp3.275.400** |

| Kategori | CNY | IDR |
|---|---|---|
| Tiket masuk (Humble Administrator's Garden, Xuanmiao Hall, Panmen, Hanshan Temple, Taihu Lake Wetland Park) | 440 | Rp1.166.000 |
| Makan (semua hari) | 510 | Rp1.351.500 |
| Transport lokal (metro + taksi singkat) | 286 | Rp757.900 |
| **TOTAL** | **1.236** | **Rp3.275.400** |

**Catatan:** Baoen Temple/North Pagoda, Guanqian Street (pelataran), Jinji Lake, Shantang Street, Fengqiao gratis (tidak dihitung). Opsional Master of Nets Garden Night Garden (Hari 1) dan Sanqing Hall Xuanmiao Temple sudah dihitung di masing-masing baris terkait. Kalau Music Fountain (Hari 4) ternyata tidak tayang, tidak mengurangi total (memang sudah gratis, tidak ada biaya yang hilang).

---

## Catatan Penting Lainnya

- **Fisik/lutut:** hindari tempat dengan tangga curam tanpa lift — naik ke atas North Pagoda TIDAK disarankan, cukup nikmati dari taman/lantai bawah. Semua jalur di itinerary ini (kanal, taman, promenade danau) datar dan aman untuk lutut.
- **Makanan:** semua rekomendasi disesuaikan agar tidak pedas, tidak asam, tidak berminyak/gorengan — sesuai karakter masakan Suzhou yang cenderung manis-ringan.
- **Transportasi:** prioritas MRT/jalan kaki untuk jarak dekat; taksi hanya untuk bawa koper (Hari 1 & Hari 5) atau leg pendek yang di luar jangkauan MRT (dalam kawasan Taihu Lake, Hari 5).
- **Tempat berbayar** ditandai jelas — sebagian bisa diganti Plan-B yang lebih murah/gratis untuk hemat biaya.
- **Opsional A & B sudah menyatu ke itinerary utama** (Hari 5 untuk Taihu Lake versi singkat, Hari 4 untuk Jinji Lake versi malam penuh) — section "Opsional" terpisah sudah tidak ada lagi di file ini.

---

# Lampiran — Cerita & Sejarah Tempat

Supaya punya gambaran sebelum berkunjung: sedikit sejarah/cerita di balik setiap tempat yang disebut di dokumen ini — itinerary utama, Plan-B, maupun Cadangan — plus link untuk lihat foto & video referensi.

## Suzhou (苏州 · Sūzhōu) — Sebelum Berangkat

### Cerita Kota Suzhou
Suzhou didirikan tahun 514 SM oleh Raja Helü dari Kerajaan Wu sebagai ibu kota "Helü City" — jauh lebih tua dari Nanjing sebagai pusat kekuasaan di kawasan ini, dan menjadi cikal-bakal tata kota tua Suzhou yang masih terlihat sampai sekarang. Berkat jaringan kanalnya yang rumit dan taman-taman klasiknya, Suzhou dijuluki "Venice of the East" dan sering disebut bersama Hangzhou sebagai "surga di bumi" (上有天堂，下有苏州杭州).

- Foto/info: https://en.wikipedia.org/wiki/Suzhou
- Video referensi: https://www.youtube.com/results?search_query=Suzhou+China+history+canal+city

### Cuaca, Iklim & Suhu
Oktober adalah salah satu bulan terbaik berkunjung — sejuk (siang ±23°C, malam ±14-16°C), kelembapan ±71%, hujan ringan ±9-10 hari sepanjang bulan. ⚠️ September-Oktober juga musim topan paling mungkin di kawasan pesisir timur China — angka di atas rata-rata historis, BUKAN forecast real-time, cek forecast H-7 sebelum berangkat.

- Foto/info: https://en.climate-data.org/asia/china/jiangsu/suzhou-2755/

### Transportasi Masuk Kota
Suzhou tidak punya bandara besar sendiri — pelancong umumnya masuk lewat Shanghai (Hongqiao/Pudong) lalu HSR ke Suzhou. Stasiun HSR utama: **Suzhou Railway Station (苏州站 · Sūzhōu Zhàn)** di Gusu District, ±2,8km dari pusat kota — inilah yang dipakai untuk leg pulang ke Ningbo di itinerary ini. Ada juga **Suzhou North Railway Station (苏州北站 · Sūzhōu Běi Zhàn)** di Xiangcheng District, ±16km dari pusat kota — jauh lebih jauh, hanya relevan kalau transportasi datang/pergi dari stasiun itu.

- Foto/info: https://en.wikipedia.org/wiki/Suzhou_railway_station

### Area Menginap yang Disarankan
Kawasan **Gusu District sisi selatan, sekitar Shiquan Street/Nanmen** — strategis karena 1 halte MRT (Line 5) dari kluster Panmen, dan dekat jalur transfer ke Line 2/4 menuju kota tua bagian utara. Alternatif lain: sekitar Guanqian Street/Xuanmiao Temple untuk yang mengutamakan pusat kota tua yang lebih ramai & komersial.

### Destinasi Terkenal Lain di Suzhou
Di luar itinerary utama: **Tiger Hill (虎丘 · Hǔqiū)** — bukit dengan pagoda miring ("Leaning Tower of China"), salah satu ikon Suzhou paling terkenal. **Zhouzhuang** dan **Tongli** — kota air kuno di luar Suzhou, populer sebagai day-trip terpisah (lihat Cadangan). **Suzhou Industrial Park** di sekitar Jinji Lake — wajah modern kota ini, kontras dengan kota tua.

- Video referensi: https://www.youtube.com/results?search_query=top+attractions+Suzhou+China

### Makanan Wajib Dikunjungi & Dicoba
Cerita/budaya kuliner khas kota — bukan berarti otomatis masuk itinerary, karena rekomendasi makan aktual tetap mengikuti kriteria ramah lambung (tidak pedas/asam/gorengan/berminyak). **Songshu Guiyu (松鼠桂鱼 · Sōngshǔ Guìyú, "squirrel fish")** — hidangan ikon Suzhou, ikan mandarin digoreng berbentuk menyerupai tupai dengan saus asam-manis, cukup berminyak jadi perlu dibatasi. **Suzhou-style mooncake (苏式月饼 · Sū Shì Yuèbǐng)** — versi berlapis renyah, lebih ringan dari versi Kanton. **Zhagao (糖粥/赤豆糊 · Tángzhōu/Chìdòu Hú)** — bubur kacang merah manis, jajanan jalanan klasik. Masakan Suzhou umumnya masuk gaya "Jiangnan" yang cenderung manis-ringan dibanding daerah lain di China — relatif lebih ramah untuk lambung dibanding masakan pedas.

- Video referensi: https://www.youtube.com/results?search_query=Suzhou+must+try+food

### Hal yang Sebaiknya Dihindari
Hindari taksi jalanan biasa karena kendala bahasa — gunakan Didi (versi internasional) atau MRT. Jangan andalkan Google Maps/Google service tanpa VPN — gunakan Amap untuk navigasi lokal. Taman-taman klasik (Humble Administrator's Garden, dll) cukup ramai di akhir pekan — datang lebih pagi kalau bisa. September-Oktober musim topan, cek forecast rutin.

### Yang Perlu Disiapkan (Khusus China)
App WeChat Pay/Alipay (tautkan kartu asing) — banyak tempat cashless total. Terjemahan offline (unduh paket bahasa Mandarin di Google Translate). Power bank & adaptor tipe A/I. VPN aktif SEBELUM masuk China kalau butuh akses Google/WhatsApp/Instagram. Salinan paspor/visa (fisik & digital).

## Hari 1 — Jumat, 10 Oktober

### Shiquan Street (十全街 · Shíquán Jiē) ⚠️
Jalan kuliner dan hiburan malam klasik Suzhou, membentang di sisi selatan kota tua persis di depan hotel — dikenal dengan restoran, bar, dan toko kerajinan tangan yang menyatu dengan suasana kanal & arsitektur tradisional di sekitarnya. Nama hotel trip ini ("Shiquan Street·Wangshi Garden") merujuk langsung ke jalan ini.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** Langsung di depan/sangat dekat hotel — tidak perlu transportasi, cukup jalan kaki.

**Jam Operasional:** jalan buka 24 jam; mayoritas resto/toko ±10:00–22:00 (beberapa bar buka lebih malam).

**Tiket:** Gratis jalan di sepanjang jalan.

- Foto/info: https://www.google.com/search?q=Shiquan+Street+Suzhou
- Video referensi: https://www.youtube.com/results?search_query=Shiquan+Street+Suzhou

### Master of Nets Garden (网师园 · Wǎngshī Yuán) ✅ — Opsional Malam Hari 1
Salah satu taman klasik terkecil tapi paling dipuji desainnya di Suzhou, pertama dibangun era Song (abad ke-12) oleh seorang pejabat yang pensiun dan menamainya "Wangshi Yuan" (taman tukang jaring ikan) sebagai sindiran rendah hati terhadap karir birokrasinya. Terkenal dengan pertunjukan "Night Garden" di musim panas-gugur yang menampilkan opera Kunqu di antara paviliun bercahaya lampion — situs UNESCO World Heritage. Nama hotel trip ini merujuk langsung ke taman ini, dan lokasinya memang persis di area yang sama.

✅ Nama Hanzi terverifikasi langsung dari halaman ranking Amap.

**Akses:** Persis di kawasan hotel/Shiquan Street — TIDAK ada stasiun MRT persis di depan, tapi jaraknya sangat dekat jalan kaki dari hotel (searah Shiquan Street). Alternatif: halte bus "Master of Nets Garden West" (bus 529/9003/9010).

**Jam Operasional:** 21 April–20 Oktober 07:30–17:30 (loket tutup 17:00); 21 Oktober–20 April 07:30–17:00. Night Garden: pertengahan Maret–pertengahan November, setiap malam 19:30–22:00 — jadi TERSEDIA di seluruh window trip 10-14 Okt ini.

**Tiket:** Siang CNY 40/org musim ramai, CNY 30/org musim sepi (±Rp106.000/79.500 per org). Night Garden CNY 100/org (±Rp265.000/org) — terpisah dari tiket siang. Gratis untuk lansia 70+ (bawa identitas) & anak di bawah 1,2m.

**Kenapa opsional, bukan wajib:** Hari 1 sengaja dibuat ringan (kedatangan sore) — taman ini memang persis di depan hotel dan bisa dinikmati kalau masih fit setelah makan malam, tapi tidak dipaksakan masuk total budget default hari itu.

- Foto/info: https://en.wikipedia.org/wiki/Master_of_the_Nets_Garden
- Video referensi: https://www.youtube.com/results?search_query=Master+of+the+Nets+Garden+Suzhou+night

## Hari 2 — Sabtu, 11 Oktober

### Suzhou Museum (苏州博物馆 · Sūzhōu Bówùguǎn) ✅
Dirancang oleh arsitek kelahiran Suzhou I.M. Pei (juga arsitek Piramida Kaca Louvre), dibuka 2006 sebagai proyek terakhir karir panjangnya. Bangunan ini memadukan estetika taman klasik Suzhou (dinding putih, atap abu-abu, kolam batu) dengan garis geometris modern — letaknya pun sengaja bersebelahan dengan Humble Administrator's Garden supaya menyatu dengan lanskap kota tua.

✅ Nama Hanzi terverifikasi langsung dari halaman ranking Amap.

**Akses:** Stasiun Beisita (北寺塔, Line 4), keluar Exit 4, jalan kaki ±700m ke timur. Dari hotel: Nanyuanbeilu (Line 5) → Nanmen → transfer Line 4 → Beisita, ±25-30 menit. Alternatif: Stasiun Humble Administrator's Garden·Suzhou Museum (Line 6).

**Jam Operasional:** Selasa–Minggu 09:00–17:00 (masuk terakhir 16:00), tutup setiap Senin kecuali libur nasional.

**Tiket:** Gratis (sejak 18 Mei 2008); sebagian pameran khusus mungkin berbayar terpisah.

- Foto/info: https://en.wikipedia.org/wiki/Suzhou_Museum
- Video referensi: https://www.youtube.com/results?search_query=Suzhou+Museum+I.M.+Pei+tour

### Baoen Temple / North Pagoda (Beisi Ta) (北寺塔 · Běisì Tǎ) ⚠️
Pagoda tertinggi di selatan Sungai Yangtze (±76m, 9 lantai kayu bersusun), berdiri di atas lahan kuil yang riwayatnya diperkirakan mundur hingga era Tiga Kerajaan (abad ke-3). Bangunan yang ada sekarang direkonstruksi era Dinasti Song (abad ke-12). Taman di sekelilingnya rindang dan tenang, cocok untuk jalan santai tanpa harus naik ke atas pagoda.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** Stasiun Beisita (北寺塔, Line 4) — pagoda punya stasiun MRT sendiri, langsung di depan gerbang. Dari Suzhou Museum, cukup jalan kaki ±700m ke barat.

**Jam Operasional:** ±08:00–18:00 setiap hari (loket tutup 17:30). Tidak ada hari libur rutin.

**Tiket:** ⚠️ harga bervariasi antar sumber (CNY 25–40/org untuk naik ke atas pagoda, ±Rp66.250–106.000/org) — sesuai rencana itinerary ini, TIDAK naik ke atas (pertimbangan lutut), cukup nikmati taman & pagoda dari luar yang **gratis**.

- Foto/info: https://en.wikipedia.org/wiki/Bao%27en_Temple,_Suzhou
- Video referensi: https://www.youtube.com/results?search_query=North+Temple+Pagoda+Suzhou+Beisi+Ta

### Guanqian Street (观前街 · Guānqián Jiē) ⚠️
Guanqian Street ('jalan di depan kelenteng') berkembang sejak Dinasti Song sebagai pusat perdagangan di depan Xuanmiao Temple, dan sekarang jadi salah satu pedestrian street belanja & jajanan tersibuk di Suzhou.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** Stasiun Chayuanchang (察院场, Line 4), keluar Exit 2, jalan kaki ±450m ke utara — searah/lanjutan dari Beisita di rute Hari 2 ini.

**Jam Operasional:** jalan pedestrian buka 24 jam (gratis); toko & kios umumnya ±09:00–22:00.

**Tiket:** Gratis jalan di pedestrian street.

- Foto/info: https://en.wikipedia.org/wiki/Xuanmiao_Temple
- Video referensi: https://www.youtube.com/results?search_query=Guanqian+Street+Suzhou

### Xuanmiao Temple (玄妙观 · Xuánmiào Guàn) ⚠️
Salah satu kelenteng Tao tertua & terbesar di China, pertama dibangun tahun 276 M, terletak persis di tengah Guanqian Street. Aula utamanya, Sanqing Hall, adalah bangunan kayu Dinasti Song asli yang masih berdiri.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** Sama dengan Guanqian Street (lihat entri sebelumnya) — kelenteng ini persis di tengah jalan tersebut, Stasiun Chayuanchang (Line 4) Exit 2, ±450m jalan kaki.

**Jam Operasional:** Mei–September 07:30–17:00 (masuk terakhir 16:45); Oktober–April 07:30–16:30 (masuk terakhir 16:15).

**Tiket:** Pelataran luar gratis; masuk aula utama (Sanqing Hall) CNY 20/org (±Rp53.000/org).

- Foto/info: https://en.wikipedia.org/wiki/Xuanmiao_Temple
- Video referensi: https://www.youtube.com/results?search_query=Xuanmiao+Temple+Suzhou

### Humble Administrator's Garden (拙政园 · Zhuōzhèng Yuán) ✅
Taman klasik terbesar di Suzhou (±5.2 hektar) dan situs UNESCO World Heritage, dibangun tahun 1509 oleh pejabat Dinasti Ming, Wang Xianchen, setelah pensiun kecewa dari birokrasi — namanya diambil dari puisi era Jin yang menyindir "mengurus kebun adalah politik orang bodoh". Desainnya berpusat pada kolam-kolam besar dengan paviliun, jembatan, dan koridor.

✅ Nama Hanzi terverifikasi langsung dari halaman ranking Amap.

**Akses:** Stasiun Zhuozhengyuan·Suzhou Museum (拙政园·苏州博物馆, Line 6), keluar Exit 1, jalan kaki ±450m — satu kompleks dengan Suzhou Museum & Beisi Ta, searah rute Hari 2 ini.

**Jam Operasional:** 1 Maret–15 November 07:30–17:30; 16 November–akhir Februari 07:30–17:00.

**Tiket:** Musim ramai (April–Mei, Juli–Oktober) CNY 80/org (±Rp212.000/org) — cocok dengan yang dipakai di itinerary ini; musim sepi CNY 70/org (±Rp185.500/org). Pelajar/lansia setengah harga.

- Foto/info: https://en.wikipedia.org/wiki/Humble_Administrator%27s_Garden
- Video referensi: https://www.youtube.com/results?search_query=Humble+Administrator%27s+Garden+Suzhou

### Pingjiang Road (平江路 · Píngjiāng Lù) ✅
Jalan kanal yang tata letaknya nyaris tidak berubah sejak peta kota era Dinasti Song (1229) — salah satu bukti tata kota kuno yang paling terjaga di China. Menyusuri kanal sepanjang ±1.6km dengan jembatan batu, rumah putih-abu tradisional, dan teahouse kecil.

✅ Nama Hanzi terverifikasi langsung dari halaman ranking Amap.

**Akses:** Stasiun Xiangmen (相门, Line 1), keluar Exit 3, jalan kaki ±350m. Dari kluster Beisita/Guanqian, transfer ke Line 1 dulu.

**Jam Operasional:** jalan kanal buka 24 jam (gratis); mayoritas toko/teahouse tutup ±22:00.

**Tiket:** Gratis.

- Foto/info: https://en.wikipedia.org/wiki/Pingjiang_Road
- Video referensi: https://www.youtube.com/results?search_query=Pingjiang+Road+Suzhou+night

### Huqiu Wetland Park (虎丘湿地公园 · Hǔqiū Shīdì Gōngyuán) ⚠️ — Plan-B Hari 2
Taman lahan basah di sekitar kawasan Tiger Hill (Huqiu), dikembangkan sebagai ruang hijau publik gratis dengan jalur air & vegetasi alami, luas ±12 km² — kontras dengan taman klasik berbayar di sekitarnya. Rumah bagi 200+ spesies burung.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** Stasiun Sunwu Memorial Museum (孙武纪念苑, Line 4), keluar Exit 2, jalan kaki ±15 menit — searah kluster Line 4 Hari 2 ini.

**Jam Operasional:** ±06:00–20:00 setiap hari.

**Tiket:** Gratis (beberapa aktivitas tambahan di dalam mungkin berbayar).

**Kenapa jadi Plan-B:** gratis, alternatif praktis kalau ingin mengurangi satu spot berbayar hari itu.

- Foto/info: https://www.google.com/search?q=Huqiu+Wetland+Park+Suzhou
- Video referensi: https://www.youtube.com/results?search_query=Huqiu+Wetland+Park+Suzhou

## Hari 3 — Minggu, 12 Oktober

### Wumen Bridge (吴门桥 · Wúmén Qiáo) ⚠️
Jembatan batu tertinggi di Suzhou (dibangun awal abad ke-11), berdiri di dekat Panmen Gate — salah satu peninggalan arsitektur kanal kuno Suzhou yang menghubungkan area gerbang kota dengan permukiman sekitarnya, bebas dikunjungi sebagai bagian dari jalan santai kawasan Panmen.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** Satu kawasan dengan Panmen Scenic Spots (lihat entri berikutnya) — persis 1 halte MRT dari hotel via Nanmen (Line 5).

**Jam Operasional:** area jembatan bisa dilihat/dilewati kapan saja sebagai bagian jalan umum; untuk masuk ke sisi dalam kompleks Panmen ikuti jam operasional Panmen.

**Tiket:** Gratis (melihat/menyeberangi jembatan dari luar kompleks berbayar Panmen).

- Foto/info: https://www.google.com/search?q=Wumen+Bridge+Suzhou
- Video referensi: https://www.youtube.com/results?search_query=Wumen+Bridge+Suzhou

### Panmen Scenic Spots (盘门景区 · Pánmén Jǐngqū) ⚠️
Satu-satunya gerbang kota kuno di China yang menggabungkan gerbang air DAN gerbang darat dalam satu struktur — mencerminkan kota Suzhou yang sejak awal dibangun mengelilingi jaringan kanal. Sejarahnya bermula era Kerajaan Wu (abad ke-6 SM), dengan struktur yang berdiri sekarang direkonstruksi era Dinasti Yuan-Ming. Kompleksnya juga mencakup Ruiguang Pagoda dan Wumen Bridge.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** Stasiun Nanmen (南门, Line 4 & Line 5) — persis **1 halte MRT dari hotel via Line 5** (koreksi dari draft lama yang mengasumsikan perjalanan lebih jauh), atau jalan kaki ±1,2km/17 menit.

**Jam Operasional:** 07:30–17:30 setiap hari.

**Tiket:** CNY 40/org (±Rp106.000/org) — cocok dengan yang dipakai di itinerary ini; beli online lebih murah beberapa yuan.

- Foto/info: https://en.wikipedia.org/wiki/Suzhou_city_wall
- Video referensi: https://www.youtube.com/results?search_query=Panmen+Gate+Suzhou

### Hanshan Temple (寒山寺 · Hánshān Sì) ✅
Kuil Buddha yang jadi terkenal berkat puisi Dinasti Tang "Malam Berlabuh di Maple Bridge" (枫桥夜泊 · Fēngqiáo Yèbó) karya Zhang Ji, yang menggambarkan suara lonceng kuil ini terdengar hingga ke perahu di kanal — puisi itu sendiri jadi salah satu karya sastra China paling dikenal. Kuil aslinya dibangun era Dinasti Liang (abad ke-6), sudah beberapa kali hancur & dibangun ulang, terakhir era Qing.

✅ Nama Hanzi terverifikasi langsung dari halaman ranking Amap.

**Akses:** Stasiun Shantangjie (山塘街, Line 2), keluar Exit 3, jalan kaki ±15 menit. Dari hotel: Nanyuanbeilu (Line 5) → Laodonglu (3 halte) → transfer Line 2 → Shantangjie.

**Jam Operasional:** 07:30–17:30 (masuk terakhir 16:30); tanggal 1 & 15 penanggalan lunar buka lebih awal jam 07:00.

**Tiket:** Musim ramai (April–Oktober) CNY 20/org dewasa, CNY 10/org pelajar/lansia (±Rp53.000/26.500); musim sepi (November–Maret) CNY 15/CNY 8/org (±Rp39.750/21.200).

- Foto/info: https://en.wikipedia.org/wiki/Hanshan_Temple
- Video referensi: https://www.youtube.com/results?search_query=Hanshan+Temple+Suzhou

### Fengqiao Scenic Area (枫桥景区 · Fēngqiáo Jǐngqū) ⚠️
Kawasan Maple Bridge (Fengqiao) yang jadi latar puisi terkenal Zhang Ji di atas — bersebelahan langsung dengan Hanshan Temple. Area sekitar jembatan & kanal bisa dinikmati gratis sambil membayangkan suasana yang diabadikan dalam puisi 1.200 tahun lalu. ⚠️ Catatan: meski sering dikira satu tempat dengan Hanshan Temple, keduanya scenic spot terpisah dengan tiket masing-masing.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** Persis bersebelahan dengan Hanshan Temple (lihat entri sebelumnya) — akses & rute sama.

**Jam Operasional:** Maret–Oktober 06:00–21:30; November–Februari 06:30–21:00.

**Tiket:** Gratis.

- Foto/info: https://en.wikipedia.org/wiki/Maple_Bridge
- Video referensi: https://www.youtube.com/results?search_query=Fengqiao+Scenic+Area+Suzhou

### Shantang Street (七里山塘 · Qīlǐ Shāntáng) ✅
Dijuluki "Jalan Kuno No.1 Suzhou", dibangun tahun 825 M atas perintah penyair sekaligus gubernur Bai Juyi untuk menghubungkan kota dengan Tiger Hill sepanjang ±7 li (±3.6km). Sepanjang kanal berjejer rumah tradisional, jembatan batu era Ming-Qing, dan toko-toko kecil.

✅ Nama Hanzi terverifikasi langsung dari halaman ranking Amap — nama resmi di ranking Amap adalah "七里山塘景区" (Qīlǐ Shāntáng Jǐngqū, Qili Shantang Scenic Area), umum disebut pendek "山塘街" (Shāntáng Jiē, Shantang Street).

**Akses:** Stasiun Shantang Street (山塘街, Line 2), keluar Exit 3 — langsung di depan jalan, satu jalur dengan Hanshan Temple.

**Jam Operasional:** jalan buka 24 jam (gratis); toko/atraksi umumnya ±09:00–22:00; boating 08:00–17:00 & 18:00–20:00.

**Tiket:** Gratis jalan di sepanjang jalan; boat tour opsional CNY 55/org (Xinmin Wharf) atau CNY 100/org (versi malam "Oriental Venice").

- Foto/info: https://en.wikipedia.org/wiki/Shantang_Street
- Video referensi: https://www.youtube.com/results?search_query=Shantang+Street+Suzhou

### Xiyuan Temple (西园寺 · Xīyuán Sì, kelenteng kucing) ✅ — Plan-B Hari 3
Awalnya bagian dari taman pribadi keluarga bangsawan era Ming, diubah jadi kelenteng Buddha tahun 1635. Terkenal dengan kolam kura-kura besar dan Aula 500 Arhat berisi ratusan patung Buddha berlapis emas.

✅ Nama Hanzi terverifikasi langsung dari halaman ranking Amap.

**Akses:** TIDAK ada stasiun MRT persis di depan — naik bus 6/10/11/17/40/Y1/Y3 turun halte Xiyuan (西园站), searah kawasan Shantang Street.

**Jam Operasional:** 07:30–17:30 setiap hari (loket tutup 17:00).

**Tiket:** CNY 5/org (±Rp13.250/org).

**Kenapa jadi Plan-B:** dekat Shantang Street, jalur datar, suasana tenang — alternatif kalau Hanshan Temple/Fengqiao terasa memutar dari rute utama.

- Foto/info: https://en.wikipedia.org/wiki/Xiyuan_Temple
- Video referensi: https://www.youtube.com/results?search_query=Xiyuan+Temple+Suzhou+turtle+pond

## Hari 4 — Senin, 13 Oktober

### The Oriental Gate / Gate of the Orient (东方之门 · Dōngfāng Zhī Mén) ⚠️
Gedung pencakar langit berbentuk gerbang raksasa (dijuluki warga lokal "celana panjang" karena bentuknya) yang jadi landmark arsitektur kontroversial-tapi-ikonik Suzhou modern, selesai dibangun 2015 di tepi Jinji Lake sebagai simbol gerbang masuk ke distrik bisnis baru.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** Stasiun Dongfangzhimen (东方之门, Line 1) — gedung ini punya stasiun MRT sendiri, tersambung langsung. Sisi barat Jinji Lake. Dari hotel: Line 5 → Nanmen/Laodonglu → transfer ke Line 1 (±35-40 menit total).

**Jam Operasional:** area luar/lihat dari luar bisa kapan saja; bangunan sendiri fungsinya hotel/kantor/residensial (bukan objek wisata dengan jam buka publik).

**Tiket:** Gratis, lihat dari luar saja.

- Foto/info: https://en.wikipedia.org/wiki/Gate_of_the_Orient
- Video referensi: https://www.youtube.com/results?search_query=Gate+of+the+Orient+Suzhou

### Jinji Lake (金鸡湖 · Jīnjī Hú) ⚠️
Danau alami seluas ±8.9 km² yang jadi jantung Suzhou Industrial Park — kawasan kota baru modern hasil kerja sama China-Singapura sejak 1994. Promenadenya menampilkan taman modern, gedung pencakar langit, dan jembatan-jembatan kontemporer, representasi wajah Suzhou masa kini. Lakeside Avenue di sisi barat sepanjang ±2km jadi jalur jalan kaki utama.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** Stasiun Dongfangzhimen (Line 1, sisi barat/West Gate) atau Stasiun Cultural Expo Center (sisi timur).

**Jam Operasional:** promenade & tepi danau buka 24 jam.

**Tiket:** Gratis masuk & jalan di tepi danau; wahana berbayar (Ferris wheel, cruise) terpisah dan tidak dihitung di itinerary ini.

- Foto/info: https://en.wikipedia.org/wiki/Jinji_Lake
- Video referensi: https://www.youtube.com/results?search_query=Jinji+Lake+Suzhou+promenade

### Jinji Lake Music Fountain (金鸡湖音乐喷泉 · Jīnjī Hú Yīnyuè Pēnquán) ⚠️
Salah satu air mancur musikal terbesar di Asia saat diresmikan, dengan pertunjukan cahaya & air yang disinkronkan musik setiap malam — jadi daya tarik gratis paling populer di kawasan Jinji Lake untuk warga lokal maupun turis.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** Stasiun Dongfangzhimen (Line 1) — lokasi di persimpangan Suyalu Road & Xingyang Street, kawasan Lakeside New World, dekat Gate of the Orient.

**Jam Operasional:** ⚠️ jadwal bervariasi musiman & sumbernya sedikit tidak konsisten — per sumber terbaru: Jumat & Sabtu 19:30 (durasi ±30 menit), tambahan sesi saat libur nasional. Hari 4 itinerary ini jatuh di hari **Senin**, kemungkinan besar TIDAK ada pertunjukan — dianggap bonus kalau ternyata tayang, bukan jaminan. Pertunjukan dibatalkan saat cuaca buruk. **Cek jadwal WeChat/website resmi Jinji Lake Scenic Area H-1** sebelum berangkat ke lokasi.

**Tiket:** Gratis.

- Foto/info: https://www.google.com/search?q=Jinji+Lake+Music+Fountain
- Video referensi: https://www.youtube.com/results?search_query=Jinji+Lake+Music+Fountain+Suzhou

### Suzhou Centre Plaza / Suzhou Center (苏州中心 · Sūzhōu Zhōngxīn) ⚠️ — Plan-B Hari 4
Mal besar di tepi Jinji Lake dengan atap gelombang khas ("cloud roof") yang jadi salah satu ikon arsitektur baru Suzhou, plus taman atap (rooftop garden) dengan pemandangan langsung ke Gate of the Orient.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** Stasiun Dongfangzhimen (Line 1), keluar Exit 3 — tersambung langsung ke mal, tidak perlu keluar ke jalan.

**Jam Operasional:** 10:00–22:00 setiap hari.

**Tiket:** Gratis masuk (mal), bukan sesi belanja di itinerary ini.

**Kenapa jadi Plan-B:** TIDAK termasuk destinasi wisata utama (prinsip itinerary ini menghindari sesi belanja), tapi lokasinya di tepi Jinji Lake — pilihan praktis untuk berteduh kalau hujan deras.

- Foto/info: https://en.wikipedia.org/wiki/Suzhou_Center
- Video referensi: https://www.youtube.com/results?search_query=Suzhou+Center+Mall+Jinji+Lake

## Hari 5 — Selasa, 14 Oktober

### Suzhou Taihu Lake Wetland Park (苏州太湖湿地公园 · Sūzhōu Tàihú Shīdì Gōngyuán) ⚠️
Taman lahan basah di tepi Danau Taihu — danau terbesar ketiga di China, terkenal dengan batu-batu taihu (batu kapur berlubang khas) yang dulu banyak diambil untuk menghias taman klasik Suzhou. Jalur promenadenya datar dan luas, kontras menyegarkan dari padatnya kota tua.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap. ⚠️ Catatan tambahan: ada KEMUNGKINAN dua entitas berbeda dengan nama mirip di kawasan ini — "Suzhou Taihu Lake Wetland Park" (berbayar) vs "Taihu Hubin National Wetland Park"/wetland tepi danau lain (gratis) — cek nama persis di Amap/Trip.com sebelum berangkat supaya tidak salah lokasi.

**Akses:** **Stasiun Taihu Xiangshan (太湖香山, Line 5) — LANGSUNG dari hotel TANPA transfer** (koreksi besar dari draft lama yang mengasumsikan taksi PP penuh), ±40-45 menit naik metro. Dari stasiun, taksi/bus singkat ±10-15 menit ke pintu masuk taman — kawasan resor Taihu ini luas, jadi tetap perlu leg pendek terakhir yang bukan jalan kaki.

**Jam Operasional:** 08:30–17:00 (masuk terakhir 16:00).

**Tiket:** ⚠️ harga bervariasi antar sumber — CNY 60/org (±Rp159.000/org, dipakai di itinerary ini) hingga versi gratis/CNY 20/org tergantung sumber & mungkin tergantung area spesifik yang dimaksud. Cek harga pasti di loket/Trip.com sebelum berangkat.

- Foto/info: https://en.wikipedia.org/wiki/Lake_Tai
- Video referensi: https://www.youtube.com/results?search_query=Suzhou+Taihu+Lake+Wetland+Park

### Shoutao Lake Scenic Area (寿桃湖 · Shòutáo Hú) ⚠️
Danau kecil (±400 mu/26.7 hektar, kedalaman maksimum 70m) hasil genangan air tanah alami sejak penambangan batu dilarang tahun 1999 di kawasan Wuzhong. Batu-batu di tengah danau menyerupai buah persik umur panjang (asal namanya), juga dijuluki "Guilin Mini"-nya Suzhou. Jadi spot foto yang relatif belum ramai turis.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** Satu kawasan resor dengan Taihu Xiangshan (Line 5) — taksi/Didi singkat dari stasiun, lokasi di kawasan Wuzhong dekat persimpangan Lingtian Road & Zhangjingbang Road. **Hanya realistis dikunjungi kalau ada waktu ekstra** — versi singkat Hari 5 di itinerary ini fokus ke Taihu Lake Wetland Park saja karena keterbatasan jam sebelum checkout.

**Jam Operasional:** buka sepanjang tahun, tidak ada jam tutup khusus (area publik terbuka).

**Tiket:** Gratis.

- Foto/info: https://www.google.com/search?q=Shoutao+Lake+Suzhou
- Video referensi: https://www.youtube.com/results?search_query=Shoutao+Lake+Suzhou

### Suzhou Wuzhong Taihu Tourist Zone (吴中太湖旅游度假区 · Wúzhōng Tàihú Lǚyóu Dùjiàqū) ⚠️
Kawasan wisata resmi 5A di tepi Danau Taihu, distrik Wuzhong, seluas ±250 km², mencakup beberapa taman & area publik di sepanjang tepi danau (termasuk Taihu Park, Situ Temple, Lushan) — cocok untuk memperpanjang waktu santai setelah mengunjungi Taihu Lake Wetland Park, kalau jadwal tidak semepet versi Hari 5 di itinerary ini.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap. ⚠️ Kawasan ini luas dan mencakup beberapa sub-area dengan aturan tiket berbeda-beda (sebagian gratis, sebagian berbayar) — bagian yang dimaksud di itinerary ini adalah area publik/promenade gratis di tepinya, BUKAN atraksi berbayar spesifik di dalamnya.

**Akses:** Satu kawasan resor dengan Taihu Xiangshan (Line 5) — taksi/Didi singkat dari stasiun.

**Jam Operasional:** area publik buka sepanjang hari; sub-atraksi berbayar (mis. Taihu Park, CNY 10/org) punya jam & hari tutup sendiri (tutup Rabu April–Oktober, Selasa-Rabu November–Maret, kecuali libur nasional).

**Tiket:** Gratis untuk area publik/promenade tepi danau.

- Foto/info: https://www.google.com/search?q=Wuzhong+Taihu+Tourist+Zone
- Video referensi: https://www.youtube.com/results?search_query=Wuzhong+Taihu+Tourist+Zone

### Dayangshan National Forest Park (大阳山国家森林公园 · Dàyángshān Guójiā Sēnlín Gōngyuán) ⚠️ — Plan-B Hari 5
Taman hutan nasional di pinggiran barat kota tua Suzhou, terbagi 2 area utama: Wenshu Monastery (dibangun era Dinasti Jin Timur) dan Botanical Garden dengan koleksi tanaman langka (yew, huanghuali, podocarpus). Jalur trekking ringan & udara segar, alternatif nature-day selain Taihu Lake.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** TIDAK ada MRT langsung — taksi/Didi dari kota, arahnya berbeda dari Taihu Xiangshan (bukan di jalur Line 5 yang sama).

**Jam Operasional:** 09:00–16:30.

**Tiket:** ⚠️ belum ditemukan sumber resmi harga tiket — cek Amap/Trip.com langsung sebelum berangkat.

**Kenapa jadi Plan-B:** redundant dengan Taihu Lake Wetland Park sebagai pilihan "alam" hari itu, dan aksesnya kurang praktis dibanding Taihu Xiangshan yang langsung 1 jalur MRT dari hotel — dipilih salah satu saja.

- Foto/info: https://www.google.com/search?q=Dayangshan+National+Forest+Park+Suzhou
- Video referensi: https://www.youtube.com/results?search_query=Dayangshan+National+Forest+Park+Suzhou

### Tianpingshan Scenic Spot (天平山 · Tiānpíng Shān) ⚠️ — Plan-B Hari 5
Gunung kecil terkenal dengan pohon maple (paling indah saat musim gugur, sekitar akhir Oktober-awal Desember) dan mata air alami yang sudah jadi tempat rekreasi sejak Dinasti Song.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** MRT Line 1 ke Stasiun Mudu (木渎), transfer bus rute 4, turun halte Tianpingshan (天平山站), ±3.5km dari stasiun Mudu — perlu transfer Line 1 dari hotel, arahnya berbeda dari rute Taihu Xiangshan.

**Jam Operasional:** 08:00–17:00 (loket & masuk terakhir 16:30).

**Tiket:** CNY 30/org dewasa, CNY 15/org lansia/anak (±Rp79.500/39.750 per org).

**Kenapa jadi Plan-B (bukan utama):** area ini punya jalur hiking gunung yang cukup menanjak — untuk kondisi lutut, lebih aman hanya dicoba di area bawah/foothill saja, bukan pendakian penuh. Juga di luar musim daun maple terbaik (trip ini 10-14 Okt, puncak maple baru akhir Oktober).

- Foto/info: https://en.wikipedia.org/wiki/Tianping_Mountain
- Video referensi: https://www.youtube.com/results?search_query=Tianpingshan+Suzhou

## Cadangan

Tempat-tempat ini layak dikunjungi, tapi sengaja TIDAK dimasukkan ke itinerary maupun Plan-B — alasannya ditulis di masing-masing uraian.

### Suzhou Bay Huangjin Lake Shore ⚠️
Kawasan tepi danau di distrik Suzhou Bay (Wuzhong), pengembangan kota baru dengan taman tepi air modern.

⚠️ Nama Hanzi TIDAK ditemukan dari sumber yang bisa diverifikasi sesi ini (termasuk percobaan Amap) — kemungkinan nama Inggris di catatan Anda adalah terjemahan longgar dari sebuah pengembangan properti/taman baru yang belum banyak terindeks di sumber berbahasa Inggris. Cek Amap langsung dengan nama Inggris di atas atau tanya penduduk lokal/hotel sebelum berkunjung.

**Akses:** ⚠️ belum ditemukan sumber resmi — kemungkinan perlu taksi/Didi karena "Jauh" sesuai catatan pribadi Anda. Cek Amap langsung sebelum berangkat.

**Jam Operasional:** ⚠️ belum ditemukan sumber resmi — kemungkinan area terbuka publik (buka sepanjang hari), tapi belum terverifikasi.

**Tiket:** ⚠️ belum ditemukan sumber resmi — kemungkinan gratis (taman tepi air publik), tapi belum terverifikasi.

**Kenapa tidak dimasukkan:** ditandai "Jauh" di catatan pribadi Anda — lokasinya di luar rute efisien hari-hari yang sudah disusun.

- Foto/info: https://www.google.com/search?q=Suzhou+Bay+Huangjin+Lake+Shore
- Video referensi: https://www.youtube.com/results?search_query=Suzhou+Bay+Huangjin+Lake+Shore

### Suzhou Culture & Arts Centre (苏州文化艺术中心 · Sūzhōu Wénhuà Yìshù Zhōngxīn) ⚠️
Pusat seni & budaya modern Suzhou rancangan arsitek Prancis Paul Andreu, dibuka 2007, seluas ±150.000 m² di tepi timur Jinji Lake — berisi grand theater, concert hall, bioskop IMAX, sekolah seni, dan Suzhou Jinji Lake Art Museum di dalamnya.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** Stasiun Cultural Expo Center (文化博览中心, Line 1), keluar Exit 1 — tersambung langsung, searah kawasan Jinji Lake (Hari 4).

**Jam Operasional:** area pameran umumnya 10:00–20:00, tutup setiap Senin.

**Tiket:** Gratis masuk gedung; harga tiket pertunjukan/pameran tertentu bervariasi per acara ⚠️.

**Kenapa tidak dimasukkan:** kontennya (galeri/teater indoor) kurang sesuai gaya jalan-jalan outdoor santai yang diprioritaskan trip ini — meski searah rute Hari 4, sengaja tidak ditambahkan supaya hari itu tidak terlalu padat.

**Terkait:** Hari 4

- Foto/info: https://www.google.com/search?q=Suzhou+Culture+%26+Arts+Centre
- Video referensi: https://www.youtube.com/results?search_query=Suzhou+Culture+and+Arts+Centre

### Dongshahu Ecology Park (东沙湖生态园 · Dōngshāhú Shēngtài Yuán) ⚠️
Taman ekologi terbuka terbesar di kawasan ini (±1,21 juta m², termasuk ±540.000 m² area air), tanpa pagar/tembok dengan banyak pintu masuk. Punya sistem 3 pulau (Cherry Blossom Island, Crabapple Island, Reed Island) memadukan bukit & air.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap. ⚠️ Catatan: nama Inggris yang muncul di beberapa sumber sedikit berbeda-beda ("Dongshahu Ecological Park" vs "Shahu Ecological Park") — kemungkinan penamaan/terjemahan tidak konsisten antar platform, bukan berarti dua tempat berbeda, tapi tetap cek nama persis di Amap sebelum berangkat.

**Akses:** Stasiun Dongshahu (东沙湖, Line 1) — taman ini punya stasiun MRT sendiri, searah kawasan Jinji Lake (Hari 4).

**Jam Operasional:** ⚠️ belum ditemukan sumber jam buka-tutup pasti — sebagai taman terbuka tanpa pagar, kemungkinan bisa diakses kapan saja.

**Tiket:** Gratis.

**Kenapa tidak dimasukkan:** redundant dengan Jinji Lake & Taihu Lake Wetland Park sebagai pilihan "taman/danau" trip ini — dipilih yang lebih ikonik.

**Terkait:** Hari 4

- Foto/info: https://www.google.com/search?q=Dongshahu+Ecology+Park+Suzhou
- Video referensi: https://www.youtube.com/results?search_query=Dongshahu+Ecology+Park+Suzhou

### Zhouzhuang Water Town (周庄 · Zhōuzhuāng) ⚠️
Desa air kuno berusia hampir 1.000 tahun (era Dinasti Song), sering disebut "Kota Air No.1 China" — rumah-rumah tepi kanal termasuk Shen House & Zhang House yang jadi ikon utama, jembatan-jembatan batu era Ming-Qing. Kota air paling populer/komersial dibanding Tongli (lihat entri berikutnya).

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** ±30km/45-50 menit dari Suzhou — bus dari Suzhou North Bus Station (berangkat tiap 20-30 menit, ±CNY 17/org), atau taksi/Didi.

**Jam Operasional:** kawasan buka sepanjang hari; tiket terusan berlaku ke 10+ spot di dalamnya, jam masing-masing spot umumnya 08:00–16:30 (Shen's House & Zhang's House sampai 20:00).

**Tiket:** CNY 100/org (weekday) — ⚠️ beberapa sumber menyebut CNY 50 weekday/CNY 100 weekend-libur, cek harga pasti sebelum berangkat (±Rp132.500–265.000/org). Masuk gratis setelah 17:00 dengan registrasi nama, tapi sebagian atraksi sudah tutup.

**Kenapa tidak dimasukkan:** berjarak ±45-50 menit di luar kota Suzhou, butuh setengah hari penuh + transport khusus yang tidak sesuai prinsip santai tanpa buru-buru trip ini. Cocok jadi trip terpisah di kesempatan lain.

- Foto/info: https://en.wikipedia.org/wiki/Zhouzhuang
- Video referensi: https://www.youtube.com/results?search_query=Zhouzhuang+Water+Town

### Tongli Water Town (同里 · Tónglǐ) ⚠️
Kota air dengan kanal & jalan lebih sempit dibanding Zhouzhuang, kesan lebih tenang & otentik (lebih banyak penduduk lokal tinggal di sana), terkenal dengan taman klasik Retreat & Reflection Garden (退思园 · Tuìsī Yuán).

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** ±30-45 menit dari Suzhou — bus dari Suzhou (operasi 07:15–17:15, ±CNY 8/org), atau taksi/Didi.

**Jam Operasional:** atraksi utama 07:30–17:30; Tuisi Garden (退思园 · Tuìsī Yuán) tambahan sesi malam 18:45–20:30. Jalan/kanal bisa diakses gratis sebelum 08:00 & setelah 17:15 (atraksi sudah tutup di jam tersebut).

**Tiket:** CNY 100/org, berlaku 2 hari untuk 10 spot di dalamnya (±Rp265.000/org); tambahan CNY 50/org untuk night tour taman (±Rp132.500/org).

**Kenapa tidak dimasukkan:** sama seperti Zhouzhuang — berjarak ±30-45 menit di luar kota Suzhou, butuh setengah hari penuh + transport khusus yang tidak sesuai prinsip santai tanpa buru-buru trip ini. Cocok jadi trip terpisah atau dipilih SALAH SATU (bukan dua-duanya) dengan Zhouzhuang kalau suatu saat diaktifkan.

- Foto/info: https://en.wikipedia.org/wiki/Tongli
- Video referensi: https://www.youtube.com/results?search_query=Tongli+Water+Town

### Suzhou Amusement Land (苏州乐园 · Sūzhōu Lèyuán) ⚠️
Taman hiburan skala besar dengan 3 zona utama (Water World, Forest World, Children's World), wahana modern termasuk roller coaster gantung terbesar di China, serta beberapa instalasi bertema landmark dunia (mis. replika Coliseum Romawi, tanda mirip "HOLLYWOOD").

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap. **⚠️ Koreksi dari draft sebelumnya:** nama "Window of the World" yang sebelumnya disandingkan dengan tempat ini sebenarnya taman berbeda yang berlokasi di **Shenzhen**, BUKAN bagian dari Suzhou Amusement Land — kemungkinan tercampur karena konsep temanya mirip (replika landmark dunia). Entri ini murni tentang Suzhou Amusement Land (苏州乐园 · Sūzhōu Lèyuán).

**Akses:** Stasiun Suzhou Amusement Park (苏州乐园, Line 1), jalan kaki ±5 menit.

**Jam Operasional:** ⚠️ bervariasi per zona/musim, cek jadwal spesifik hari kunjungan di Trip.com/website resmi sebelum berangkat.

**Tiket:** CNY 200–260/org dewasa, CNY 150–180/org anak/lansia (±Rp530.000–689.000 / Rp397.500–477.000 per org) tergantung zona & musim; paket combo dewasa+anak mulai CNY 198.

**Kenapa tidak dimasukkan:** berbayar mahal dan berorientasi turis/hiburan, tidak sejalan dengan prinsip trip ini yang mengutamakan tempat gratis/merakyat dan suasana lokal otentik.

- Foto/info: https://en.wikipedia.org/wiki/Suzhou_Amusement_Land
- Video referensi: https://www.youtube.com/results?search_query=Suzhou+Amusement+Land

---

*Draft ini masih dalam format .md untuk review. PDF hanya di-generate kalau diminta eksplisit, sesuai skill PDF.*
