# pattern_matching_test.py

import re
from tqdm import tqdm

def pattern_crack(hidden_password):
    # A list of regex patterns to match
    patterns = [
        r'[a-z]{3}[0-9]{3}',  # Example: 3 letters followed by 3 digits
    ]
    for pattern in tqdm(patterns):
        if re.fullmatch(pattern, hidden_password):
            return hidden_password
    return None

if __name__ == "__main__":
    hidden_password = "password"  # This is the target password to be cracked
    print(f"Cracking password: {hidden_password}")

    # Crack the password using pattern matching
    cracked_password = pattern_crack(hidden_password)

    if cracked_password:
        print(f"Password cracked: {cracked_password}")
    else:
        print("Failed to crack the password.")
