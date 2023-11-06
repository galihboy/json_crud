import json

with open("barang.json", "r") as f:
    barang = json.load(f)

# Tambahkan data barang baru
barang.append({
    "kode": 5,
    "nama": "Buku",
    "harga": 10000
})

# Simpan data barang yang telah diubah
with open("barang.json", "w") as f:
    json.dump(barang, f)