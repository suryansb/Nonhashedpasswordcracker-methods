import argparse
from brute_force import brute_force_crack
from dictionary_attack import dictionary_crack
from pattern_matching import pattern_crack

def parse_arguments():
    parser = argparse.ArgumentParser(description='Non-hashed password cracker')
    parser.add_argument('-m', '--mode', required=True, choices=['bruteforce', 'dictionary', 'pattern'], help='Mode of attack')
    parser.add_argument('-p', '--password', required=True, help='Password to crack')
    parser.add_argument('-f', '--file', help='Dictionary file (for dictionary attack)')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_arguments()

    if args.mode == 'bruteforce':
        result = brute_force_crack(args.password)
    elif args.mode == 'dictionary' and args.file:
        result = dictionary_crack(args.password, args.file)
    elif args.mode == 'pattern':
        result = pattern_crack(args.password)
    else:
        result = None

    if result:
        print(f"Password cracked: {result}")
    else:
        print("Failed to crack the password.")
