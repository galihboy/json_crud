import json

with open("barang.json", "r") as f:
    barang = json.load(f)

# Tampilan standar
print(barang)

# Tampilan yang lebih rapi/cantik dengan indentasi 4
print(json.dumps(barang, indent=4))

# Cari semua barang dengan harga di atas 2000
barang_mahal = []
for item in barang:
    if item["harga"] >= 2000:
        barang_mahal.append(item)

# Cetak daftar barang mahal
#print(barang_mahal)
print(json.dumps(barang_mahal, indent=4))
