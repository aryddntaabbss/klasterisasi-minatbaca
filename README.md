
# 📊 Klasterisasi Minat Baca Masyarakat Kota Ternate

Proyek ini merupakan implementasi algoritma **Hierarchical Clustering** menggunakan Python untuk mengelompokkan minat baca masyarakat berdasarkan data survei yang dikumpulkan oleh Dinas Perpustakaan dan Kearsipan Daerah Kota Ternate.

---

## 📁 Struktur Folder

```
klasterisasi-minatbaca/
├── data/
│   └── minat_baca.csv       # Dataset minat baca
├── hasil/
│   └── dendrogram.png       # Visualisasi dendrogram hasil clustering
├── src/
│   ├── clustering.py        # Proses clustering data
│   ├── evaluation.py        # Evaluasi hasil clustering
│   ├── visualisasi.py       # Visualisasi hasil clustering
│   └── utils.py             # Utility function (buat dummy data, dll)
├── main.py                  # Program utama untuk menjalankan seluruh proses
├── requirements.txt         # Daftar library Python yang dibutuhkan
└── README.md                # Dokumentasi proyek ini
```

---

## 🛠️ Library yang Digunakan

- `pandas`: Digunakan untuk memanipulasi dan menganalisis data.
- `numpy`: Digunakan untuk komputasi numerik, terutama dalam perhitungan statistik dan matematika.
- `scikit-learn`: Digunakan untuk model machine learning, termasuk metrik evaluasi dan algoritma clustering.
- `scipy`: Digunakan untuk teknik ilmiah dan algoritma optimisasi.
- `matplotlib`: Digunakan untuk visualisasi data, seperti plot dendrogram.

---

## 📖 Penjelasan Teknologi

### Data Mining
Data mining adalah proses menemukan pola atau informasi yang berguna dari data yang besar dan kompleks. Teknik data mining digunakan untuk menganalisis data dan membuat model prediktif atau pengelompokan, serta menemukan hubungan atau pola tersembunyi dalam dataset. Dalam proyek ini, data mining digunakan untuk mengelompokkan minat baca masyarakat ke dalam klaster berdasarkan kemiripan data.

### Hierarchical Clustering
**Hierarchical Clustering** adalah metode klasterisasi yang digunakan untuk mengelompokkan data menjadi hirarki berdasarkan kedekatannya. Hierarchical clustering membangun struktur tree atau dendrogram yang menunjukkan hubungan antar data. Metode ini memiliki dua pendekatan utama:
- **Agglomerative (Bottom-up)**: Mulai dengan setiap data sebagai satu cluster terpisah, lalu secara bertahap menggabungkan pasangan cluster yang paling mirip.
- **Divisive (Top-down)**: Mulai dengan semua data dalam satu cluster besar, kemudian secara bertahap memisahkannya menjadi cluster yang lebih kecil.

Pada proyek ini, kami menggunakan metode **Agglomerative** untuk klasterisasi data minat baca.

### Agglomerative Clustering
Agglomerative Clustering adalah pendekatan bottom-up dalam Hierarchical Clustering, di mana setiap titik data dimulai sebagai klaster individu. Selanjutnya, algoritma ini menggabungkan dua klaster yang paling mirip berdasarkan pengukuran jarak (misalnya, Euclidean distance) hingga akhirnya semua data digabungkan menjadi satu klaster besar. Proses ini digambarkan dalam bentuk dendrogram yang menunjukkan urutan penggabungan klaster.

---

## 📦 Cara Instalasi

1. **Clone repository ini**
   ```bash
   git clone https://github.com/username/klasterisasi-minatbaca.git
   cd klasterisasi-minatbaca
   ```

2. **Buat virtual environment (opsional tapi disarankan)**
   ```bash
   python -m venv venv
   source venv/bin/activate    # di Mac/Linux
   venv\Scripts\activate       # di Windows
   ```

3. **Install library yang dibutuhkan**
   ```bash
   pip install -r requirements.txt
   ```

---

## 📑 Cara Menjalankan Program

1. **Pastikan dataset `data/minat_baca.csv` sudah tersedia.**
   - Format file:
     ```
     Nama,Fitur1,Fitur2,Fitur3
     Andi,5,3,4
     Budi,2,5,3
     ...
     ```

2. **Jika belum ada data, jalankan fungsi pembuat dummy**
   Buka `src/utils.py` → uncomment baris `buat_dummy_csv()` lalu jalankan:

   ```bash
   python src/utils.py
   ```

3. **Jalankan program utama**
   ```bash
   python main.py
   ```

4. **Hasil**
   - Visualisasi dendrogram akan disimpan di `hasil/dendrogram.png`
   - Hasil evaluasi clustering akan ditampilkan di terminal

---

## 📊 Fitur

- Klasterisasi data minat baca dengan **Agglomerative Hierarchical Clustering**
- Visualisasi hasil clustering dalam bentuk **Dendrogram**
- Evaluasi hasil clustering menggunakan **Silhouette Score**
- Support pembuatan dataset dummy untuk simulasi
