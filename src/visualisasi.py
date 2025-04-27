import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import os

def tampilkan_visualisasi():
    # Baca hasil clustering
    data = pd.read_csv('hasil/hasil_klasterisasi.csv')
    X = data.iloc[:, 1:-1].values  # exclude kolom Cluster

    # PCA untuk reduksi dimensi ke 2D
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    # Tambahkan hasil PCA ke dataframe
    data['PCA1'] = X_pca[:, 0]
    data['PCA2'] = X_pca[:, 1]

    # Plot scatter plot cluster
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='PCA1', y='PCA2', hue='Cluster', data=data, palette='Set1')
    plt.title('Visualisasi Klasterisasi Minat Baca (PCA)')
    plt.xlabel('Komponen Utama 1')
    plt.ylabel('Komponen Utama 2')
    os.makedirs('hasil', exist_ok=True)
    plt.savefig('hasil/scatter_plot.png')
    plt.close()

    print("📊 Scatter plot cluster disimpan di folder 'hasil'.")

