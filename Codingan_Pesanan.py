import pandas as pd
from datetime import datetime

# Baca data Excel yang sudah ada
file_path = r"E:\Berkas Kuliah\SEMESTER 5\Mata Kuliah\Kompnon\Pesanan.xlsx"
df_existing = pd.read_excel(file_path)

# Mendapatkan tanggal hari ini dan waktu sekarang
tanggal_hari_ini = datetime.now().strftime("%Y-%m-%d")
waktu_sekarang = datetime.now().strftime("%H:%M:%S")

# Menu dan harga
menu = {
    "nasi goreng": 10,
    "mie goreng": 10,
    "es teh": 5,
}

pesanan = []
harga = 0
remover = []

print("======= Menu Hari Esok =======")
for key, value in menu.items():
    remover.append(f'-{key}')
    print(f"{key:15}: ${value}")

# Input nama dan pesanan
name = input("Input Nama Anda: ")
makanan = ''
while makanan != "s":
    makanan = input("Silahkan input pesanan anda (s jika selesai): ").lower()
    if makanan == "s":
        break
    elif menu.get(makanan) is not None:
        pesanan.append(makanan)
    elif makanan in remover:
        pesanan.remove(makanan[1:])
    else:
        print("Menu tidak tersedia")

# Hitung jumlah pesanan dan total harga
count_dict = {"nasi goreng": 0, "mie goreng": 0, "es teh": 0}
for item in pesanan:
    count_dict[item] += 1
    harga += menu.get(item)

# Tampilkan nota
print("\n============ Nota Hari Esok ============")
print('-----------------------------------------')
for item in count_dict:
    if count_dict[item] > 0:
        print(f'{item:15}: {count_dict[item]} x ${menu.get(item):3}:  ${count_dict[item] * menu.get(item)}')
print('-----------------------------------------')
print(f'{" ":13} {" HARGA JUAL":3}: ${harga}')
print('-----------------------------------------')
print(f'{" ":19} {"TOTAL":3}: ${harga}')

# Data baru yang ingin ditambahkan
data_baru = pd.DataFrame({
    'Tanggal': [tanggal_hari_ini] * len(count_dict),
    'Waktu': [waktu_sekarang] * len(count_dict),
    'Nama': [name] * len(count_dict),
    'Pesanan': list(count_dict.keys()),
    'Qty': list(count_dict.values()),
    'Biaya': [menu[item] for item in count_dict],
    'Total': [count_dict[item] * menu[item] for item in count_dict]
})
data_baru = data_baru[data_baru['Qty'] > 0]

# Gabungkan data lama dengan data baru
df_final = pd.concat([df_existing, data_baru], ignore_index=True)

# Export data ke file Excel
output_file = file_path  
df_final.to_excel(output_file, index=False)

print(f"Data berhasil diekspor ke {output_file}!")

print("============================================================")

print('Berikut merupakan tipe data dari dataset tersebut:')
print(df_final.dtypes)

