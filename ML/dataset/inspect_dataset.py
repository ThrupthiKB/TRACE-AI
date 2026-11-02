import pandas as pd
from pathlib import Path

# Load downloaded dataset
file_path = Path(__file__).parent / "phishing_dataset.csv"
data = pd.read_csv(file_path)

print("Total records:", len(data))

print("\nLabel distribution:")
print(data["label"].value_counts())

print("\nLabel percentages:")
print(data["label"].value_counts(normalize=True) * 100)

print("\nMissing values:")
print(data.isnull().sum().sum())