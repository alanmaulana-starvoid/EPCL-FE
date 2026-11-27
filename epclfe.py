#!/usr/bin/env python3
"""
EPCL-FE v1.0 (Easy Programming Code Language - For Education)
Interpreter & Transpiler berbasis Python dengan 106 perintah bahasa sehari-hari.
"""

import sys
import os
import re
import math
import random
import time
import platform
from datetime import datetime

VERSION = "1.0.0"

# ==============================================================================
# KAMUS 106 CODE COMMAND EPCL-FE v1.0
# Format: "perintah_epcl": ("target_python", "kategori", "deskripsi", is_callable)
# ==============================================================================
COMMANDS = {
    # 1. Perintah Sistem & Bantuan (6)
    "/bantu-listkode": ("_epcl_bantu_listkode()", "Sistem", "Menampilkan seluruh daftar code command EPCL-FE", False),
    "/info-epcl": ("_epcl_info()", "Sistem", "Menampilkan informasi versi EPCL-FE", False),
    "/bersihkan": ("_epcl_bersihkan()", "Sistem", "Membersihkan layar terminal", False),
    "/keluar": ("sys.exit(0)", "Sistem", "Menghentikan dan keluar dari program", False),
    "/waktu-sekarang": ("_epcl_waktu_sekarang()", "Sistem", "Menampilkan tanggal dan jam saat ini", False),
    "/sistem-os": ("_epcl_sistem_os()", "Sistem", "Menampilkan informasi sistem operasi", False),

    # 2. Input & Output Dasar (8)
    "cetak": ("print", "Input/Output", "Menampilkan teks atau nilai ke layar", True),
    "tanya": ("input", "Input/Output", "Meminta masukan teks dari pengguna", True),
    "tanya_angka": ("_epcl_tanya_angka", "Input/Output", "Meminta masukan bilangan bulat dari pengguna", True),
    "tanya_desimal": ("_epcl_tanya_desimal", "Input/Output", "Meminta masukan bilangan desimal dari pengguna", True),
    "cetak_baris": ("_epcl_cetak_baris", "Input/Output", "Mencetak garis pemisah horizontal", True),
    "cetak_kosong": ("print", "Input/Output", "Mencetak baris kosong", True),
    "cetak_sukses": ("_epcl_cetak_sukses", "Input/Output", "Mencetak pesan berlabel [SUKSES]", True),
    "cetak_gagal": ("_epcl_cetak_gagal", "Input/Output", "Mencetak pesan berlabel [GAGAL]", True),

    # 3. Logika, Percabangan & Perulangan (17)
    "jika": ("if", "Logika & Loop", "Memulai percabangan kondisi (if)", False),
    "atau_jika": ("elif", "Logika & Loop", "Cabang kondisi alternatif (elif)", False),
    "selain_itu": ("else", "Logika & Loop", "Cabang terakhir jika kondisi tidak terpenuhi (else)", False),
    "ulangi_selama": ("while", "Logika & Loop", "Perulangan selama kondisi bernilai benar (while)", False),
    "untuk_setiap": ("for", "Logika & Loop", "Perulangan untuk setiap elemen (for)", False),
    "dalam": ("in", "Logika & Loop", "Operator keanggotaan dalam urutan/daftar (in)", False),
    "rentang": ("range", "Logika & Loop", "Membuat deret angka berurutan (range)", True),
    "berhenti": ("break", "Logika & Loop", "Menghentikan perulangan secara paksa (break)", False),
    "lewati": ("continue", "Logika & Loop", "Melompati iterasi saat ini ke iterasi berikutnya", False),
    "diam": ("pass", "Logika & Loop", "Pernyataan kosong tanpa aksi (pass)", False),
    "dan": ("and", "Logika & Loop", "Operator logika DAN (and)", False),
    "atau": ("or", "Logika & Loop", "Operator logika ATAU (or)", False),
    "bukan": ("not", "Logika & Loop", "Operator negasi/kebalikan logika (not)", False),
    "adalah": ("is", "Logika & Loop", "Memeriksa identitas objek yang sama (is)", False),
    "benar": ("True", "Logika & Loop", "Nilai logika benar (True)", False),
    "salah": ("False", "Logika & Loop", "Nilai logika salah (False)", False),
    "kosong": ("None", "Logika & Loop", "Nilai hampa / tidak ada data (None)", False),

    # 4. Fungsi, Kelas & Penanganan Error (14)
    "buat_fungsi": ("def", "Fungsi & OOP", "Mendefinisikan fungsi baru (def)", False),
    "kembalikan": ("return", "Fungsi & OOP", "Mengembalikan nilai hasil dari fungsi (return)", False),
    "fungsi_singkat": ("lambda", "Fungsi & OOP", "Membuat fungsi anonim satu baris (lambda)", False),
    "variabel_global": ("global", "Fungsi & OOP", "Mengakses variabel global di dalam fungsi", False),
    "buat_kelas": ("class", "Fungsi & OOP", "Mendefinisikan cetak biru objek/kelas (class)", False),
    "diri": ("self", "Fungsi & OOP", "Referensi ke objek itu sendiri di dalam kelas (self)", False),
    "coba": ("try", "Fungsi & OOP", "Mencoba menjalankan blok kode rawan error (try)", False),
    "jika_error": ("except", "Fungsi & OOP", "Menangani error yang terjadi pada blok coba", False),
    "akhirnya": ("finally", "Fungsi & OOP", "Blok yang selalu dijalankan di akhir coba/jika_error", False),
    "picu_error": ("raise", "Fungsi & OOP", "Memunculkan pesan error secara manual (raise)", False),
    "pastikan": ("assert", "Fungsi & OOP", "Memastikan kondisi benar saat pengujian (assert)", False),
    "pakai_modul": ("import", "Fungsi & OOP", "Mengimpor pustaka/modul eksternal (import)", False),
    "dari_modul": ("from", "Fungsi & OOP", "Memilih bagian tertentu dari modul (from)", False),
    "sebagai": ("as", "Fungsi & OOP", "Memberi nama alias pada modul/error (as)", False),

    # 5. Tipe Data & Konversi (11)
    "ke_teks": ("str", "Tipe Data", "Mengubah nilai menjadi teks/string (str)", True),
    "ke_bulat": ("int", "Tipe Data", "Mengubah nilai menjadi bilangan bulat (int)", True),
    "ke_desimal": ("float", "Tipe Data", "Mengubah nilai menjadi bilangan desimal (float)", True),
    "ke_logika": ("bool", "Tipe Data", "Mengubah nilai menjadi True/False (bool)", True),
    "ke_daftar": ("list", "Tipe Data", "Mengubah data menjadi daftar/list", True),
    "ke_kamus": ("dict", "Tipe Data", "Membuat atau mengubah menjadi kamus/dict", True),
    "ke_himpunan": ("set", "Tipe Data", "Membuat himpunan unik tanpa duplikat (set)", True),
    "ke_tuple": ("tuple", "Tipe Data", "Membuat daftar tetap yang tidak bisa diubah (tuple)", True),
    "cek_tipe": ("type", "Tipe Data", "Mengetahui jenis tipe data suatu variabel", True),
    "apakah_tipe": ("isinstance", "Tipe Data", "Mengecek apakah variabel bertipe tertentu", True),
    "panjang": ("len", "Tipe Data", "Menghitung jumlah karakter atau anggota daftar", True),

    # 6. Matematika & Angka (16)
    "jumlahkan": ("sum", "Matematika", "Menjumlahkan seluruh angka di dalam daftar", True),
    "terbesar": ("max", "Matematika", "Mencari nilai paling besar", True),
    "terkecil": ("min", "Matematika", "Mencari nilai paling kecil", True),
    "bulatkan": ("round", "Matematika", "Membulatkan angka desimal terdekat", True),
    "nilai_mutlak": ("abs", "Matematika", "Mengubah angka negatif menjadi positif (absolut)", True),
    "pangkat": ("pow", "Matematika", "Menghitung perpangkatan angka (x pangkat y)", True),
    "akar_kuadrat": ("math.sqrt", "Matematika", "Menghitung akar kuadrat suatu bilangan", True),
    "pembulatan_atas": ("math.ceil", "Matematika", "Membulatkan angka desimal ke atas", True),
    "pembulatan_bawah": ("math.floor", "Matematika", "Membulatkan angka desimal ke bawah", True),
    "nilai_pi": ("math.pi", "Matematika", "Konstanta matematika Pi (3.14159...)", False),
    "sinus": ("math.sin", "Matematika", "Menghitung nilai sinus (radian)", True),
    "kosinus": ("math.cos", "Matematika", "Menghitung nilai kosinus (radian)", True),
    "tangen": ("math.tan", "Matematika", "Menghitung nilai tangen (radian)", True),
    "logaritma": ("math.log10", "Matematika", "Menghitung logaritma basis 10", True),
    "faktorial": ("math.factorial", "Matematika", "Menghitung nilai faktorial bilangan bulat", True),
    "sisa_bagi": ("math.fmod", "Matematika", "Menghitung sisa pembagian desimal", True),

    # 7. Pengolahan Teks / String (12)
    "huruf_besar": ("_epcl_huruf_besar", "Teks/String", "Mengubah semua huruf menjadi KAPITAL", True),
    "huruf_kecil": ("_epcl_huruf_kecil", "Teks/String", "Mengubah semua huruf menjadi huruf kecil", True),
    "huruf_kapital": ("_epcl_huruf_kapital", "Teks/String", "Mengubah huruf awal setiap kata menjadi kapital", True),
    "hapus_spasi": ("_epcl_hapus_spasi", "Teks/String", "Menghapus spasi berlebih di awal dan akhir teks", True),
    "ganti_teks": ("_epcl_ganti_teks", "Teks/String", "Mengganti bagian teks lama dengan teks baru", True),
    "pecah_teks": ("_epcl_pecah_teks", "Teks/String", "Memecah teks menjadi daftar berdasarkan pemisah", True),
    "gabung_teks": ("_epcl_gabung_teks", "Teks/String", "Menggabungkan daftar teks dengan pemisah", True),
    "cek_awalan": ("_epcl_cek_awalan", "Teks/String", "Mengecek apakah teks diawali kata tertentu", True),
    "cek_akhiran": ("_epcl_cek_akhiran", "Teks/String", "Mengecek apakah teks diakhiri kata tertentu", True),
    "hitung_kata": ("_epcl_hitung_kata", "Teks/String", "Menghitung kemunculan kata dalam teks", True),
    "balik_teks": ("_epcl_balik_teks", "Teks/String", "Membalik urutan karakter pada teks", True),
    "apakah_angka": ("_epcl_apakah_angka", "Teks/String", "Mengecek apakah teks hanya berisi digit angka", True),

    # 8. Manipulasi Daftar / List (11)
    "tambah_item": ("_epcl_tambah_item", "Daftar/List", "Menambahkan elemen baru ke akhir daftar", True),
    "sisipkan_item": ("_epcl_sisipkan_item", "Daftar/List", "Menyisipkan elemen pada indeks tertentu", True),
    "hapus_item": ("_epcl_hapus_item", "Daftar/List", "Menghapus elemen tertentu dari daftar", True),
    "ambil_terakhir": ("_epcl_ambil_terakhir", "Daftar/List", "Mengambil dan menghapus elemen terakhir daftar", True),
    "urutkan": ("sorted", "Daftar/List", "Mengurutkan isi daftar dari kecil ke besar", True),
    "balik_urutan": ("_epcl_balik_urutan", "Daftar/List", "Membalik urutan elemen dalam daftar", True),
    "hapus_semua": ("_epcl_hapus_semua", "Daftar/List", "Mengosongkan seluruh isi daftar", True),
    "nomor_urut": ("enumerate", "Daftar/List", "Memberi nomor indeks pada setiap elemen daftar", True),
    "pasangkan": ("zip", "Daftar/List", "Menggabungkan dua daftar secara berpasangan", True),
    "semua_benar": ("all", "Daftar/List", "Benar jika semua elemen dalam daftar bernilai benar", True),
    "ada_yang_benar": ("any", "Daftar/List", "Benar jika minimal ada satu elemen bernilai benar", True),

    # 9. Acak, Waktu & Berkas/File (11)
    "angka_acak": ("random.randint", "Acak & File", "Menghasilkan angka bulat acak dalam rentang (a, b)", True),
    "pilih_acak": ("random.choice", "Acak & File", "Memilih satu elemen secara acak dari daftar", True),
    "acak_daftar": ("_epcl_acak_daftar", "Acak & File", "Mengacak posisi seluruh elemen dalam daftar", True),
    "desimal_acak": ("random.random", "Acak & File", "Menghasilkan angka desimal acak antara 0 dan 1", True),
    "tunggu_detik": ("time.sleep", "Acak & File", "Menjeda jalannya program selama N detik", True),
    "detik_epoch": ("time.time", "Acak & File", "Mengambil waktu sistem dalam satuan detik", True),
    "baca_file": ("_epcl_baca_file", "Acak & File", "Membaca seluruh isi teks dari sebuah file", True),
    "tulis_file": ("_epcl_tulis_file", "Acak & File", "Menulis teks baru ke file (menimpa isi lama)", True),
    "tambah_isi_file": ("_epcl_tambah_isi_file", "Acak & File", "Menambahkan teks baru ke baris akhir file", True),
    "cek_file_ada": ("os.path.exists", "Acak & File", "Mengecek apakah file atau folder tersedia", True),
    "hapus_file": ("os.remove", "Acak & File", "Menghapus file dari penyimpanan", True),
}

CALLABLE_NAMES = {k for k, v in COMMANDS.items() if v[3]}
SLASH_COMMANDS = {k: v[0] for k, v in COMMANDS.items() if k.startswith("/")}
WORD_COMMANDS = {k: v[0] for k, v in COMMANDS.items() if not k.startswith("/")}

# ==============================================================================
# FUNGSI RUNTIME PENDUKUNG EPCL-FE
# ==============================================================================
def _epcl_bantu_listkode():
    print("=" * 72)
    print(f"  DAFTAR CODE COMMAND EPCL-FE v{VERSION} (Total: {len(COMMANDS)} Perintah)")
    print("  Tips: Fungsi bertanda [()] bisa ditulis cetak('hi') atau cetak='hi'")
    print("=" * 72)
    kategori_grup = {}
    for cmd, (_, kat, desc, is_call) in COMMANDS.items():
        kategori_grup.setdefault(kat, []).append((cmd, desc, is_call))
    nomor = 1
    for kat, items in kategori_grup.items():
        print(f"\n[{kat.upper()}]")
        for cmd, desc, is_call in items:
            tanda = "()" if is_call else ""
            print(f"  {nomor:03d}. {cmd + tanda:<22} -> {desc}")
            nomor += 1
    print("=" * 72)

def _epcl_info():
    print(f"EPCL-FE (Easy Programming Code Language - For Education) versi {VERSION}")
    print(f"Total perintah aktif: {len(COMMANDS)} | Mesin: Python {platform.python_version()}")

def _epcl_bersihkan():
    os.system("cls" if os.name == "nt" else "clear")

def _epcl_waktu_sekarang():
    sekarang = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(f"Waktu saat ini: {sekarang}")
    return sekarang

def _epcl_sistem_os():
    info = f"{platform.system()} {platform.release()}"
    print(f"Sistem Operasi: {info}")
    return info

def _epcl_tanya_angka(pesan=""):
    return int(input(pesan))

def _epcl_tanya_desimal(pesan=""):
    return float(input(pesan))

def _epcl_cetak_baris(karakter="-", panjang_garis=40):
    print(str(karakter) * int(panjang_garis))

def _epcl_cetak_sukses(pesan):
    print(f"[SUKSES] {pesan}")

def _epcl_cetak_gagal(pesan):
    print(f"[GAGAL] {pesan}")

def _epcl_huruf_besar(teks): return str(teks).upper()
def _epcl_huruf_kecil(teks): return str(teks).lower()
def _epcl_huruf_kapital(teks): return str(teks).title()
def _epcl_hapus_spasi(teks): return str(teks).strip()
def _epcl_ganti_teks(teks, lama, baru): return str(teks).replace(str(lama), str(baru))
def _epcl_pecah_teks(teks, pemisah=" "): return str(teks).split(pemisah)
def _epcl_gabung_teks(pemisah, daftar): return str(pemisah).join(str(x) for x in daftar)
def _epcl_cek_awalan(teks, awal): return str(teks).startswith(str(awal))
def _epcl_cek_akhiran(teks, akhir): return str(teks).endswith(str(akhir))
def _epcl_hitung_kata(teks, cari): return str(teks).count(str(cari))
def _epcl_balik_teks(teks): return str(teks)[::-1]
def _epcl_apakah_angka(teks): return str(teks).isdigit()

def _epcl_tambah_item(daftar, item): daftar.append(item); return daftar
def _epcl_sisipkan_item(daftar, idx, item): daftar.insert(idx, item); return daftar
def _epcl_hapus_item(daftar, item): daftar.remove(item); return daftar
def _epcl_ambil_terakhir(daftar): return daftar.pop()
def _epcl_balik_urutan(daftar): return list(reversed(daftar))
def _epcl_hapus_semua(daftar): daftar.clear(); return daftar
def _epcl_acak_daftar(daftar): random.shuffle(daftar); return daftar

def _epcl_baca_file(nama):
    with open(nama, "r", encoding="utf-8") as f:
        return f.read()

def _epcl_tulis_file(nama, isi):
    with open(nama, "w", encoding="utf-8") as f:
        f.write(str(isi))

def _epcl_tambah_isi_file(nama, isi):
    with open(nama, "a", encoding="utf-8") as f:
        f.write(str(isi))

# ==============================================================================
# TRANSPILER EPCL-FE -> PYTHON
# ==============================================================================
TOKEN_SPLIT_RE = re.compile(r'("""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'|"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|#.*)')
ASSIGN_CALL_RE = re.compile(r'(?<![=!<>])\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=(?!=)\s*(.+)$')
WORD_RE = re.compile(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b')

def _transform_shorthand_equals(code_chunk):
    """Mengubah sintaks perintah=argumen menjadi perintah(argumen) di luar string."""
    match = ASSIGN_CALL_RE.search(code_chunk)
    if not match:
        return code_chunk
    prefix = code_chunk[:match.start()]
    cmd_name = match.group(1)
    rhs = _transform_shorthand_equals(match.group(2).strip())
    if cmd_name in CALLABLE_NAMES:
        return f"{prefix}{cmd_name}({rhs})"
    return f"{prefix}{cmd_name} = {rhs}"

def transpile_line(line):
    stripped = line.lstrip()
    indent = line[:len(line) - len(stripped)]

    # Cek slash command di awal baris (misal: /bantu-listkode)
    for scmd, py_call in SLASH_COMMANDS.items():
        if stripped == scmd or stripped.startswith(scmd + " ") or stripped.startswith(scmd + "#"):
            sisa = stripped[len(scmd):]
            return f"{indent}{py_call}{sisa}"

    # Pisahkan kode dari string literal & komentar agar isi teks aman
    parts = TOKEN_SPLIT_RE.split(line)
    for i in range(0, len(parts), 2):
        chunk = parts[i]
        if not chunk:
            continue
        chunk = _transform_shorthand_equals(chunk)
        chunk = WORD_RE.sub(lambda m: WORD_COMMANDS.get(m.group(1), m.group(1)), chunk)
        parts[i] = chunk
    return "".join(parts)

def transpile_source(source):
    return "\n".join(transpile_line(line) for line in source.splitlines())

def build_env():
    env = {"__name__": "__main__", "math": math, "random": random, "time": time, "os": os, "sys": sys}
    for name, val in globals().items():
        if name.startswith("_epcl_"):
            env[name] = val
    return env

def run_file(filepath):
    if not os.path.exists(filepath):
        print(f"[ERROR] File '{filepath}' tidak ditemukan.")
        sys.exit(1)
    with open(filepath, "r", encoding="utf-8") as f:
        epcl_code = f.read()
    py_code = transpile_source(epcl_code)
    exec(compile(py_code, filepath, "exec"), build_env())

def run_repl():
    print(f"EPCL-FE v{VERSION} Interactive Mode — Ketik /bantu-listkode atau /keluar")
    env = build_env()
    while True:
        try:
            line = input("epcl> ")
            if not line.strip():
                continue
            py_code = transpile_source(line)
            exec(compile(py_code, "<epcl-repl>", "exec"), env)
        except KeyboardInterrupt:
            print("\nKeluar dari EPCL-FE.")
            break
        except Exception as e:
            print(f"[Kesalahan EPCL-FE] {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_file(sys.argv[1])
    else:
        run_repl()
