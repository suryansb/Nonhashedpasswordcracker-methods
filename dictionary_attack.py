from tqdm import tqdm
def dictionary_crack(password, dictionary_file):
    with open(dictionary_file, 'r', encoding='utf-8') as f:
        for word in tqdm(f.readlines()):
            word = word.strip()
            if word == password:
                return word
    return None

if __name__ == "__main__":
    cracked_password = dictionary_crack("password123", "ignis-1M.txt")
    if cracked_password:
        print(f"Password cracked: {cracked_password}")
    else:
        print("Failed to crack the password.")
