import tkinter as tk

def press_number(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def press_operator(operator):
    current = entry.get()
    if current and current[-1] not in ['+', '-', '*', '/']:
        entry.delete(0, tk.END)
        entry.insert(0, current + operator)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Mobile Calculator")

# Create entry field for expression
entry = tk.Entry(root, width=30, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button layout
# Define button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 1, 4)  # Corrected button definition
]

# Create buttons
for button_text, row, column, *span in buttons:
    if button_text == '=':
        button = tk.Button(root, text=button_text, width=10, height=2, command=calculate)
        button.grid(row=row, column=column, columnspan=span[0], padx=5, pady=5)
    elif button_text == 'C':
        button = tk.Button(root, text=button_text, width=10, height=2, command=clear)
        button.grid(row=row, column=column, padx=5, pady=5)
    else:
        button = tk.Button(root, text=button_text, width=5, height=2, command=lambda x=button_text: press_number(x) if x.isdigit() else press_operator(x))
        button.grid(row=row, column=column, padx=5, pady=5)


# Run the main event loop
root.mainloop()
