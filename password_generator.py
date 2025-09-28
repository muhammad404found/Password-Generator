# Import tools for GUI and password generation
import tkinter as tk
import random
import string

# Check how strong the password is
def get_strength(password):
    if len(password) < 6:
        return "Weak"
    elif len(password) < 10:
        return "Moderate"
    else:
        return "Strong"

# Copy the password to clipboard
def copy_to_clipboard():
    password = result_label.cget("text").split("\n")[0]
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()
    result_label.config(text="Password copied to clipboard!")

# Make a new password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            result_label.config(text="Password must be at least 4 characters.")
            return
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        return
    
# Build the character pool
    characters = ""
    if include_letters.get():
        characters += string.ascii_letters
    if include_numbers.get():
        characters += string.digits
    if include_symbols.get():
        characters += string.punctuation

    if not characters:
        result_label.config(text="Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    strength = get_strength(password)
    result_label.config(text=f"{password}\nStrength: {strength}")
    copy_button.config(state="normal")
    length_entry.delete(0, tk.END)

# Set up the window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x350")
root.configure(bg="#f0f0f0")

# Add title and input field
tk.Label(root, text="Secure Password Length", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)
tk.Label(root, text="Enter Password Length:", font=("Arial", 12), bg="#f0f0f0").pack()
length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack(pady=5)

# Set up checkboxes
include_letters = tk.BooleanVar(value=False)
include_numbers = tk.BooleanVar(value=False)
include_symbols = tk.BooleanVar(value=False)

# Put the checkboxes in a row
checkbox_frame = tk.Frame(root, bg="#f0f0f0")
checkbox_frame.pack(pady=10)

tk.Checkbutton(checkbox_frame, text="Include Letters", variable=include_letters, bg="#f0f0f0", font=("Arial", 11)).grid(row=0, column=0, padx=10)
tk.Checkbutton(checkbox_frame, text="Include Numbers", variable=include_numbers, bg="#f0f0f0", font=("Arial", 11)).grid(row=0, column=1, padx=10)
tk.Checkbutton(checkbox_frame, text="Include Symbols", variable=include_symbols, bg="#f0f0f0", font=("Arial", 11)).grid(row=0, column=2, padx=10)

# Add buttons and result label
tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12)).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue", bg="#f0f0f0")
result_label.pack(pady=10)

copy_button = tk.Button(root, text="Copy Password", command=copy_to_clipboard, font=("Arial", 12))
copy_button.pack()
copy_button.config(state="disabled")

# Start the app
root.mainloop()
