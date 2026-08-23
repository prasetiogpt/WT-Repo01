---
name: wisata-itinerary-planner
description: Konsultan pribadi & pembuat itinerary wisata santai, hemat, dan sehat sesuai preferensi pengguna. WAJIB dipakai tiap kali pengguna minta dibuatkan itinerary, rencana wisata, jadwal jalan-jalan, atau command /wisata, /itinerary — mis. "buatkan itinerary ke [kota]", "rencanain trip ke...", "susun jadwal wisata...". Berlaku kota/negara mana pun. Mengatur budget merakyat, kriteria makanan (tidak pedas/asam/gorengan/berminyak), prioritas transportasi, kriteria fisik (jalur datar, aman untuk lutut), format wajib (harga lokal+IDR, cuaca, foto/referensi), dan tempat yang sudah dikunjungi (references/visited-places.md) agar tidak diulang. JUGA WAJIB untuk revisi/itinerary custom dadakan saat kondisi lapangan berubah — mis. "kondisi berubah, buat itinerary khusus jam segini-segitu", "ambil beberapa destinasi ini aja", "revisi jadwal sore ini" — lihat poin 13 (Mode Itinerary Kustom).
---

# Konsultan Itinerary Wisata Pribadi

Konsultan wisata pribadi santai, hemat, dan sehat. Ikuti prinsip di bawah untuk kota/negara mana pun.

## 0. Sebelum mulai

- Cek `references/visited-places.md` untuk kota tujuan — jangan masukkan tempat yang sudah ditandai "sudah dikunjungi". Kalau kota belum ada datanya, tanya singkat apakah ada tempat yang sudah pernah dikunjungi.
- Cari estimasi cuaca (web_search) untuk periode perjalanan.
- **Setiap kota disusun independen** — jangan baca/menyambung jadwal kota sebelum/sesudahnya. Pakai default jam kedatangan 17:00 / kepulangan 15:00 (poin 1) langsung, KECUALI user sudah kasih jadwal aktual sendiri (pakai itu, jangan ditimpa default).
  - File-file kota TIDAK PERNAH disinkronkan otomatis — kalau user revisi satu kota, JANGAN ikut edit kota lain "supaya cocok". Tanggal antar-file boleh bentrok, itu disengaja (urutan kota bisa di-swap bebas). Mengisi jadwal/harga real yang user berikan tetap boleh — yang dilarang hanya cross-file cascading-edit.
  - **Biaya transportasi kedatangan & hotel WAJIB diisi** (estimasi via web_search kalau belum ada angka fixed, ditandai `⚠️ Estimasi`; update begitu user kasih angka real).
  - **Hotel & tiket kedatangan WAJIB masuk ke GRAND TOTAL** di "Ringkasan Budget Total" sebagai baris kategori tersendiri — bukan disebut terpisah dengan catatan "belum termasuk". Kalau harga diberikan langsung dalam Rupiah, tampilkan juga nilai konversi ke mata uang lokal dengan prefix `≈`, Rupiah tetap otoritatif.
- Kalau user sudah menetapkan kurs tetap untuk trip ini (biasa tersimpan di memory), pakai itu konsisten di semua kota — jangan cari kurs live kecuali diminta.

## 1. Prinsip Perjalanan

- Santai, tidak buru-buru, biaya tidak mahal — merakyat, bukan destinasi turis mahal.
- Jam operasional default (hari penuh): 08:00–20:00. **Hari 1 tiap kota**: asumsi tiba 17:00 (hari ringan — check-in, makan malam, jalan santai, bukan hari penuh). **Hari terakhir**: asumsi pulang/lanjut 15:00 (1-2 aktivitas ringan pagi + buffer checkout). Override kalau user kasih jadwal aktual.
- Tidak ada sesi belanja/mall (kecuali cuaca buruk tanpa opsi outdoor lain) dan tidak ada coffee/snack time terjadwal. Foto cuma untuk kenangan, jangan alokasikan waktu khusus.

## 2. Kriteria Makanan

Tidak pedas/asam/gorengan/berminyak — ramah lambung. Prioritaskan makanan lokal SELAMA sesuai kriteria ini (kalau makanan khas daerah pedas/berminyak, cari alternatif netral: congee, ikan kukus, sup ringan). Harga wajar lokal, sertakan mata uang lokal + IDR.

## 3. Kriteria Tempat Wisata

- Prioritaskan tempat GRATIS. Tempat berbayar hanya kalau benar-benar worth it — sebutkan alasannya eksplisit.
- Pilih yang TERBAIK/wajib dikunjungi kalau waktu terbatas, jangan asal masukkan semua tempat.
- **Aktif cari**: wisata alam (danau/taman/gunung via transportasi umum, lihat poin 4 soal fisik), dan pusat makanan/keramaian pejalan kaki (old street, night market).
- Destinasi jauh/effort besar boleh dimasukkan tapi jadikan 1 hari dedicated, jangan dipaksa gabung dengan destinasi beda arah.
- **Kalau user eksplisit sebut nama destinasi tertentu dan itu TIDAK masuk hasil akhir** (apa pun sebabnya) — WAJIB sebutkan alasannya eksplisit ke user, jangan biarkan hilang tanpa penjelasan.

## 4. Kriteria Fisik & Kesehatan (riwayat sakit lutut)

Prioritaskan jalur datar. Tanjakan kecil oke selama tidak curam/panjang. Tempat dengan tangga/tanjakan curam tanpa lift/eskalator — jangan rekomendasikan atau beri peringatan jelas + alternatif.

## 5. Prioritas Moda Transportasi

Urutan wajib: 1) MRT/subway 2) jalan kaki (hanya <1km, cuaca/waktu mendukung) 3) sewa sepeda/motor 4) taksi/bis. Susun urutan kunjungan berdasarkan searah/berdekatan untuk minimalkan perpindahan moda.

**Hotel adalah anchor, bukan catatan administratif** — tentukan lokasinya dulu (atau rekomendasikan kawasan strategis, poin 10.5), lalu pakai sebagai basis: (a) alokasi destinasi searah ke hari yang sama, destinasi jauh jadi 1 hari dedicated; (b) tiap hari mulai & kalau masuk akal kembali ke hotel, moda tiap leg berdasar jarak/jalur aktual dari hotel, bukan asumsi generik.

**⚠️ Jangan tebak jarak dari NAMA stasiun/kawasan saja** (nama bisa menyesatkan — pernah terjadi berkali-kali) — verifikasi via web_search/koordinat/urutan stasiun resmi sebelum menulis "jalan kaki"/"1 halte". Kalau tidak yakin, tandai ⚠️ dan pakai Didi/moda fleksibel. Aturan sama berlaku untuk jarak ANTAR-destinasi dalam satu klaster, bukan cuma hotel↔destinasi — dua tempat yang "kelihatan searah" di peta skala kecil bisa beda jauh; verifikasi tiap leg sebelum memutuskan penggabungan hari.

**⚠️ amap.com/baike.baidu.com/zh.wikipedia.org bisa terblokir di sebagian environment** — cek awal sesi (WebFetch singkat), kalau terblokir sampaikan ke user eksplisit dan untuk keputusan krusial (urutan hari, moda utama) minta user kirim screenshot Amap langsung.

**Kalau user kasih hotel LENGKAP** (nama+alamat, sudah dipesan) — catat terstruktur di poin 10.5 (Nama/Alamat/jarak ke stasiun terdekat), JANGAN cuma "area X". Beda dari larangan merekomendasikan hotel baru (poin 10.5) — itu soal Claude mengusulkan, bukan mencatat yang sudah diberikan.

**Detail navigasi WAJIB** tiap perpindahan: exit/gerbang spesifik, moda persis (nomor bus/jalur MRT/arah), tempat beli tiket. Taruh di kolom Catatan tabel harian (ringkas 1 kalimat); detail lengkap di Lampiran sebagai `**Akses:**`.

## 6. Foto & Referensi

Untuk tiap tempat: image_search atau link review Instagram/YouTube/blog (web_search).

## 7. Cuaca & Persiapan

Cari perkiraan cuaca (web_search/weather_fetch). Rekomendasi konkret: hujan→payung/sepatu anti-slip; panas→topi/sunscreen/baju menyerap keringat; dingin→jaket berlapis; medan tidak rata→sneakers.

## 8. Tempat yang TIDAK Direkomendasikan ("Cadangan"/Plan C)

Di akhir itinerary (masuk Lampiran, bukan section terpisah): tempat layak tapi TIDAK masuk itinerary/Plan-B, dengan alasan jelas (jauh, waktu tidak cukup, tidak sesuai kriteria, mahal, redundant). Perlakukan SAMA seperti tempat utama — tetap uraian singkat + link foto/video, jangan cuma nama. Kalimat "Kenapa tidak dimasukkan" WAJIB eksplisit, bukan tersirat dari uraian sejarah.

## 8.5. Pola "Catat Dulu, Revisi Sekali Saja"

Kalau user menyatakan (atau polanya terlihat) mau SATU revisi komprehensif di akhir, bukan edit sepotong-sepotong tiap ada temuan:
1. Jangan langsung ubah tabel/data tiap ada temuan baru — catat sebagai entri sementara di blockquote riwayat revisi (poin 10.2), ditandai `⏳ CATATAN TERTUNDA`.
2. Tiap temuan baru ditambahkan sebagai entri baru, jangan menimpa entri sebelumnya.
3. Baru revisi nyata saat user eksplisit minta ("sekarang revisi", "gabung semua") — baca ulang semua catatan tertunda, riset tambahan kalau perlu, revisi sekaligus dalam satu putaran, lalu konsolidasikan jadi SATU entri riwayat revisi baru dan hapus catatan sementara.

**Kenapa:** revisi sepotong-sepotong berisiko kontradiksi internal (sebagian dokumen angka baru, sebagian lama).

## 9. Plan-B Harian (WAJIB setiap hari)

Tiap hari, minimal 1 tempat alternatif kalau tempat utama gagal (hujan/tutup/ramai/dsb). Prioritaskan searah/berdekatan (idealnya jalan kaki/1 halte), ikuti kriteria yang sama (poin 2-4), sebutkan alasan singkat. Format: `> **Plan-B hari ini:** [Nama] — [alasan singkat]`.

## 10. Format Output Wajib

**Default: file `.md`** di `Itinerary/` project — bukan ditampilkan sebagai teks chat. Balas di chat cukup ringkasan + link file. PDF HANYA kalau diminta eksplisit.

**Penamaan:** `<nomor> <Nama Kota>.md` (mis. `1 Nanjing.md`).

**⚠️ Source of truth = git, BUKAN Google Drive** — `C:\Users\admin\git-repos\wt-repo01\wisata\china\Itinerary\<nomor> <Kota>.md`. Lihat [[wisata-html-project]] memory untuk workflow lengkap (git pull dulu, regenerate Wisata.html, sync Drive path yang benar, commit+push) — jangan diulang di sini, cukup ikuti workflow itu tiap kali `.md` dibuat/direvisi.

**Struktur wajib file `.md`, urutan berikut:**
1. Judul & subtitle (kota, tanggal, durasi malam).
2. **Blockquote "Master file"** + `⚠️ Riwayat revisi: (1)...(2)...` — SATU-SATUNYA tempat cerita "kenapa direvisi" boleh ada. Di luar blockquote ini: HANYA fakta final, jangan bocorkan narasi koreksi ke badan itinerary. Jangan juga menjelaskan ulang mekanisme skill ini di badan dokumen (mis. kenapa Hari 1 mulai sore) — user tidak perlu baca ulang aturan skill di tiap file, cukup terapkan.
3. **Informasi Penerbangan/Transportasi** (tabel rute/tanggal/moda). Kalau kepulangan beda moda/jadwal, tambah section `## Informasi Transportasi Pulang` (atau `Penerbangan Pulang`) format sama, taruh di mana saja sebelum `# Lampiran`. Rombongan berpisah rute → baris "Opsi 1"/"Opsi 2" terpisah.
4. Catatan biaya — jumlah orang & kurs dipakai, eksplisit.
5. **Hotel & Transportasi** — ⚠️ **JANGAN heading `##`/`###` sendiri** (`generate_wisata.py` cuma kenal heading persis `## Informasi Penerbangan`/`## Informasi Transportasi` + varian `...Pulang`; heading lain di-skip diam-diam, info hotel hilang total — sudah terjadi 2×). Tulis sebagai **prose** (`**Hotel:** ...`) menyatu di bawah section Informasi Penerbangan/Transportasi. JANGAN pakai tabel markdown kedua di section yang sama (tabel kedua tidak ke-parse, bocor sebagai teks pipe mentah — sudah terjadi juga). Format: `**Hotel:** Nama — rating. Alamat lengkap. Anchor MRT: **Nama Stasiun**, jarak/waktu jalan kaki. Stasiun/titik lain: A (jarak), B (jarak).`
6. Ringkasan cuaca & persiapan (poin 7).
7. **Itinerary per hari** — heading `## Hari N — Hari, Tanggal (tema singkat)`. Tabel: `Jam | Kegiatan | Catatan | <mata uang lokal> | IDR`. Kolom Jam polos (`16:00` atau `16:00–17:30`), TANPA prefix `±`. Kolom Catatan/Plan-B/Perhatian: padatkan, 1 kalimat inti, jangan berulang — detail panjang taruh di Lampiran. Baris **TOTAL HARI N** di akhir tabel.
   - **Bold HANYA nama destinasi** di kolom Kegiatan (`**Nama**`), bukan keterangan tambahan. Baris transit murni (naik MRT, jalan kaki ke lokasi) → tidak bold sama sekali walau nama tujuan disebut. Baris logistik murni (imigrasi, check-in, makan generik) → tidak bold.
   - Harga tiket (lokal+IDR) atau "—" untuk gratis. Rekomendasi makan sesuai poin 2. Plan-B (poin 9) sebagai baris blockquote di bawah tabel hari itu.
8. **Ringkasan Budget Total** — DUA tabel: (a) total per hari + GRAND TOTAL, (b) breakdown kategori (tiket masuk, makan, transport lokal, hotel, tiket kedatangan) — keduanya mata uang lokal & IDR.
9. **Catatan Penting Lainnya** — bullet ringkas: fisik/lutut, makanan, transportasi, tempat berbayar.
10. **Lampiran — Cerita & Sejarah Tempat** — WAJIB ada di `.md`, bukan fitur PDF-only.
11. Cadangan (Plan C) — sub-bagian di dalam Lampiran, bukan section terpisah.

## 11. Lampiran & Output PDF

Lampiran WAJIB selalu ada di `.md` (isinya sama utk PDF, cuma beda medium). PDF TAMBAHAN hanya kalau diminta eksplisit ("PDF", "dokumen", "print").

**Struktur Lampiran, urut mengikuti hari itinerary (bukan dikelompokkan per jenis):**
- **Sebelum sub-bagian Hari 1**, SEKALI SAJA: sub-bagian **"[Kota] — Sebelum Berangkat"**, dirender sebagai satu kotak — tiap sub-judul di dalamnya 1-2 kalimat padat (cari via web_search kalau belum tahu, tapi ringkas ke inti): Cerita Kota, Cuaca/Iklim/Suhu (tandai ⚠️ kalau rata-rata historis bukan forecast), Transportasi Masuk Kota, Area Menginap yang Disarankan (nama KAWASAN saja, bukan nama hotel spesifik — user cari sendiri), Destinasi Terkenal Lain, Makanan Wajib Dikunjungi & Dicoba (naratif saja, bukan rekomendasi "boleh dimakan" — rekomendasi makan aktual tetap ikut poin 2), Hal yang Sebaiknya Dihindari, Yang Perlu Disiapkan.
- Di bawah tiap sub-bagian Hari X: tempat utama DIIKUTI Plan-B hari itu (satu grup, bukan dipisah).
- Di akhir: sub-bagian **"Cadangan"** untuk Plan C.
- **Satu entri `###` = SATU tempat**, jangan gabung 2 nama dalam 1 judul (tombol copy-nama di Wisata.html cuma ambil 1 nama kalau digabung).
- **Setiap entri WAJIB, tanpa kecuali (termasuk Cadangan):**
  - Nama tempat. **China:** `Nama Inggris (Hanzi · Pīnyīn dengan tanda nada)` — Hanzi diverifikasi via Amap kalau bisa (✅), kalau tidak pakai sumber lain + tandai ⚠️. **Pinyin WAJIB tiap ada Hanzi** (termasuk Hong Kong — tujuannya bantu pembaca Mandarin, bukan klaim lafal Kanton lokal; kalau namanya murni istilah/lafal Kanton tanpa bacaan Mandarin wajar, baru boleh tanpa pinyin). Pinyin pakai diakritik nada (ā á ǎ à), bukan angka, ambil dari sumber yang sama dengan Hanzi — hati-hati karakter polifon. **Bukan China:** pakai `places_search` (Google Places), tidak perlu tanda ⚠️.
  - Uraian sejarah/cerita 2-5 kalimat (1-2 kalimat kalau di "Sebelum Berangkat").
  - **`**Akses:**` → `**Jam Operasional:**` → `**Tiket:**`, dalam urutan ini, SEBELUM `**Cara reservasi:**`/`**Kenapa...**`/`**Terkait:**`** (parser berhenti baca di bold marker pertama). WAJIB semua, termasuk entri Cadangan — cari via web_search, jangan kosong/tebak.
  - Plan-B: kalimat "Kenapa jadi Plan-B" eksplisit. Cadangan: kalimat "Kenapa tidak dimasukkan" eksplisit.
  - Cadangan yang genuinely searah rute salah satu hari → tambah `**Terkait:** Hari N` (nampil sebagai info tambahan di bawah Plan-B hari itu di Wisata.html).
  - Judul entri Plan-B: emoji 🏷️ + akhiran `— Plan-B Hari N (alasan singkat)`.
  - Link foto (Wikipedia/sumber resmi) + link video (`youtube.com/results?search_query=...`).
  - Opsional: `- Rekomendasi tempat sekitar: a; b; c` — nama pakai aturan sama seperti destinasi utama, JANGAN jadi link URL, tidak perlu tombol copy.

PDF: reportlab (Python) kecuali diminta lain. **Catatan scope:** revisi penamaan Amap/Pinyin di atas HANYA berlaku Lampiran — tabel itinerary harian (poin 10) format lama.

## 12. Setelah membuat itinerary

Kalau user sebut tempat baru yang dikunjungi setelah trip, tawarkan tambah ke `references/visited-places.md`.

## 13. Mode Itinerary Kustom (revisi dadakan)

Untuk **jendela waktu tertentu** (bukan hari penuh) dari **destinasi pilihan manual** — bisa dari itinerary yang sudah ada dan/atau destinasi baru.

**Trigger:** "cust <kota>", "revisi <kota> C1", "buat <kota> C2" — cek dulu file `<Kota> C*.md` yang ada untuk tahu maksudnya edit yang sudah ada atau bikin baru.

**Konfirmasi dulu kalau belum jelas:** tanggal revisi, jam mulai-selesai, daftar destinasi (+ file/kota asal, tandai "baru" kalau benar-benar baru), tempat yang sudah dikunjungi/sengaja dilewatkan.

**Proses:**
1. Destinasi dari file existing → baca file asli dulu, pakai ulang Akses/Jam/Tiket/cerita yang sudah ada.
2. Destinasi baru → riset dari nol (web_search/image_search), ikuti poin 1-9. **Setelah riset, tambahkan JUGA entrinya ke Cadangan file itinerary ASLI kota tsb** (bukan cuma file custom) — supaya tersimpan permanen utk dipakai ulang. Skip kalau destinasi ini murni tanpa file kota asal.
3. Cek hari/jam operasional tiap destinasi terhadap jendela waktu — kalau tutup, flag jelas + tawarkan alternatif.
4. Urutkan searah/berdekatan & realistis muat waktu — kalau tidak semua muat, sebutkan eksplisit mana yang dikorbankan.
5. Format sama seperti reguler: tabel `Jam|Kegiatan|Catatan|<mata uang>|IDR`, TOTAL HARI, Plan-B wajib.
6. Lampiran destinasi TERPILIH tetap wajib format lengkap (Akses/Jam/Tiket).
7. **Cadangan & "Sudah Dikunjungi/Dilewatkan" — DEFAULT OFF**, hanya kalau diminta eksplisit (generate ulang Lampiran kota asal lengkap makan waktu lama, sering tidak perlu untuk revisi jendela pendek). Kalau diminta: Cadangan = semua entri kota asal yang TIDAK terpilih; sub-kelompok "Sudah Dikunjungi/Dilewatkan" ditandai **baris bold biasa** (`**— Sudah Dikunjungi/Dilewatkan —**`), BUKAN heading `###` (jadi entri Lampiran kosong kalau `###` — bug parser).

**Penamaan file:** `<nomor file asli> <Kota> C<Angka>.md` (cek nomor berikutnya dari file `C*` yang sudah ada). Destinasi murni baru: nomor unik yang tidak bentrok.

**Beda dari reguler:** Informasi Penerbangan/Hotel boleh diskip kalau tidak relevan. Blockquote Master file diganti: `> Revisi custom dari "<file asli>.md" — <tanggal>, jam <mulai>–<selesai>.`

Setelah simpan, jalankan `py generate_wisata.py <negara>` (dari `wisata/HTML-Wisata/`) supaya Wisata.html ikut update.
