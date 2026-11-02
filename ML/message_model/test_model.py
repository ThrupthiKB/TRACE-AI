import joblib
from pathlib import Path

# Load trained model
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "message_model.pkl"

model = joblib.load(MODEL_PATH)

print("TRACE Message Intelligence Model")
print("--------------------------------")

while True:

    message = input("\nEnter a message (or type exit): ")

    if message.lower() == "exit":
        break

    if not message.strip():
        print("Please enter a message.")
        continue

    prediction = model.predict([message])[0]
    probabilities = model.predict_proba([message])[0]

    confidence = max(probabilities) * 100

    if prediction == "spam":
        print("\n⚠️ Classification: SPAM / SUSPICIOUS")
    else:
        print("\n✓ Classification: HAM / LEGITIMATE")

    print(f"Model confidence: {confidence:.2f}%")