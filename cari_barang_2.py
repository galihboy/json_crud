import json

with open("barang.json", "r") as f:
    barang = json.load(f)

# Cari barang yang namanya mengandung huruf/kata "peng" (tanpa memperhatikan huruf besar atau kecil)
barang_cari = []
kataCari = "peng"

for item in barang:
    if kataCari.lower() in item["nama"].lower():
        barang_cari.append(item)

# Cetak daftar barang pensil
#print(barang_cari)
print(json.dumps(barang_cari, indent=4))
