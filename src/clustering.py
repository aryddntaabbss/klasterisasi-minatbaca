import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import matplotlib.pyplot as plt
import os

def proses_clustering():
    # Baca data
    data = pd.read_csv('data/minat_baca.csv')

    # Ambil kolom fitur yang mau dianalisis (misal kolom 2 sampai terakhir)
    X = data.iloc[:, 1:].values

    # Proses linkage hierarchical clustering
    Z = linkage(X, method='ward')  # atau 'average', 'complete'

    # Simpan dendrogram
    plt.figure(figsize=(10, 7))
    dendrogram(Z)
    plt.title('Dendrogram Klasterisasi Minat Baca')
    plt.xlabel('Data Responden')
    plt.ylabel('Jarak (Euclidean)')
    os.makedirs('hasil', exist_ok=True)
    plt.savefig('hasil/dendrogram.png')
    plt.close()

    # Buat cluster (misal 3 cluster)
    cluster_result = fcluster(Z, 3, criterion='maxclust')
    data['Cluster'] = cluster_result

    # Simpan hasil clustering
    data.to_csv('hasil/hasil_klasterisasi.csv', index=False)

    print("✅ Proses clustering selesai, hasil disimpan di folder 'hasil'.")

