import streamlit as st
import requests

# PAGE CONFIGURATION

st.set_page_config(
page_title="TRACE URL Intelligence",
page_icon="🌐",
layout="wide"
)

API_URL = "http://127.0.0.1:8000/analyze-url"

# PAGE HEADER

st.title("URL Intelligence")
st.write("Analyse suspicious URLs using machine learning.")
st.divider()

st.header("URL Threat Scanner")

url = st.text_input(
"Enter a website URL",
placeholder="https://example.com"
)

# URL ANALYSIS BUTTON

if st.button("Analyse URL", type="primary"):
   

if not url.strip():
    st.warning("Please enter a URL first.")

else:
    try:
        with st.spinner("Analysing URL..."):

            response = requests.post(
                API_URL,
                json={"url": url.strip()},
                timeout=30
            )

        if response.status_code == 200:

            result = response.json()

            st.success("Analysis completed!")

            # CLASSIFICATION RESULT

            if result["result"] == "PHISHING":
                st.error("⚠️ Potential Phishing URL Detected")
            else:
                st.success("✅ Classified as Legitimate")

            # MODEL METRICS

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Model Confidence",
                    f'{result["model_confidence"]}%'
                )

            with col2:
                st.metric(
                    "Classification",
                    result["result"]
                )

            st.divider()

            # URL CHARACTERISTICS

            st.subheader("URL Characteristics")

            features = result["features"]

            columns = st.columns(3)

            for index, (name, value) in enumerate(features.items()):

                with columns[index % 3]:
                    st.metric(
                        name.replace("_", " ").title(),
                        value
                    )

            st.caption(
                "Model confidence is not a guarantee that a "
                "website is safe or malicious."
            )

        else:
            st.error(
                f"API Error: {response.status_code}"
            )
            st.write(response.text)

    except requests.exceptions.ConnectionError:
        st.error(
            "Cannot connect to TRACE API. "
            "Please make sure the FastAPI server is running."
        )

    except requests.exceptions.Timeout:
        st.error(
            "Request timed out. Please try again."
        )

    except Exception as error:
        st.error(
            f"Unexpected error: {error}"
        )


# FOOTER

st.divider()

st.caption(
"TRACE | AI-Powered Digital Threat Intelligence Platform"
)
