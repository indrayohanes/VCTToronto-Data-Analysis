# Import library yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Atur gaya visualisasi agar lebih menarik
sns.set_style('whitegrid')

# Muat file CSV ke dalam sebuah DataFrame Pandas
# Pastikan file 'vct toronto.csv' ada di folder yang sama dengan notebook-mu
df = pd.read_csv('vct toronto.csv')

# Tampilkan 5 baris pertama data
print("5 Baris Pertama Data:")
print(df.head())

# Lihat informasi umum tentang data (tipe data, kolom, nilai non-null)
print("\nInformasi DataFrame:")
df.info()

# Cek apakah ada data yang hilang (missing values)
print("\nJumlah Data yang Hilang per Kolom:")
print(df.isnull().sum())

# Menghindari pembagian dengan nol jika ada pemain yang Deaths-nya 0
df['KDA Ratio'] = (df['K'] + df['A']) / df['D'].replace(0, 1)

print("\nData dengan kolom KDA Ratio baru:")
print(df.head())

# Kelompokkan data berdasarkan pemain, hitung rata-rata ACS, lalu urutkan
top_10_players_acs = df.groupby('Player')['ACS'].mean().sort_values(ascending=False).head(10)

print("Top 10 Pemain Berdasarkan Rata-rata ACS:")
print(top_10_players_acs)

# Visualisasikan dalam bentuk bar chart
plt.figure(figsize=(12, 7)) # Mengatur ukuran gambar
sns.barplot(x=top_10_players_acs.values, y=top_10_players_acs.index, palette='viridis')
plt.title('Top 10 Pemain VCT Toronto Berdasarkan Rata-Rata ACS', fontsize=16)
plt.xlabel('Rata-Rata Average Combat Score (ACS)', fontsize=12)
plt.ylabel('Pemain', fontsize=12)
plt.show() # Tampilkan grafiknya

# Hitung frekuensi setiap agent
role_picks = df['Role'].value_counts()

print("Jumlah Pemilihan Agent Selama Turnamen:")
print(role_picks)

# Visualisasikan
plt.figure(figsize=(14, 8))
sns.barplot(x=role_picks.index, y=role_picks.values, palette='mako')
plt.title('Popularitas Role di VCT Toronto', fontsize=16)
plt.xlabel('Role', fontsize=12)
plt.ylabel('Jumlah Kali Dipilih', fontsize=12)
plt.show()