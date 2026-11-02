import pandas as pd
from ucimlrepo import fetch_ucirepo
from pathlib import Path

print("Downloading PhiUSIIL dataset...")

dataset = fetch_ucirepo(id=967)

X = dataset.data.features
y = dataset.data.targets

data = pd.concat([X, y], axis=1)

output_path = Path(__file__).parent / "phishing_dataset.csv"

data.to_csv(output_path, index=False)

print("\nDataset downloaded successfully!")
print("Dataset shape:", data.shape)

print("\nAvailable columns:")
print(data.columns.tolist())

print("\nFirst five records:")
print(data.head())

print("\nDataset saved at:", output_path)
