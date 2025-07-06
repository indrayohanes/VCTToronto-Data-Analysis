import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Konfigurasi Halaman dan Judul ---
st.set_page_config(layout="wide")
st.title('📊 Dashboard Analisis VCT')
st.write("Visualisasi data dari turnamen VCT berdasarkan file `vct toronto.csv`.")

# --- Fungsi untuk Memuat dan Mengolah Data ---
# Menggunakan cache agar data tidak perlu dimuat ulang setiap kali ada interaksi
@st.cache_data
def load_data():
    df = pd.read_csv('vct toronto.csv')
    # Menghindari pembagian dengan nol jika ada pemain yang Deaths-nya 0
    df['KDA Ratio'] = (df['K'] + df['A']) / df['D'].replace(0, 1)
    return df

# Memuat data menggunakan fungsi yang sudah dibuat
df = load_data()

# --- Garis Pemisah ---
st.markdown("---")

# --- Visualisasi Data ---
col1, col2 = st.columns(2)

with col1:
    # --- Analisis 1: Top 10 Pemain Berdasarkan ACS ---
    st.header('🏆 Top 10 Pemain Terbaik (ACS)')
    
    top_10_players_acs = df.groupby('Player')['ACS'].mean().sort_values(ascending=False).head(10)

    fig1, ax1 = plt.subplots(figsize=(10, 8))
    sns.barplot(ax=ax1, x=top_10_players_acs.values, y=top_10_players_acs.index, palette='viridis', orient='h')
    
    ax1.set_title('Top 10 Pemain Berdasarkan Rata-Rata ACS', fontsize=16)
    ax1.set_xlabel('Rata-Rata Average Combat Score (ACS)', fontsize=12)
    ax1.set_ylabel('Pemain', fontsize=12)
    
    st.pyplot(fig1)

with col2:
    # --- Analisis 2: Popularitas Role Agent ---
    st.header('🗺️ Popularitas Role Agent')

    role_picks = df['Role'].value_counts()

    fig2, ax2 = plt.subplots(figsize=(10, 8))
    sns.barplot(ax=ax2, x=role_picks.index, y=role_picks.values, palette='mako')

    ax2.set_title('Popularitas Role di VCT Toronto', fontsize=16)
    ax2.set_xlabel('Role', fontsize=12)
    ax2.set_ylabel('Jumlah Kali Dipilih', fontsize=12)

    st.pyplot(fig2)

# --- Garis Pemisah ---
st.markdown("---")

# --- Tambahkan Filter Interaktif ---
st.sidebar.header("Filter Data")
selected_team = st.sidebar.selectbox('Pilih Tim:', df['Region'].unique())
team_data = df[df['Region'] == selected_team]

st.header(f'Detail Statistik untuk Regionc: {selected_team}')
st.dataframe(team_data)

# --- Menampilkan Data Mentah (Opsional) ---
if st.checkbox('Tampilkan Data Lengkap'):
    st.header('Data Lengkap Turnamen')
    st.dataframe(df)