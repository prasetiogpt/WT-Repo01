# Itinerary Perjalanan Suzhou
10 – 14 Oktober · 4 Malam · Direncanakan Independen (bukan sambungan kota lain)

> **Master file** — edit di sini dulu untuk revisi cepat. PDF (`Suzhou Itinerary.pdf`) di-generate ulang dari file ini hanya saat diminta.
>
> ⚠️ Riwayat revisi: (1) **Sinkronisasi format ke standar Nanjing/Wuxi** — kolom Kegiatan di semua tabel itinerary (Hari 1-4, Opsional A/B) sekarang bold selektif, hanya nama destinasi wisata yang di-`**bold**` (baris transit/logistik/makan polos dibiarkan tanpa bold); (2) seluruh 30 entri Lampiran (termasuk Cadangan & Plan-B) dilengkapi Hanzi + badge verifikasi, `**Akses:**` (jalur MRT/exit/jarak jalan kaki), `**Jam Operasional:**`, dan `**Tiket:**` (CNY+IDR, kurs tetap Rp2.650/CNY) — diriset via web search, ditandai ⚠️ kalau tidak ditemukan sumber resmi/pasti, bukan tebakan; (3) "Guanqian Street & Xuanmiao Temple" dan "Zhouzhuang / Tongli Water Town" dipecah masing-masing jadi 2 entri terpisah (satu `###` = satu tempat, sesuai aturan parser); (4) dikoreksi kerancuan penamaan di entri "Suzhou Amusement Land / Window of the World" — "Window of the World" sebenarnya taman berbeda di Shenzhen, bukan bagian dari Suzhou Amusement Land (苏州乐园); entri diganti jadi murni Suzhou Amusement Land dengan catatan koreksi; (5) diperbaiki bug parser `generate_wisata.py` — heading Lampiran "## Opsional A" dan "## Opsional B" sebelumnya tidak dikenali parser (entrinya diam-diam ter-skip dari Wisata.html); ditambahkan pengenalan generik untuk heading `## Opsional <label>` di parser; (6) **Revisi besar 2026-08-19** — tanggal digeser jadi **10–14 Oktober (4 malam, 5 hari)** sesuai jadwal baru; **hotel dikoreksi** ke Suzhou City Holiday Hotel (Shiquan Street·Wangshi Garden), Gusu District, dengan anchor MRT **Nanyuanbeilu (Line 5)** — SELURUH rute harian & moda transportasi disusun ulang dari titik ini (bukan lagi asumsi hotel lama); **city independence diterapkan** — Hari 1 & Hari 5 tidak lagi menyambung jadwal transportasi aktual kota sebelumnya (`[[itinerary-continuity]]` sudah SUPERSEDED), dipakai default kedatangan 17:00/kepulangan pola skill terbaru, dengan pengecualian Hari 5 yang pakai data riil jadwal HSR Suzhou→Ningbo; **Opsional A (Taihu Lake) & Opsional B (Jinji Lake malam/Music Fountain) diaktifkan kembali ke badan itinerary utama** (Hari 5 & Hari 4) karena durasi Suzhou diperpanjang jadi 5 hari — section "## Opsional" dihapus, entri Lampiran-nya dipindah ke grup Hari terkait; **rute Panmen & Wumen Bridge disederhanakan** karena sekarang persis 1 halte MRT dari hotel (dulu perlu perjalanan lebih jauh); **leg pulang dikoreksi** dari asumsi lama ke **HSR Suzhou → Ningbo** via Suzhou Railway Station (bukan Guangzhou — itu leg trip terpisah yang belum diputuskan); seluruh tabel budget dihitung ulang untuk struktur 5 hari; (7) **2026-08-21** — ditambahkan rating hotel (⭐⭐⭐⭐, 9.4/10, 17.650 ulasan) dan info stasiun tambahan **Suzhou Industrial Park Railway Station** (11,4km/±30 menit) dari screenshot Amap pengguna; (8) **2026-08-21 — bug fix parser**: sempat dicoba format tabel terpisah "## Hotel & Transportasi" — ternyata bikin info hotel HILANG dari Wisata.html, karena `generate_wisata.py` cuma mengenali heading persis `## Informasi Penerbangan`/`## Informasi Transportasi` (tidak match dengan varian "(Kedatangan)" yang dipakai di sini) dan tidak punya handler untuk heading `##` custom apa pun di luar daftar yang dikenali (di-skip diam-diam, bukan error) — heading "Informasi Transportasi (Kedatangan)" dikembalikan jadi persis "Informasi Transportasi", dan info hotel dikembalikan jadi prose (bukan tabel terpisah) menyatu di section yang sama, sesuai konvensi Nanjing/Wuxi (`### Hotel` sebagai sub-heading H3 tetap ikut ter-parse sebagai prose dalam section H2 induknya — H3 TIDAK memulai section baru, beda dari H2); (9) **2026-08-21 — dipangkas info berulang/kurang relevan**: paragraf "Kenapa Hari 1 dimulai sore" dan "Prioritas transportasi lokal" dihapus (sudah default skill, tidak perlu diulang per file), blockquote "Kota disusun independen" dihapus (duplikat), tabel Informasi Transportasi Pulang dipadatkan (alasan pemilihan stasiun/detail teknis dipangkas jadi 1 kalimat inti) — tujuan: layar lebih fokus ke info yang benar-benar spesifik trip ini; (10) **2026-08-21 — restrukturisasi hari & swap besar** atas beberapa temuan pengguna: **Jinji Lake + Music Fountain dipindah ke Hari 2 (Sabtu)** — Music Fountain cuma tayang Jumat & Sabtu, versi lama di hari Senin tidak terjamin tayang; **Kota Tua Bagian Tengah dipindah ke Hari 3 (Minggu)** — Suzhou Museum tutup tiap Senin jadi aman di hari Minggu; **Panmen→Hanshan→Shantang dipindah ke Hari 4 (Senin)** — tidak ada destinasi di kluster ini yang tutup hari Senin; **Gate of the Orient digeser ke sore/malam** (dari pagi) — gedung kaca ini lebih menarik dilihat saat lampu menyala, sekalian searah jalan ke titik nonton Music Fountain; **Taihu Lake Wetland Park (beserta Shoutao Lake & Wuzhong Taihu Tourist Zone yang satu kawasan) dipindah ke Cadangan, diganti Master of Nets Garden di Hari 5** — Taihu ±40-45 menit sekali jalan terlalu jauh untuk hari kepulangan, sementara Master of Nets Garden persis di kawasan hotel; Dayangshan & Tianpingshan (sebelumnya Plan-B untuk Taihu) ikut dipindah ke Cadangan karena Taihu sendiri sudah bukan itinerary utama; **Baoen Temple/North Pagoda dipindah ke Cadangan** atas permintaan pengguna. Total budget berubah dari 1.236 CNY (Rp3.275.400) jadi 1.104 CNY (Rp2.925.600) — turun karena Master of Nets Garden (CNY 40/org) lebih murah dari Taihu Lake Wetland Park (CNY 60/org) + ongkos transport jauhnya; (11) **2026-08-21** — **Suzhou Ancient Canal Night Cruise ditambahkan ke Hari 4** (naik perahu dari Baijuyi Wharf, Shantang Street, versi malam "Oriental Venice", CNY 100/org) setelah makan malam Shantang, menggantikan slot kembali langsung ke hotel — Total Hari 4 282→482 CNY, Grand Total 1.104→1.304 CNY (Rp2.925.600→Rp3.455.600); ditambahkan 4 entri baru ke Cadangan atas permintaan pengguna: **Lion Grove Garden** (searah Hari 3), **The Lingering Garden** (taman klasik UNESCO lain, tidak searah kluster manapun), **Yuanrong Times Square** (mal Jinji Lake, searah Hari 2), **Ruiguang Tower** (pagoda dalam kompleks Panmen, sudah termasuk kunjungan Hari 4); (12) **2026-08-21** — 3 entri Cadangan dihapus atas permintaan pengguna (terlalu jauh dari rute, tidak akan pernah dipakai): **Suzhou Bay Huangjin Lake Shore**, **Zhouzhuang Water Town**, **Tongli Water Town**. Referensi "lihat Cadangan" untuk Zhouzhuang/Tongli di bagian "Destinasi Terkenal Lain" diperbarui jadi keterangan singkat langsung (tidak menunjuk ke Cadangan lagi). (13) **2026-08-22** — Hotel & tiket HSR kedatangan (dari Wuxi) sekarang masuk GRAND TOTAL Ringkasan Budget (sebelumnya eksplisit "tidak dihitung, di luar scope budget Suzhou"). Hotel Rp1.800.000 (4 malam, fixed), tiket HSR kedatangan ⚠️ estimasi ±CNY 20/org. GRAND TOTAL naik dari 1.304 CNY (Rp3.455.600, aktivitas saja) jadi **2.023 CNY (Rp5.361.600)**.

> **✅ Sudah lewat Golden Week:** Golden Week resmi 1–8 Oktober. Trip Suzhou 10–14 Oktober ini sepenuhnya di luar periode itu — jauh lebih tenang. Sabtu (11 Okt) tetap akhir pekan domestik biasa, jadi mungkin sedikit lebih ramai dari hari kerja tapi tidak sebanding puncak Golden Week.

## Informasi Transportasi

| | |
|---|---|
| Tanggal & Jam Kedatangan | Jumat, 10 Oktober, **±17:00**, via HSR dari Wuxi |
| Tiket HSR kedatangan | ⚠️ estimasi ±CNY 20/org (2 org, ±Rp106.000) |
| Titik kedatangan → Hotel | Taksi/Didi singkat ke hotel |

**Catatan biaya:** semua angka CNY/IDR di bawah untuk **2 orang (dewasa)**. Kurs dipakai: **Rp2.650/CNY** (kurs tetap, lihat [[exchange-rates]]). Tanda — berarti gratis/tidak ada biaya.

**Hotel:** Suzhou City Holiday Hotel (Shiquan Street·Wangshi Garden) — 苏州城市假日酒店(十全街网师园店), ⭐⭐⭐⭐ rating 9.4/10 (17.650 ulasan). Rp1.800.000 (4 malam). No. 77 North Nanyuan Road (北南园路77号), Canglang Subdistrict, Gusu District, Suzhou. ±4,8km (garis lurus) dari pusat kota. Anchor MRT: **Nanyuanbeilu Station (南园北路, Line 5)**, ±140m/±2 menit jalan kaki — dipakai sebagai basis SEMUA rute harian di bawah. Stasiun/terminal lain di sekitar hotel: Nanmen Metro Station (1,2km/±17 menit jalan kaki), Suzhou South Gate Passenger Transport Terminal (bus, 1,4km/±20 menit jalan kaki), Suzhou Railway Station (苏州站, stasiun HSR utama — 5,9km/±27 menit naik mobil, TIDAK dekat/jalan kaki), Suzhou Industrial Park Railway Station (苏州工业园区站, 11,4km/±30 menit naik mobil, relevan hanya untuk leg dari arah timur/Jinji Lake).

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
| 19:00–20:00 | Jalan santai sekitar Shiquan Street / area hotel | Opsional: **Master of Nets Garden (网师园 · Wǎngshī Yuán) versi Night Garden** kalau masih fit — CNY 100/org (±Rp265.000/org), TIDAK dihitung di total default hari ini. Beda dari kunjungan versi siang di Hari 5 pagi — murni bonus malam kalau berminat lihat suasana lampion, lihat entri Lampiran untuk detail | — | — |
| | **TOTAL HARI 1** | | **80** | **Rp212.000** |

**Plan-B hari ini:** kalau kedatangan lebih malam dari rencana — langsung istirahat penuh di hotel, makan malam di resto terdekat hotel saja (Shiquan Street tetap buka larut, banyak pilihan santai).

---

## Hari 2 — Sabtu, 11 Oktober (Jinji Lake Penuh + Music Fountain Malam)

> **Rute:** dari hotel ke kawasan Jinji Lake (Line 1, Stasiun Dongfangzhimen), lewat 2x transfer (Line 5→Nanmen/Laodonglu→Line 4/2→interchange ke Line 1). Sengaja ditaruh di hari Sabtu — Jinji Lake Music Fountain hanya tayang Jumat & Sabtu, jadi hari ini pertunjukannya terjamin ada.

| Jam | Kegiatan | Catatan | CNY | IDR |
|---|---|---|---|---|
| 08:00 | Sarapan | ±CNY 12/org | 24 | Rp63.600 |
| 08:30–09:15 | Metro ke area Jinji Lake (Dongfangzhimen, Line 1) | ±35-40 menit termasuk transfer | 20 | Rp53.000 |
| 09:15–11:45 | **Jinji Lake Walking Tour** (versi penuh) | Gratis, jalur sangat datar. Sewa sepeda opsional ±CNY 17/jam/org, tidak dihitung | — | — |
| 11:45–12:45 | Makan siang di tepi danau | ±CNY 25/org | 50 | Rp132.500 |
| 12:45–16:00 | Santai lanjut promenade danau | Gratis | — | — |
| 17:00–18:00 | Makan malam ringan sekitar Jinji Lake | ±CNY 40/org | 80 | Rp212.000 |
| 18:00–18:45 | **The Oriental Gate / Gate of the Orient** | Gratis, lihat dari luar — landmark ini lebih bagus dilihat sore/malam saat lampu gedung mulai menyala, dan searah jalan ke titik nonton Music Fountain | — | — |
| 19:00–19:30 | **Jinji Lake Music Fountain** | Gratis. Tayang tiap Sabtu 19:30 — terjamin di hari ini | — | — |
| 20:00–20:30 | Metro kembali ke hotel | ±35-40 menit | 20 | Rp53.000 |
| | **TOTAL HARI 2** | | **194** | **Rp514.100** |

**Plan-B hari ini:** **Suzhou Centre Plaza (Mall)** — indoor, satu kawasan dengan Jinji Lake, kalau hujan deras.

---

## Hari 3 — Minggu, 12 Oktober (Kota Tua Bagian Tengah)

> **Rute:** dari hotel naik Line 5 (Nanyuanbeilu) 1 halte ke **Nanmen**, transfer **Line 4** menuju **Beisita** — kluster museum/taman/kelenteng di utara kota tua, ditutup jalan malam di Pingjiang Road.

| Jam | Kegiatan | Catatan | CNY | IDR |
|---|---|---|---|---|
| 08:00 | Sarapan di sekitar hotel | Bubur/baozi kukus, ±CNY 12/org | 24 | Rp63.600 |
| 08:30–09:00 | Metro: Nanyuanbeilu (Line 5) → Nanmen → transfer Line 4 → Beisita | ±25-30 menit termasuk transfer | 12 | Rp31.800 |
| 09:00–10:30 | **Suzhou Museum** | Gratis (reservasi online/tunjukkan paspor) | — | — |
| 10:45–11:45 | Makan siang: Yangchun mian (mie kuah polos) | ±CNY 20/org | 40 | Rp106.000 |
| 11:45–13:00 | **Guanqian Street** & **Xuanmiao Temple** | Jalan kaki singkat dari Beisita, pedestrian street. Pelataran gratis, masuk aula utama Xuanmiao opsional ±CNY 20/org | 40 | Rp106.000 |
| 13:00–15:30 | **Humble Administrator's Garden** | Via Stasiun Zhuozhengyuan·Suzhou Museum (Line 6), searah/berdekatan dengan Beisita & Museum. Tiket ±CNY 80/org | 160 | Rp424.000 |
| 15:45–16:15 | Metro ke **Pingjiang Road** (transfer ke Line 1, Stasiun Xiangmen) | — | 12 | Rp31.800 |
| 18:00–19:30 | Makan malam + jalan malam **Pingjiang Road** | Kanal bersejarah, gratis. Makan ±CNY 25/org | 50 | Rp132.500 |
| 20:00 | Kembali ke hotel (metro, transfer di Nanmen) | — | 12 | Rp31.800 |
| | **TOTAL HARI 3** | | **350** | **Rp927.500** |

**Plan-B hari ini:** **Huqiu Wetland Park** — gratis, alternatif kalau ingin ganti salah satu spot berbayar dengan opsi gratis (searah, sekitar Beisita). **Baoen Temple / North Pagoda** juga bisa disisipkan kembali (persis 1 jalur dengan Museum) kalau masih ada waktu — lihat Cadangan.

---

## Hari 4 — Senin, 13 Oktober (Panmen di Depan Hotel → Hanshan → Shantang)

> **Rute:** Panmen persis 1 halte dari hotel — mulai pagi di sini dulu sebelum lanjut ke kluster barat (Hanshan Temple/Shantang, via Line 5→Laodonglu→transfer Line 2). Hari kerja biasa, relatif lebih tenang dibanding akhir pekan.

| Jam | Kegiatan | Catatan | CNY | IDR |
|---|---|---|---|---|
| 08:00 | Sarapan | ±CNY 12/org | 24 | Rp63.600 |
| 08:15–08:30 | Metro 1 halte: Nanyuanbeilu → Nanmen | Bisa juga jalan kaki ±1,2km/17 menit kalau ingin pemanasan pagi | 8 | Rp21.200 |
| 08:45–10:00 | **Wumen Bridge** (gratis) + **Panmen Scenic Spots** | Tiket Panmen ±CNY 40/org — persis di depan hotel | 80 | Rp212.000 |
| 10:00–11:00 | Makan siang sekitar Panmen | ±CNY 25/org | 50 | Rp132.500 |
| 11:00–11:45 | Metro: Nanmen → Laodonglu (Line 5, 2 halte) → transfer Line 2 → Shantangjie | ±30-35 menit termasuk transfer | 20 | Rp53.000 |
| 11:45–13:45 | **Hanshan Temple** (±CNY 20/org) + **Fengqiao Scenic Area** (gratis, jalan sekitar) | Situs kuil terkenal lewat puisi kuno, bersebelahan | 40 | Rp106.000 |
| 14:00–16:00 | **Shantang Street** | "Jalan Kuno No.1 Suzhou", kanal & jembatan tua, gratis | — | — |
| 16:00–17:30 | Makan malam sekitar Shantang | ±CNY 20/org | 40 | Rp106.000 |
| 18:00–18:45 | **Suzhou Ancient Canal Night Cruise** | Naik perahu dari Baijuyi Wharf di Shantang Street, versi malam "Oriental Venice". Tiket ±CNY 100/org | 200 | Rp530.000 |
| 19:00 | Kembali ke hotel (Line 2 → Laodonglu → transfer Line 5 → Nanyuanbeilu) | ±30-35 menit | 20 | Rp53.000 |
| | **TOTAL HARI 4** | | **482** | **Rp1.277.300** |

**Plan-B hari ini:** **Xiyuan Temple (kelenteng kucing)** — ±CNY 10/org (±Rp53.000 untuk 2 orang), dekat Shantang Street, alternatif tenang kalau Hanshan Temple/Fengqiao terlalu ramai atau rute terasa memutar.

---

## Hari 5 — Selasa, 14 Oktober (Master of Nets Garden Dekat Hotel, Checkout, HSR ke Ningbo)

> **Kenapa ini hari ringan:** Master of Nets Garden persis di kawasan hotel/Shiquan Street — tidak perlu transportasi jauh sebelum checkout, pas untuk hari kepulangan. Taihu Lake Wetland Park (±40-45 menit sekali jalan) dipindah ke Cadangan karena terlalu jauh untuk hari kepulangan.

| Jam | Kegiatan | Catatan | CNY | IDR |
|---|---|---|---|---|
| 08:00 | Sarapan | ±CNY 12/org | 24 | Rp63.600 |
| 08:30–09:00 | Jalan kaki ke **Master of Nets Garden** | Persis di kawasan hotel/Shiquan Street, tidak perlu transportasi | — | — |
| 09:00–10:30 | **Master of Nets Garden** (versi siang) | Tiket ±CNY 40/org | 80 | Rp212.000 |
| 10:30–11:00 | Jalan kaki balik ke hotel | — | — | — |
| 11:00–12:00 | Checkout hotel, siap-siap | — | — | — |
| 12:00–13:00 | Makan siang dekat hotel | ±CNY 27/org | 54 | Rp143.100 |
| 13:00–14:00 | Waktu buffer / santai | — | — | — |
| 14:00–14:30 | Taksi/Didi ke **Suzhou Railway Station** | ±27 menit, dengan koper lebih praktis daripada MRT+transfer | 40 | Rp106.000 |
| 15:00 | HSR Suzhou → Ningbo | ±2,5-3,5 jam, tiket ±CNY 147-218/org | — | *(masuk budget Ningbo)* |
| | **TOTAL HARI 5** | | **198** | **Rp524.700** |

**Plan-B hari ini:** kalau Master of Nets Garden tutup lebih awal dari perkiraan atau cuaca buruk — jalan santai saja di Shiquan Street (gratis, langsung depan hotel) sampai waktu checkout.

---

## Ringkasan Budget Total (2 Orang, 4 Malam / 5 Hari di Suzhou)

Tiket HSR Suzhou→Ningbo TIDAK termasuk (masuk budget Ningbo, lihat "Informasi Transportasi Pulang"). Angka di bawah biaya aktivitas harian (tiket masuk, makan, transport lokal). Kurs: Rp2.650/CNY.

| Hari | CNY | IDR |
|---|---|---|
| Hari 1 (10 Okt) | 80 | Rp212.000 |
| Hari 2 (11 Okt) | 194 | Rp514.100 |
| Hari 3 (12 Okt) | 350 | Rp927.500 |
| Hari 4 (13 Okt) | 482 | Rp1.277.300 |
| Hari 5 (14 Okt) | 198 | Rp524.700 |
| **Subtotal aktivitas harian** | **1.304** | **Rp3.455.600** |

| Kategori | CNY | IDR |
|---|---|---|
| Tiket masuk (Xuanmiao Hall, Humble Administrator's Garden, Panmen, Hanshan Temple, Master of Nets Garden, Suzhou Ancient Canal Night Cruise) | 600 | Rp1.590.000 |
| Makan (semua hari) | 510 | Rp1.351.500 |
| Transport lokal (metro + taksi singkat) | 194 | Rp514.100 |
| Tiket HSR kedatangan dari Wuxi (2 org) | ≈40 | Rp106.000 |
| Hotel (4 malam) | ≈679 | Rp1.800.000 |
| **GRAND TOTAL** | **2.023** | **Rp5.361.600** |

**Catatan:** Guanqian Street (pelataran), Jinji Lake, Shantang Street, Fengqiao gratis (tidak dihitung). Sanqing Hall Xuanmiao Temple sudah dihitung di baris terkait. Music Fountain (Hari 2) terjamin tayang karena jatuh di hari Sabtu.

---

## Catatan Penting Lainnya

- **Fisik/lutut:** hindari tempat dengan tangga curam tanpa lift. Semua jalur di itinerary ini (kanal, taman, promenade danau) datar dan aman untuk lutut.
- **Makanan:** semua rekomendasi disesuaikan agar tidak pedas, tidak asam, tidak berminyak/gorengan — sesuai karakter masakan Suzhou yang cenderung manis-ringan.
- **Transportasi:** prioritas MRT/jalan kaki untuk jarak dekat; taksi hanya untuk bawa koper (Hari 1 & Hari 5).
- **Tempat berbayar** ditandai jelas — sebagian bisa diganti Plan-B yang lebih murah/gratis untuk hemat biaya.

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
Di luar itinerary utama: **Tiger Hill (虎丘 · Hǔqiū)** — bukit dengan pagoda miring ("Leaning Tower of China"), salah satu ikon Suzhou paling terkenal. **Zhouzhuang** dan **Tongli** — kota air kuno ±30-50 menit di luar Suzhou, populer sebagai day-trip terpisah tapi tidak masuk trip kali ini (terlalu jauh dari rute). **Suzhou Industrial Park** di sekitar Jinji Lake — wajah modern kota ini, kontras dengan kota tua.

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

## Hari 2 — Sabtu, 11 Oktober

### The Oriental Gate / Gate of the Orient (东方之门 · Dōngfāng Zhī Mén) ⚠️
Gedung pencakar langit berbentuk gerbang raksasa (dijuluki warga lokal "celana panjang" karena bentuknya) yang jadi landmark arsitektur kontroversial-tapi-ikonik Suzhou modern, selesai dibangun 2015 di tepi Jinji Lake sebagai simbol gerbang masuk ke distrik bisnis baru. Dijadwalkan dilihat sore/malam (bukan pagi) di itinerary ini — gedung kaca ini lebih menarik dilihat saat lampu mulai menyala, dan lokasinya persis searah jalan ke titik nonton Music Fountain.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** Stasiun Dongfangzhimen (东方之门, Line 1) — gedung ini punya stasiun MRT sendiri, tersambung langsung. Sisi barat Jinji Lake. Dari hotel: Line 5 → Nanmen/Laodonglu → transfer ke Line 1 (±35-40 menit total).

**Jam Operasional:** area luar/lihat dari luar bisa kapan saja; bangunan sendiri fungsinya hotel/kantor/residensial (bukan objek wisata dengan jam buka publik). Paling bagus dilihat menjelang malam saat lampu gedung menyala.

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

**Jam Operasional:** ⚠️ jadwal bervariasi musiman & sumbernya sedikit tidak konsisten — per sumber terbaru: Jumat & Sabtu 19:30 (durasi ±30 menit), tambahan sesi saat libur nasional. Hari 2 itinerary ini sengaja jatuh di hari **Sabtu** supaya pertunjukan terjamin ada. Pertunjukan dibatalkan saat cuaca buruk. **Cek jadwal WeChat/website resmi Jinji Lake Scenic Area H-1** untuk konfirmasi terakhir.

**Tiket:** Gratis.

- Foto/info: https://www.google.com/search?q=Jinji+Lake+Music+Fountain
- Video referensi: https://www.youtube.com/results?search_query=Jinji+Lake+Music+Fountain+Suzhou

### Suzhou Centre Plaza / Suzhou Center (苏州中心 · Sūzhōu Zhōngxīn) ⚠️ — Plan-B Hari 2
Mal besar di tepi Jinji Lake dengan atap gelombang khas ("cloud roof") yang jadi salah satu ikon arsitektur baru Suzhou, plus taman atap (rooftop garden) dengan pemandangan langsung ke Gate of the Orient.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** Stasiun Dongfangzhimen (Line 1), keluar Exit 3 — tersambung langsung ke mal, tidak perlu keluar ke jalan.

**Jam Operasional:** 10:00–22:00 setiap hari.

**Tiket:** Gratis masuk (mal), bukan sesi belanja di itinerary ini.

**Kenapa jadi Plan-B:** TIDAK termasuk destinasi wisata utama (prinsip itinerary ini menghindari sesi belanja), tapi lokasinya di tepi Jinji Lake — pilihan praktis untuk berteduh kalau hujan deras.

- Foto/info: https://en.wikipedia.org/wiki/Suzhou_Center
- Video referensi: https://www.youtube.com/results?search_query=Suzhou+Center+Mall+Jinji+Lake

## Hari 3 — Minggu, 12 Oktober

### Suzhou Museum (苏州博物馆 · Sūzhōu Bówùguǎn) ✅
Dirancang oleh arsitek kelahiran Suzhou I.M. Pei (juga arsitek Piramida Kaca Louvre), dibuka 2006 sebagai proyek terakhir karir panjangnya. Bangunan ini memadukan estetika taman klasik Suzhou (dinding putih, atap abu-abu, kolam batu) dengan garis geometris modern — letaknya pun sengaja bersebelahan dengan Humble Administrator's Garden supaya menyatu dengan lanskap kota tua.

✅ Nama Hanzi terverifikasi langsung dari halaman ranking Amap.

**Akses:** Stasiun Beisita (北寺塔, Line 4), keluar Exit 4, jalan kaki ±700m ke timur. Dari hotel: Nanyuanbeilu (Line 5) → Nanmen → transfer Line 4 → Beisita, ±25-30 menit. Alternatif: Stasiun Humble Administrator's Garden·Suzhou Museum (Line 6).

**Jam Operasional:** Selasa–Minggu 09:00–17:00 (masuk terakhir 16:00), tutup setiap Senin kecuali libur nasional.

**Tiket:** Gratis (sejak 18 Mei 2008); sebagian pameran khusus mungkin berbayar terpisah.

- Foto/info: https://en.wikipedia.org/wiki/Suzhou_Museum
- Video referensi: https://www.youtube.com/results?search_query=Suzhou+Museum+I.M.+Pei+tour

### Guanqian Street (观前街 · Guānqián Jiē) ⚠️
Guanqian Street ('jalan di depan kelenteng') berkembang sejak Dinasti Song sebagai pusat perdagangan di depan Xuanmiao Temple, dan sekarang jadi salah satu pedestrian street belanja & jajanan tersibuk di Suzhou.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** Stasiun Chayuanchang (察院场, Line 4), keluar Exit 2, jalan kaki ±450m ke utara — searah/lanjutan dari Beisita di rute Hari 3 ini.

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

**Akses:** Stasiun Zhuozhengyuan·Suzhou Museum (拙政园·苏州博物馆, Line 6), keluar Exit 1, jalan kaki ±450m — satu kompleks dengan Suzhou Museum, searah rute Hari 3 ini.

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

### Huqiu Wetland Park (虎丘湿地公园 · Hǔqiū Shīdì Gōngyuán) ⚠️ — Plan-B Hari 3
Taman lahan basah di sekitar kawasan Tiger Hill (Huqiu), dikembangkan sebagai ruang hijau publik gratis dengan jalur air & vegetasi alami, luas ±12 km² — kontras dengan taman klasik berbayar di sekitarnya. Rumah bagi 200+ spesies burung.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** Stasiun Sunwu Memorial Museum (孙武纪念苑, Line 4), keluar Exit 2, jalan kaki ±15 menit — searah kluster Line 4 Hari 3 ini.

**Jam Operasional:** ±06:00–20:00 setiap hari.

**Tiket:** Gratis (beberapa aktivitas tambahan di dalam mungkin berbayar).

**Kenapa jadi Plan-B:** gratis, alternatif praktis kalau ingin mengurangi satu spot berbayar hari itu.

- Foto/info: https://www.google.com/search?q=Huqiu+Wetland+Park+Suzhou
- Video referensi: https://www.youtube.com/results?search_query=Huqiu+Wetland+Park+Suzhou

## Hari 4 — Senin, 13 Oktober

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

**Tiket:** Gratis jalan di sepanjang jalan. Boat tour terpisah — lihat entri **Suzhou Ancient Canal Night Cruise** di bawah untuk versi malam yang dipakai di Hari 4.

- Foto/info: https://en.wikipedia.org/wiki/Shantang_Street
- Video referensi: https://www.youtube.com/results?search_query=Shantang+Street+Suzhou

### Suzhou Ancient Canal Night Cruise (苏州古运河夜游 · Sūzhōu Gǔ Yùnhé Yèyóu) ⚠️
Perahu wisata menyusuri kanal kuno Suzhou di malam hari, berangkat dari dermaga di kawasan Shantang Street (Baijuyi Wharf) — versi malam dijuluki "Oriental Venice" karena suasana lampion & bangunan tepi kanal yang menyala. Cara paling santai untuk melihat kota tua dari sisi air, pelengkap jalan kaki di Shantang Street.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** Naik dari dermaga di Shantang Street (山塘街, Line 2, Exit 3) — sama persis dengan akses Shantang Street, tidak perlu transportasi tambahan.

**Jam Operasional:** boating 08:00–17:00 (siang) & 18:00–20:00 (malam); durasi tiap sesi ±40 menit–1 jam.

**Tiket:** Siang CNY 55/org (±Rp145.750/org), malam "Oriental Venice" CNY 100/org (±Rp265.000/org) — versi malam yang dipakai di Hari 4 itinerary ini.

- Foto/info: https://www.tripadvisor.com/AttractionProductReview-g297442-d20003384-Suzhou_Ancient_Grand_Canal_Cruise_Experience-Suzhou_Jiangsu.html
- Video referensi: https://www.youtube.com/results?search_query=Suzhou+Ancient+Canal+Night+Cruise+Shantang

### Xiyuan Temple (西园寺 · Xīyuán Sì, kelenteng kucing) ✅ — Plan-B Hari 4
Awalnya bagian dari taman pribadi keluarga bangsawan era Ming, diubah jadi kelenteng Buddha tahun 1635. Terkenal dengan kolam kura-kura besar dan Aula 500 Arhat berisi ratusan patung Buddha berlapis emas.

✅ Nama Hanzi terverifikasi langsung dari halaman ranking Amap.

**Akses:** TIDAK ada stasiun MRT persis di depan — naik bus 6/10/11/17/40/Y1/Y3 turun halte Xiyuan (西园站), searah kawasan Shantang Street.

**Jam Operasional:** 07:30–17:30 setiap hari (loket tutup 17:00).

**Tiket:** CNY 5/org (±Rp13.250/org).

**Kenapa jadi Plan-B:** dekat Shantang Street, jalur datar, suasana tenang — alternatif kalau Hanshan Temple/Fengqiao terasa memutar dari rute utama.

- Foto/info: https://en.wikipedia.org/wiki/Xiyuan_Temple
- Video referensi: https://www.youtube.com/results?search_query=Xiyuan+Temple+Suzhou+turtle+pond

## Hari 5 — Selasa, 14 Oktober

### Master of Nets Garden (网师园 · Wǎngshī Yuán) ✅
Salah satu taman klasik terkecil tapi paling dipuji desainnya di Suzhou, pertama dibangun era Song (abad ke-12) oleh seorang pejabat yang pensiun dan menamainya "Wangshi Yuan" (taman tukang jaring ikan) sebagai sindiran rendah hati terhadap karir birokrasinya. Terkenal dengan pertunjukan "Night Garden" di musim panas-gugur yang menampilkan opera Kunqu di antara paviliun bercahaya lampion — situs UNESCO World Heritage. Nama hotel trip ini merujuk langsung ke taman ini, dan lokasinya memang persis di area yang sama.

✅ Nama Hanzi terverifikasi langsung dari halaman ranking Amap.

**Akses:** Persis di kawasan hotel/Shiquan Street — TIDAK ada stasiun MRT persis di depan, tapi jaraknya sangat dekat jalan kaki dari hotel (searah Shiquan Street). Alternatif: halte bus "Master of Nets Garden West" (bus 529/9003/9010).

**Jam Operasional:** 21 April–20 Oktober 07:30–17:30 (loket tutup 17:00); 21 Oktober–20 April 07:30–17:00. Night Garden: pertengahan Maret–pertengahan November, setiap malam 19:30–22:00.

**Tiket:** Siang CNY 40/org musim ramai, CNY 30/org musim sepi (±Rp106.000/79.500 per org). Night Garden CNY 100/org (±Rp265.000/org) — terpisah dari tiket siang, opsional di Hari 1 malam kalau masih berminat lihat versi lampion. Gratis untuk lansia 70+ (bawa identitas) & anak di bawah 1,2m.

- Foto/info: https://en.wikipedia.org/wiki/Master_of_the_Nets_Garden
- Video referensi: https://www.youtube.com/results?search_query=Master+of+the+Nets+Garden+Suzhou+night

## Cadangan

Tempat-tempat ini layak dikunjungi, tapi sengaja TIDAK dimasukkan ke itinerary maupun Plan-B — alasannya ditulis di masing-masing uraian.

### Baoen Temple / North Pagoda (Beisi Ta) (北寺塔 · Běisì Tǎ) ⚠️
Pagoda tertinggi di selatan Sungai Yangtze (±76m, 9 lantai kayu bersusun), berdiri di atas lahan kuil yang riwayatnya diperkirakan mundur hingga era Tiga Kerajaan (abad ke-3). Bangunan yang ada sekarang direkonstruksi era Dinasti Song (abad ke-12). Taman di sekelilingnya rindang dan tenang, cocok untuk jalan santai tanpa harus naik ke atas pagoda.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** Stasiun Beisita (北寺塔, Line 4) — pagoda punya stasiun MRT sendiri, langsung di depan gerbang. Persis sejalur dengan Suzhou Museum (Hari 3).

**Jam Operasional:** ±08:00–18:00 setiap hari (loket tutup 17:30). Tidak ada hari libur rutin.

**Tiket:** ⚠️ harga bervariasi antar sumber (CNY 25–40/org untuk naik ke atas pagoda, ±Rp66.250–106.000/org) — kalau dikunjungi, TIDAK naik ke atas (pertimbangan lutut), cukup nikmati taman & pagoda dari luar yang **gratis**.

**Kenapa tidak dimasukkan:** searah Suzhou Museum tapi Hari 3 sudah cukup padat (Museum, Guanqian, Xuanmiao, Humble Administrator's Garden, Pingjiang Road) — bisa disisipkan kalau ternyata ada waktu ekstra.

**Terkait:** Hari 3

- Foto/info: https://en.wikipedia.org/wiki/Bao%27en_Temple,_Suzhou
- Video referensi: https://www.youtube.com/results?search_query=North+Temple+Pagoda+Suzhou+Beisi+Ta

### Suzhou Taihu Lake Wetland Park (苏州太湖湿地公园 · Sūzhōu Tàihú Shīdì Gōngyuán) ⚠️
Taman lahan basah di tepi Danau Taihu — danau terbesar ketiga di China, terkenal dengan batu-batu taihu (batu kapur berlubang khas) yang dulu banyak diambil untuk menghias taman klasik Suzhou. Jalur promenadenya datar dan luas, kontras menyegarkan dari padatnya kota tua.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap. ⚠️ Catatan tambahan: ada KEMUNGKINAN dua entitas berbeda dengan nama mirip di kawasan ini — "Suzhou Taihu Lake Wetland Park" (berbayar) vs "Taihu Hubin National Wetland Park"/wetland tepi danau lain (gratis) — cek nama persis di Amap/Trip.com sebelum berangkat supaya tidak salah lokasi.

**Akses:** **Stasiun Taihu Xiangshan (太湖香山, Line 5) — LANGSUNG dari hotel TANPA transfer**, ±40-45 menit naik metro. Dari stasiun, taksi/bus singkat ±10-15 menit ke pintu masuk taman.

**Jam Operasional:** 08:30–17:00 (masuk terakhir 16:00).

**Tiket:** ⚠️ harga bervariasi antar sumber — CNY 60/org (±Rp159.000/org) hingga versi gratis/CNY 20/org tergantung sumber & mungkin tergantung area spesifik yang dimaksud. Cek harga pasti di loket/Trip.com sebelum berangkat.

**Kenapa tidak dimasukkan:** ±40-45 menit sekali jalan dari hotel — terlalu jauh untuk hari kepulangan (Hari 5), dan tidak ada hari lain yang tersisa untuk dedicated day khusus Taihu di trip 5-hari ini. Cocok jadi tambahan kalau durasi trip Suzhou diperpanjang di kesempatan lain.

- Foto/info: https://en.wikipedia.org/wiki/Lake_Tai
- Video referensi: https://www.youtube.com/results?search_query=Suzhou+Taihu+Lake+Wetland+Park

### Shoutao Lake Scenic Area (寿桃湖 · Shòutáo Hú) ⚠️
Danau kecil (±400 mu/26.7 hektar, kedalaman maksimum 70m) hasil genangan air tanah alami sejak penambangan batu dilarang tahun 1999 di kawasan Wuzhong. Batu-batu di tengah danau menyerupai buah persik umur panjang (asal namanya), juga dijuluki "Guilin Mini"-nya Suzhou. Jadi spot foto yang relatif belum ramai turis.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** Satu kawasan resor dengan Taihu Xiangshan (Line 5) — taksi/Didi singkat dari stasiun, lokasi di kawasan Wuzhong dekat persimpangan Lingtian Road & Zhangjingbang Road.

**Jam Operasional:** buka sepanjang tahun, tidak ada jam tutup khusus (area publik terbuka).

**Tiket:** Gratis.

**Kenapa tidak dimasukkan:** satu kawasan dengan Taihu Lake Wetland Park (lihat entri di atas) yang sendiri sudah tidak masuk itinerary utama — hanya realistis kalau ada waktu ekstra dedicated ke kawasan Taihu.

- Foto/info: https://www.google.com/search?q=Shoutao+Lake+Suzhou
- Video referensi: https://www.youtube.com/results?search_query=Shoutao+Lake+Suzhou

### Suzhou Wuzhong Taihu Tourist Zone (吴中太湖旅游度假区 · Wúzhōng Tàihú Lǚyóu Dùjiàqū) ⚠️
Kawasan wisata resmi 5A di tepi Danau Taihu, distrik Wuzhong, seluas ±250 km², mencakup beberapa taman & area publik di sepanjang tepi danau (termasuk Taihu Park, Situ Temple, Lushan).

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap. ⚠️ Kawasan ini luas dan mencakup beberapa sub-area dengan aturan tiket berbeda-beda (sebagian gratis, sebagian berbayar) — bagian yang dimaksud di sini adalah area publik/promenade gratis di tepinya, BUKAN atraksi berbayar spesifik di dalamnya.

**Akses:** Satu kawasan resor dengan Taihu Xiangshan (Line 5) — taksi/Didi singkat dari stasiun.

**Jam Operasional:** area publik buka sepanjang hari; sub-atraksi berbayar (mis. Taihu Park, CNY 10/org) punya jam & hari tutup sendiri (tutup Rabu April–Oktober, Selasa-Rabu November–Maret, kecuali libur nasional).

**Tiket:** Gratis untuk area publik/promenade tepi danau.

**Kenapa tidak dimasukkan:** satu kawasan dengan Taihu Lake Wetland Park — sama-sama tidak masuk itinerary utama karena Hari 5 sekarang fokus destinasi dekat hotel.

- Foto/info: https://www.google.com/search?q=Wuzhong+Taihu+Tourist+Zone
- Video referensi: https://www.youtube.com/results?search_query=Wuzhong+Taihu+Tourist+Zone

### Dayangshan National Forest Park (大阳山国家森林公园 · Dàyángshān Guójiā Sēnlín Gōngyuán) ⚠️
Taman hutan nasional di pinggiran barat kota tua Suzhou, terbagi 2 area utama: Wenshu Monastery (dibangun era Dinasti Jin Timur) dan Botanical Garden dengan koleksi tanaman langka (yew, huanghuali, podocarpus). Jalur trekking ringan & udara segar.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** TIDAK ada MRT langsung — taksi/Didi dari kota.

**Jam Operasional:** 09:00–16:30.

**Tiket:** ⚠️ belum ditemukan sumber resmi harga tiket — cek Amap/Trip.com langsung sebelum berangkat.

**Kenapa tidak dimasukkan:** redundant dengan Taihu Lake Wetland Park sebagai pilihan "alam", dan Taihu sendiri sudah tidak masuk itinerary utama karena keterbatasan hari.

- Foto/info: https://www.google.com/search?q=Dayangshan+National+Forest+Park+Suzhou
- Video referensi: https://www.youtube.com/results?search_query=Dayangshan+National+Forest+Park+Suzhou

### Tianpingshan Scenic Spot (天平山 · Tiānpíng Shān) ⚠️
Gunung kecil terkenal dengan pohon maple (paling indah saat musim gugur, sekitar akhir Oktober-awal Desember) dan mata air alami yang sudah jadi tempat rekreasi sejak Dinasti Song.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** MRT Line 1 ke Stasiun Mudu (木渎), transfer bus rute 4, turun halte Tianpingshan (天平山站), ±3.5km dari stasiun Mudu.

**Jam Operasional:** 08:00–17:00 (loket & masuk terakhir 16:30).

**Tiket:** CNY 30/org dewasa, CNY 15/org lansia/anak (±Rp79.500/39.750 per org).

**Kenapa tidak dimasukkan:** jalur hiking gunung cukup menanjak — untuk kondisi lutut, lebih aman hanya dicoba di area bawah/foothill saja, bukan pendakian penuh. Juga di luar musim daun maple terbaik (trip ini 10-14 Okt, puncak maple baru akhir Oktober).

- Foto/info: https://en.wikipedia.org/wiki/Tianping_Mountain
- Video referensi: https://www.youtube.com/results?search_query=Tianpingshan+Suzhou

### Suzhou Culture & Arts Centre (苏州文化艺术中心 · Sūzhōu Wénhuà Yìshù Zhōngxīn) ⚠️
Pusat seni & budaya modern Suzhou rancangan arsitek Prancis Paul Andreu, dibuka 2007, seluas ±150.000 m² di tepi timur Jinji Lake — berisi grand theater, concert hall, bioskop IMAX, sekolah seni, dan Suzhou Jinji Lake Art Museum di dalamnya.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** Stasiun Cultural Expo Center (文化博览中心, Line 1), keluar Exit 1 — tersambung langsung, searah kawasan Jinji Lake (Hari 2).

**Jam Operasional:** area pameran umumnya 10:00–20:00, tutup setiap Senin.

**Tiket:** Gratis masuk gedung; harga tiket pertunjukan/pameran tertentu bervariasi per acara ⚠️.

**Kenapa tidak dimasukkan:** kontennya (galeri/teater indoor) kurang sesuai gaya jalan-jalan outdoor santai yang diprioritaskan trip ini — meski searah rute Hari 2, sengaja tidak ditambahkan supaya hari itu tidak terlalu padat.

**Terkait:** Hari 2

- Foto/info: https://www.google.com/search?q=Suzhou+Culture+%26+Arts+Centre
- Video referensi: https://www.youtube.com/results?search_query=Suzhou+Culture+and+Arts+Centre

### Dongshahu Ecology Park (东沙湖生态园 · Dōngshāhú Shēngtài Yuán) ⚠️
Taman ekologi terbuka terbesar di kawasan ini (±1,21 juta m², termasuk ±540.000 m² area air), tanpa pagar/tembok dengan banyak pintu masuk. Punya sistem 3 pulau (Cherry Blossom Island, Crabapple Island, Reed Island) memadukan bukit & air.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap. ⚠️ Catatan: nama Inggris yang muncul di beberapa sumber sedikit berbeda-beda ("Dongshahu Ecological Park" vs "Shahu Ecological Park") — kemungkinan penamaan/terjemahan tidak konsisten antar platform, bukan berarti dua tempat berbeda, tapi tetap cek nama persis di Amap sebelum berangkat.

**Akses:** Stasiun Dongshahu (东沙湖, Line 1) — taman ini punya stasiun MRT sendiri, searah kawasan Jinji Lake (Hari 2).

**Jam Operasional:** ⚠️ belum ditemukan sumber jam buka-tutup pasti — sebagai taman terbuka tanpa pagar, kemungkinan bisa diakses kapan saja.

**Tiket:** Gratis.

**Kenapa tidak dimasukkan:** redundant dengan Jinji Lake & Taihu Lake Wetland Park sebagai pilihan "taman/danau" trip ini — dipilih yang lebih ikonik.

**Terkait:** Hari 2

- Foto/info: https://www.google.com/search?q=Dongshahu+Ecology+Park+Suzhou
- Video referensi: https://www.youtube.com/results?search_query=Dongshahu+Ecology+Park+Suzhou

### Suzhou Amusement Land (苏州乐园 · Sūzhōu Lèyuán) ⚠️
Taman hiburan skala besar dengan 3 zona utama (Water World, Forest World, Children's World), wahana modern termasuk roller coaster gantung terbesar di China, serta beberapa instalasi bertema landmark dunia (mis. replika Coliseum Romawi, tanda mirip "HOLLYWOOD").

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap. **⚠️ Koreksi dari draft sebelumnya:** nama "Window of the World" yang sebelumnya disandingkan dengan tempat ini sebenarnya taman berbeda yang berlokasi di **Shenzhen**, BUKAN bagian dari Suzhou Amusement Land — kemungkinan tercampur karena konsep temanya mirip (replika landmark dunia). Entri ini murni tentang Suzhou Amusement Land (苏州乐园 · Sūzhōu Lèyuán).

**Akses:** Stasiun Suzhou Amusement Park (苏州乐园, Line 1), jalan kaki ±5 menit.

**Jam Operasional:** ⚠️ bervariasi per zona/musim, cek jadwal spesifik hari kunjungan di Trip.com/website resmi sebelum berangkat.

**Tiket:** CNY 200–260/org dewasa, CNY 150–180/org anak/lansia (±Rp530.000–689.000 / Rp397.500–477.000 per org) tergantung zona & musim; paket combo dewasa+anak mulai CNY 198.

**Kenapa tidak dimasukkan:** berbayar mahal dan berorientasi turis/hiburan, tidak sejalan dengan prinsip trip ini yang mengutamakan tempat gratis/merakyat dan suasana lokal otentik.

- Foto/info: https://en.wikipedia.org/wiki/Suzhou_Amusement_Land
- Video referensi: https://www.youtube.com/results?search_query=Suzhou+Amusement+Land

### Lion Grove Garden (狮子林 · Shīzi Lín) ✅
Salah satu 4 taman klasik terkenal Suzhou, dibangun tahun 1342 oleh biksu Buddha Tianru untuk menghormati gurunya — dijuluki "Lion Grove" karena batu-batu taihu-nya yang berbentuk menyerupai singa, dianggap kompleks batu buatan (rockery) terbesar & paling rumit di antara taman-taman klasik Suzhou. Kublai Khan's descendant dan pelukis terkenal Ni Zan pernah terlibat dalam desainnya.

✅ Nama Hanzi terverifikasi dari sumber yang konsisten (Wikipedia & travel guide resmi).

**Akses:** Stasiun Humble Administrator's Garden·Suzhou Museum (Line 6), Exit 2, jalan kaki beberapa menit. Alternatif: Stasiun Beisita (Line 4), jalan kaki ±1km ke timur. No. 23 Yuanlin Road, Gusu District.

**Jam Operasional:** 1 Maret–31 Oktober 07:30–17:30; 1 November–akhir Februari 07:30–17:00.

**Tiket:** Musim ramai (April, Mei, Juli–Oktober) CNY 40/org (±Rp106.000/org); musim sepi (Januari–Maret, Juni, November–Desember) CNY 30/org (±Rp79.500/org).

**Kenapa tidak dimasukkan:** persis searah/dekat kluster Suzhou Museum & Humble Administrator's Garden (Hari 3), tapi trip ini sudah cukup padat dengan Humble Administrator's Garden sebagai taman klasik utama hari itu — bisa disisipkan kalau ada waktu ekstra.

**Terkait:** Hari 3

- Foto/info: https://en.wikipedia.org/wiki/Lion_Grove_Garden
- Video referensi: https://www.youtube.com/results?search_query=Lion+Grove+Garden+Suzhou

### The Lingering Garden (留园 · Liú Yuán) ✅
Salah satu 4 taman klasik terkenal China (bersama Humble Administrator's Garden, Summer Palace Beijing, dan Chengde Mountain Resort), pertama dibangun era Ming (1593) oleh pejabat Xu Taishi. Terkenal dengan koridor beratap sepanjang ±700m yang menghubungkan seluruh taman dan koleksi batu taihu raksasa termasuk "Cloud-Capped Peak" setinggi ±6,5m — situs UNESCO World Heritage.

✅ Nama Hanzi terverifikasi dari sumber yang konsisten (Wikipedia & travel guide resmi).

**Akses:** Stasiun Shi Road (石路, Line 2), Exit 1, jalan kaki ke utara ±300m via Guangji South Road.

**Jam Operasional:** 1 Maret–31 Oktober 07:30–17:30 (loket tutup 17:00); 1 November–28 Februari 07:30–17:00 (loket tutup 16:30).

**Tiket:** Musim ramai (April, Mei, Juli–Oktober) CNY 55/org (±Rp145.750/org); musim sepi (Januari–Maret, Juni, November–Desember) CNY 45/org (±Rp119.250/org).

**Kenapa tidak dimasukkan:** lokasinya di barat kota (dekat Shi Road), tidak searah dengan kluster manapun di itinerary ini — situs UNESCO yang bagus, tapi butuh perjalanan tersendiri. Bisa jadi alternatif kalau ingin ganti Humble Administrator's Garden di kesempatan lain.

- Foto/info: https://en.wikipedia.org/wiki/Lingering_Garden
- Video referensi: https://www.youtube.com/results?search_query=Lingering+Garden+Suzhou

### Yuanrong Times Square (圆融时代广场 · Yuánróng Shídài Guǎngchǎng) ⚠️
Mal besar di tepi timur Jinji Lake, kompleks komersial-hiburan seluas ±210.000 m². Terkenal dengan kanopi LED sepanjang ±500m (salah satu terpanjang di dunia) yang menampilkan pertunjukan cahaya "daun teratai & ikan berenang" setiap malam — jadi daya tarik tersendiri di luar belanja.

⚠️ Nama Hanzi belum diverifikasi langsung dari halaman Amap.

**Akses:** Stasiun Times Square (Line 1) — tersambung langsung ke mal.

**Jam Operasional:** toko umumnya ±10:00–22:00; pertunjukan kanopi LED tayang rutin tiap malam (jadwal spesifik bervariasi, cek on-site).

**Tiket:** Gratis masuk (mal).

**Kenapa tidak dimasukkan:** sesi belanja/mal bukan prioritas trip ini (sama alasan seperti Suzhou Centre Plaza) — meski searah kawasan Jinji Lake (Hari 2), sengaja tidak ditambahkan supaya hari itu tetap fokus outdoor.

**Terkait:** Hari 2

- Foto/info: https://www.trip.com/travel-guide/shops/suzhou/yuanrong-times-square-10567883/
- Video referensi: https://www.youtube.com/results?search_query=Yuanrong+Times+Square+Suzhou

### Ruiguang Tower (瑞光塔 · Ruìguāng Tǎ) ✅
Pagoda 7 lantai berbentuk oktagonal setinggi ±53,6m, dibangun era Dinasti Song Utara — bagian dari kompleks Panmen Scenic Spots, berdiri berdekatan dengan Wumen Bridge dan gerbang kota kuno.

✅ Nama Hanzi terverifikasi dari sumber yang konsisten (Wikipedia & Trip.com).

**Akses:** Sama dengan Panmen Scenic Spots — Stasiun Nanmen (Line 4 & Line 5), persis 1 halte MRT dari hotel.

**Jam Operasional:** 08:30–16:00 sepanjang tahun.

**Tiket:** Termasuk tiket masuk Panmen (CNY 40/org); tambahan CNY 6/org untuk naik ke atas pagoda.

**Kenapa tidak dimasukkan:** sudah termasuk dalam kunjungan Panmen Scenic Spots di Hari 4 (dilihat dari luar sebagai bagian kompleks) — TIDAK naik ke atas pagoda (pertimbangan lutut, tangga tanpa lift/eskalator).

**Terkait:** Hari 4

- Foto/info: https://en.wikipedia.org/wiki/Ruiguang_Pagoda
- Video referensi: https://www.youtube.com/results?search_query=Ruiguang+Pagoda+Suzhou

---

*Draft ini masih dalam format .md untuk review. PDF hanya di-generate kalau diminta eksplisit, sesuai skill PDF.*
