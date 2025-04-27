import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """
    Fungsi untuk membaca file CSV.
    :param file_path: path ke file csv
    :return: DataFrame pandas
    """
    try:
        data = pd.read_csv(file_path)
        print(f"✅ Data berhasil dibaca dari {file_path}")
        return data
    except FileNotFoundError:
        print(f"❌ File {file_path} tidak ditemukan.")
        return None


def standardize_data(dataframe, feature_columns):
    """
    Fungsi untuk melakukan standardisasi data numerik.
    :param dataframe: DataFrame pandas
    :param feature_columns: list nama kolom yang ingin distandardisasi
    :return: array hasil standardisasi
    """
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(dataframe[feature_columns].values)
    print("✅ Data berhasil distandardisasi.")
    return X_scaled


def save_dataframe(dataframe, output_path):
    """
    Fungsi untuk menyimpan DataFrame ke file CSV.
    :param dataframe: DataFrame pandas
    :param output_path: path file output
    """
    dataframe.to_csv(output_path, index=False)
    print(f"✅ Data berhasil disimpan di {output_path}")

