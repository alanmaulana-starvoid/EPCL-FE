#!/usr/bin/env bash
# Script Instalasi & Konfigurasi EPCL-FE v1.0 (Termux / Linux)

echo "=========================================="
echo "  Menyiapkan EPCL-FE v1.0..."
echo "=========================================="

# 1. Cek instalasi Python
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "[INFO] Python belum terpasang. Memasang Python..."
    if command -v pkg &> /dev/null; then
        pkg update -y && pkg install python -y
    elif command -v apt &> /dev/null; then
        sudo apt update && sudo apt install python3 -y
    else
        echo "[ERROR] Harap instal Python 3 secara manual terlebih dahulu."
        exit 1
    fi
fi

# Tentukan perintah python yang tersedia
PY_CMD="python3"
if command -v python &> /dev/null; then
    PY_CMD="python"
fi

# 2. Beri izin eksekusi pada epcl.py
chmod +x epcl.py

# 3. Tambahkan alias 'epcl' ke ~/.bashrc jika belum ada
REPO_DIR="$(pwd)"
ALIAS_LINE="alias epcl='$PY_CMD $REPO_DIR/epcl.py'"

if [ -f "$HOME/.bashrc" ]; then
    if ! grep -q "alias epcl=" "$HOME/.bashrc"; then
        echo "" >> "$HOME/.bashrc"
        echo "# Pintasan EPCL-FE v1.0" >> "$HOME/.bashrc"
        echo "$ALIAS_LINE" >> "$HOME/.bashrc"
        echo "[SUKSES] Pintasan 'epcl' berhasil ditambahkan ke ~/.bashrc"
    fi
else
    echo "$ALIAS_LINE" > "$HOME/.bashrc"
    echo "[SUKSES] File ~/.bashrc dibuat dengan pintasan 'epcl'"
fi

echo "=========================================="
echo "  Setup Selesai!"
echo "  Cara menjalankan:"
echo "  1. Mode Interaktif : $PY_CMD epcl.py"
echo "  2. Jalankan Materi : $PY_CMD epcl.py materi/01_halo_dunia.epcl"
echo "  (Buka ulang terminal untuk memakai perintah singkat 'epcl')"
echo "=========================================="
