
---SUBMISSION--- 

A. Setup Environment

1. python -m venv main-ds
2. main-ds\scripts\activate
3. pip install numpy pandas scipy matplotlib seaborn jupyter 
4. mkdir proyek_analisis
5. cd proyek_analisis
6. jupyter-notebook

B.  Gatering Data

1. impor day.csv
2. impor hour.csv

C. Assessing Data

1. Pada tabel day_df

a. Mengecek missing value dan duplikasi 
b. Mencegek kevalidan nilai season
c. Mengecek kevalidan nilai yr
d. Mengecek kevalidan nilai mnth
e. Mengecek kevalidan nilai weathersit
f. Mengecek skala normalisasi apakah melebihi 1
g. Mengecek kolom cnt (total penyewaan) harus selalu sama dengan jumlah casual + registered

2. Pada tabel hour_df

a. Mengecek mising value dan duplikasi
b. Mengecek Nilai Unik dalam weathersit
c. Mengecek Nilai Unik dalam weathersit
d. mengcek Konsistensi cnt dengan casual + registered
note : Pada Assessing Data pada day_df dan hour_df terdapat kesalahan type data pada dteday harusnya datetime

D. Cleaning Data
memperbaiki kesalahan yang di assessing data

E. Eksplorasi Data (EDA) 
Pertenyaan Bisnis
1. Bagaimana tren penyewaan sepeda dari waktu ke waktu?
2. Bagaimana cuaca mempengaruhi jumlah penyewaan sepeda?

F. Run steamlit app
streamlit run dashboard.py