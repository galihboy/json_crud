import json

with open("barang.json", "r") as f:
    barang = json.load(f)

# Cari barang dengan kode 1
for item in barang:
    if item["kode"] == 2:
        print(item)

# Cari barang dengan nama "Pensil"
for item in barang:
    if item["nama"] == "Pensil":
        print(item)

# Cari barang yang namanya mengandung huruf/kata "p"
barang_cari = []
kataCari = "p"
for item in barang:
    if kataCari in item["nama"]:
        barang_cari.append(item)

# Cetak daftar barang pensil
print(barang_cari)