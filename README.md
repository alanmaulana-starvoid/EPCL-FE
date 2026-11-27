# EPCL-FE v1.0 (Easy Programming Code Language - For Education)

**EPCL-FE** adalah bahasa pemrograman edukasi berbasis Python yang dirancang khusus untuk pelajar sekolah menengah agar dapat memahami logika pemrograman menggunakan kosakata bahasa Indonesia sehari-hari.

---

## Fitur Utama
* **106 Perintah Bahasa Indonesia:** Mencakup input/output, percabangan, perulangan, matematika, pengolahan teks, manipulasi daftar, hingga manajemen file.
* **Sintaks Ganda (Dual-Syntax):** Mendukung gaya pemanggilan fungsi standar `cetak("Halo")` maupun gaya pintasan sederhana `cetak="Halo"`.
* **Mode Interaktif (REPL) & Mode File:** Dapat dijalankan baris demi baris untuk demonstrasi langsung di kelas maupun disimpan sebagai file tugas berekstensi `.epcl`.
* **Ringan & Tanpa Instalasi Eksternal:** Hanya membutuhkan Python 3 bawaan tanpa library tambahan.

---

## Panduan Penggunaan untuk Guru & Siswa

### 1. Komputer Lab Sekolah (Windows)
1. Klik tombol **Code** $\rightarrow$ **Download ZIP**, lalu ekstrak folder `EPCL-FE`.
2. Pastikan **Python 3** sudah terinstal di komputer.
3. Klik ganda file **`jalankan_epcl.bat`** untuk langsung masuk ke mode interaktif (`epcl>`), atau buka Command Prompt (CMD) di dalam folder dan ketik:
   ```cmd
   python epcl.py materi/01_halo_dunia.epcl
   ```
---

### 2. Tanpa Instalasi via Browser (Chromebook / PC Terkunci)
1. Buka halaman repositori GitHub ini di browser.
2. Tekan tombol titik (.) di keyboard atau pilih Code lalu pilih Codespaces dan tekan Create codespace on main.
3. Jalankan interpreter melalui terminal bawaan browser dengan perintah python epcl.py.

### 3. Smartphone Android (Termux / Pydroid 3)
Jalankan perintah berikut di terminal Termux:
```bash
git clone https://github.com/alanmaulana-starvoid/EPCL-FE.git
cd EPCL-FE
bash setup.sh
```
## Daftar Perintah Sistem Bawaan
Ketik perintah berikut langsung di dalam mode interaktif (epcl>) atau di dalam file .epcl:
Perintah dan Fungsi:
/bantu-listkode untuk Menampilkan daftar lengkap seluruh 106 code command EPCL-FE
/info-epcl untuk Menampilkan versi EPCL-FE dan versi Python yang digunakan
/bersihkan untuk Membersihkan layar terminal
/waktu-sekarang untuk Menampilkan tanggal dan waktu sistem saat ini
/sistem-os untuk Menampilkan informasi sistem operasi perangkat
/keluar untuk Keluar dari mode interaktif EPCL-FE
## Struktur Modul Latihan (materi/)
01_halo_dunia.epcl — Pengenalan output, input teks, dan variabel.
02_kalkulator.epcl — Operasi aritmatika dan pembulatan angka.
03_cek_kelulusan.epcl — Logika percabangan (jika, atau_jika, selain_itu).
04_tebak_angka.epcl — Permainan interaktif menggunakan perulangan (ulangi_selama) dan angka acak.
