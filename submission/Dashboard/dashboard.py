from numpy import fix
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

# Load data 
all_dt=pd.read_csv("all_data.csv")

# Mapping categorical values
season_map = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
weather_map = {1: "Clear", 2: "Cloudy", 3: "Light Rain/Snow", 4: "Heavy Rain/Snow"}

all_dt["season"] = all_dt["season"].map(season_map)
all_dt["weathersit"] = all_dt["weathersit"].map(weather_map)

# Dashboard Title
st.title("📊 Bike Sharing Dashboard")
st.write("Analisis Penyewaan Sepeda Berdasarkan Faktor Cuaca, Musim, dan Hari")

# Sidebar Filter
st.sidebar.header("📌 Filter Data")
selected_year = st.sidebar.radio("Pilih Tahun:", [2011, 2012])
filtered_df = all_dt[all_dt["yr"] == (selected_year - 2011)]

# Menampilkan DataFrame
st.subheader(f"Dataset Penyewaan Sepeda Tahun {selected_year}")
st.dataframe(filtered_df.head())

#**Visualisasi Tren Penyewaan Sepeda**
st.subheader("📈 Tren Penyewaan Sepeda dari Waktu ke Waktu")
fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(x=filtered_df["dteday"], y=filtered_df["cnt"], color="blue", ax=ax)

ax.set_title("Tren Penyewaan Sepeda")
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Penyewaan")

# Format tanggal agar lebih renggang (misal, tiap 2 minggu)
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))

plt.xticks(rotation=45)  # Putar tanggal agar lebih terbaca
st.pyplot(fig)

#**Heatmap Penyewaan Sepeda Per Jam dan Hari**
st.subheader("⏳ Heatmap Penyewaan Sepeda per Jam dan Hari")
heatmap_data = all_dt.pivot_table(index="hr", columns="weekday", values="cnt", aggfunc="mean")

fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(heatmap_data, cmap="coolwarm", annot=True, fmt=".0f", ax=ax)
ax.set_title("Pola Penyewaan Sepeda (Jam vs Hari)")
ax.set_xlabel("Hari (0=Senin, 6=Minggu)")
ax.set_ylabel("Jam")
st.pyplot(fig)

# Footer