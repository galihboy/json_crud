import json

with open("barang.json", "r") as f:
    barang = json.load(f)

# Cari data barang dengan kode 5
for item in barang:
    if item["kode"] == 5:
        # Ubah nama dan harga
        item["nama"] = "Buku Tulis"
        item["harga"] = 15000

# Simpan data barang yang telah diubah
with open("barang.json", "w") as f:
    json.dump(barang, f)

# Cetak daftar barang
print(barang)
