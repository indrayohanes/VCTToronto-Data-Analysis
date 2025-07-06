import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
df = pd.read_csv('vct toronto.csv')

print("5 Baris Pertama Data:")
print(df.head())

print("\nInformasi DataFrame:")
df.info()


print("\nJumlah Data yang Hilang per Kolom:")
print(df.isnull().sum())

df['KDA Ratio'] = (df['K'] + df['A']) / df['D'].replace(0, 1)

print("\nData dengan kolom KDA Ratio baru:")
print(df.head())

top_10_players_acs = df.groupby('Player')['ACS'].mean().sort_values(ascending=False).head(10)

print("Top 10 Pemain Berdasarkan Rata-rata ACS:")
print(top_10_players_acs)

plt.figure(figsize=(12, 7)) 
sns.barplot(x=top_10_players_acs.values, y=top_10_players_acs.index, palette='viridis')
plt.title('Top 10 Pemain VCT Toronto Berdasarkan Rata-Rata ACS', fontsize=16)
plt.xlabel('Rata-Rata Average Combat Score (ACS)', fontsize=12)
plt.ylabel('Pemain', fontsize=12)
plt.show() 


role_picks = df['Role'].value_counts()

print("Jumlah Pemilihan Agent Selama Turnamen:")
print(role_picks)

plt.figure(figsize=(14, 8))
sns.barplot(x=role_picks.index, y=role_picks.values, palette='mako')
plt.title('Popularitas Role di VCT Toronto', fontsize=16)
plt.xlabel('Role', fontsize=12)
plt.ylabel('Jumlah Kali Dipilih', fontsize=12)
plt.show()
