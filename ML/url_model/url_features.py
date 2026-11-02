import re
import ipaddress
from urllib.parse import urlparse


def extract_url_features(url):

    # Add scheme if missing
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    parsed = urlparse(url)

    hostname = parsed.hostname or ""
    path = parsed.path or ""
    full_url = url.lower()

    # Check whether domain is an IP address
    try:
        ipaddress.ip_address(hostname)
        is_ip = 1
    except ValueError:
        is_ip = 0

    # Count digits and letters
    digit_count = sum(char.isdigit() for char in full_url)
    letter_count = sum(char.isalpha() for char in full_url)

    # Extract features
    features = {

        "url_length": len(url),

        "hostname_length": len(hostname),

        "path_length": len(path),

        "count_dots": full_url.count("."),

        "count_hyphens": full_url.count("-"),

        "count_at": full_url.count("@"),

        "count_question": full_url.count("?"),

        "count_ampersand": full_url.count("&"),

        "count_equal": full_url.count("="),

        "count_slash": full_url.count("/"),

        "count_digits": digit_count,

        "count_letters": letter_count,

        "count_percent": full_url.count("%"),

        "count_underscore": full_url.count("_"),

        "subdomain_count": max(0, len(hostname.split(".")) - 2),

        "has_https": 1 if parsed.scheme == "https" else 0,

        "is_ip": is_ip,

        "has_port": 1 if parsed.port is not None else 0,

        "has_suspicious_word": 1 if re.search(
            r"login|verify|update|secure|account|banking|password",
            full_url
        ) else 0

    }

    return features


# Test the feature extractor
if __name__ == "__main__":

    test_url = "https://secure-login-example.com/verify"

    result = extract_url_features(test_url)

    print("Testing URL Feature Extractor")
    print("--------------------------------")

    print("URL:", test_url)

    print("\nExtracted Features:")

    for feature, value in result.items():
        print(f"{feature}: {value}")