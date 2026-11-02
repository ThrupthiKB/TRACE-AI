import pandas as pd
from pathlib import Path
from url_features import extract_url_features

print("Loading phishing dataset...")

dataset_path = Path(__file__).parent.parent / "dataset" / "phishing_dataset.csv"

data = pd.read_csv(dataset_path)

print("Dataset loaded:", len(data), "records")

print("\nExtracting URL features...")

features = data["URL"].apply(extract_url_features)

X = pd.DataFrame(features.tolist())
y = data["label"]

print("\nFeature extraction completed!")
print("Feature shape:", X.shape)
print("Target shape:", y.shape)

prepared_data = X.copy()
prepared_data["label"] = y.values

output_path = Path(__file__).parent / "url_training_data.csv"

prepared_data.to_csv(output_path, index=False)

print("\nPrepared dataset saved!")
print("Location:", output_path)

print("\nFirst five records:")
print(prepared_data.head())