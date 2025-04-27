import pandas as pd
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, fcluster

def evaluasi_clustering():
    # Baca data
    data = pd.read_csv('data/minat_baca.csv')
    X = data.iloc[:, 1:].values

    # Standardisasi data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Buat linkage matrix
    Z = linkage(X_scaled, method='ward')

    # Ambil cluster hasil fcluster
    cluster_result = fcluster(Z, 3, criterion='maxclust')

    # Hitung Silhouette Score
    score = silhouette_score(X_scaled, cluster_result)
    print(f"📊 Silhouette Score: {score:.4f}")

