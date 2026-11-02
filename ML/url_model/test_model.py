import joblib
from pathlib import Path

from url_features import extract_url_features

# Load trained model
model_path = Path(__file__).parent / "url_model.pkl"

model = joblib.load(model_path)

print("TRACE URL Intelligence")
print("----------------------")

while True:

    url = input("\nEnter a URL (or type exit): ")

    if url.lower() == "exit":
        print("Exiting TRACE...")
        break

    try:
        # Extract URL features
        features = extract_url_features(url)

        # Convert features into model input
        import pandas as pd

        input_data = pd.DataFrame([features])

        # Predict
        prediction = model.predict(input_data)[0]

        probabilities = model.predict_proba(input_data)[0]

        if prediction == 0:
            print("\nResult: PHISHING URL")
        else:
            print("\nResult: LEGITIMATE URL")

        print(
            "Model confidence:",
            round(max(probabilities) * 100, 2),
            "%"
        )

    except Exception as error:
        print("Error:", error)