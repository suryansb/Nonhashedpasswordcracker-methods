import itertools
import string
from tqdm import tqdm

def brute_force_crack(hidden_password):
    charset = string.ascii_lowercase + string.digits  # Characters to attempt
    for length in range(1, 6):  # Password lengths to try (e.g., from 1 to 6 characters)
        attempts = itertools.product(charset, repeat=length)
        for attempt in tqdm(attempts, total=len(charset) ** length):
            attempt_password = ''.join(attempt)
            if attempt_password == hidden_password:  # Compare attempt to the hidden password
                return attempt_password
    return None

if __name__ == "__main__":
    hidden_password = "qwerty"  # This is the password the tool is trying to crack (you don't show this to the user)
    cracked_password = brute_force_crack(hidden_password)
    
    if cracked_password:
        print(f"Password cracked: {cracked_password}")
    else:
        print("Failed to crack the password.")
