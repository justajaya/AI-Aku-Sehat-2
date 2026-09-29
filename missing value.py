import pandas as pd
file_path = "data/nutrition.csv"
df = pd.read_csv(file_path)
print("=" * 50)
print("MISSING VALUE CHECK")
print("=" * 50)
print(f"Jumlah data       : {len(df)}")
print(f"Jumlah kolom      : {len(df.columns)}")
missing = df.isnull().sum()
print("\nMissing value setiap kolom:")
print(missing)
total_missing = missing.sum()
print(f"\nTotal missing value: {total_missing}")
df_clean = df.dropna()
print(f"\nJumlah data setelah cleaning: {len(df_clean)}")
output_file = "data/nutrition_clean.csv"
df_clean.to_csv(output_file, index=False)
print(f"File hasil cleaning: {output_file}")
print("\nProses selesai.")