import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer")
        
        # Characters to choose from for generating the password
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Generate the password
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display the generated password
        password_output.config(state=tk.NORMAL)
        password_output.delete(1.0, tk.END)
        password_output.insert(tk.END, password)
        password_output.config(state=tk.DISABLED)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def clear_fields():
    name_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    password_output.config(state=tk.NORMAL)
    password_output.delete(1.0, tk.END)
    password_output.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create labels
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

length_label = tk.Label(root, text="Length:")
length_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

password_label = tk.Label(root, text="Generated Password:")
password_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

# Create entry fields
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

length_entry = tk.Entry(root)
length_entry.grid(row=1, column=1, padx=5, pady=5)

# Create output field for generated password
password_output = tk.Text(root, height=2, width=30, state=tk.DISABLED)
password_output.grid(row=2, column=1, padx=5, pady=5)

# Create buttons
generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_fields)
clear_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

accept_button = tk.Button(root, text="Accept", command=root.quit)
accept_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Run the main event loop
root.mainloop()
