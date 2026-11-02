import pandas as pd
import urllib.request
import zipfile
import io
from pathlib import Path

# Dataset download URL
DATA_URL = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"

# Current folder
BASE_DIR = Path(__file__).resolve().parent

# Download dataset
print("Downloading SMS Spam Collection dataset...")

with urllib.request.urlopen(DATA_URL) as response:
    zip_data = response.read()

# Extract dataset
with zipfile.ZipFile(io.BytesIO(zip_data)) as archive:
    raw_data = archive.read("SMSSpamCollection")

# Read dataset
df = pd.read_csv(
    io.BytesIO(raw_data),
    sep="\t",
    header=None,
    names=["label", "message"],
    encoding="utf-8"
)

# Remove duplicate messages
df = df.drop_duplicates(subset="message").reset_index(drop=True)

# Save as CSV
output_path = BASE_DIR / "message_dataset.csv"
df.to_csv(output_path, index=False)

# Display dataset information
print("\nDataset downloaded successfully!")

print("\nFirst five messages:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nLabel distribution:")
print(df["label"].value_counts())

print("\nSaved to:", output_path)