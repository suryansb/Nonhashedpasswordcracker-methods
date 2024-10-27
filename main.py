import tkinter as tk
from tkinter import messagebox
import threading
from methods import brute_force_crack, dictionary_crack, pattern_crack

def crack_password():
    hidden_password = password_entry.get()
    method = method_var.get()

    # Run the password cracking in a separate thread to avoid freezing the GUI
    def run_cracker():
        if method == 'bruteforce':
            result = brute_force_crack(hidden_password)
        elif method == 'dictionary':
            result = dictionary_crack(hidden_password, "ignis-1M.txt")
        elif method == 'pattern':
            result = pattern_crack(hidden_password)
        else:
            result = None

        if result:
            messagebox.showinfo("Success", f"Password cracked: {result}")
        else:
            messagebox.showerror("Failed", "Failed to crack the password.")

    # Start the cracking process in a separate thread
    threading.Thread(target=run_cracker).start()

# Set up the main window
root = tk.Tk()
root.title("Password Cracker")

# Password entry
tk.Label(root, text="Enter password to crack:").pack(pady=10)
password_entry = tk.Entry(root, show="*")  # Hide input with '*'
password_entry.pack(pady=10)

# Method selection
method_var = tk.StringVar(value='bruteforce')
tk.Label(root, text="Choose cracking method:").pack(pady=10)

tk.Radiobutton(root, text="Brute Force", variable=method_var, value='bruteforce').pack()
tk.Radiobutton(root, text="Dictionary Attack", variable=method_var, value='dictionary').pack()
tk.Radiobutton(root, text="Pattern Matching", variable=method_var, value='pattern').pack()

# Crack button
tk.Button(root, text="Crack Password", command=crack_password).pack(pady=20)

# Run the application
root.mainloop()
