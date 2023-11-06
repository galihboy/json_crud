import json

with open("barang.json", "r") as f:
    barang = json.load(f)

# Cari data barang dengan kode 5
for item in barang:
    if item["kode"] == 5:
        # Hapus data barang
        barang.remove(item)

# Simpan data barang yang telah dihapus
with open("barang.json", "w") as f:
    json.dump(barang, f)

# Cetak daftar barang
print(barang)
