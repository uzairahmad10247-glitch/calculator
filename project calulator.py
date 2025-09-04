import tkinter as tk

# Function to update expression
def press(key):
    global expression
    expression += str(key)
    equation.set(expression)

# Function to evaluate final result
def equalpress():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# Function to clear
def clear():
    global expression
    expression = ""
    equation.set("")

# Main window
root = tk.Tk()
root.title("Calculator")

# Set fullscreen-like window size
root.geometry("400x550")     # bigger size
root.resizable(False, False)

# Colors
bg_color = "#2E3247"       # Dark background
btn_color = "#2E3247"      # Button color
fg_color = "white"         # Text color
display_color = "#FFD54F"  # Yellow display

expression = ""
equation = tk.StringVar()

# Display
display = tk.Entry(root, textvariable=equation, font=('Arial', 28, 'bold'),
                   bg=display_color, fg="black", bd=0, justify='right')
display.pack(fill='both', ipadx=8, ipady=25, padx=5, pady=5)

# Buttons Frame
btns_frame = tk.Frame(root, bg=bg_color)
btns_frame.pack(expand=True, fill="both")

# Button creator
def create_button(text, row, col, width=5, height=2, command=None, colspan=1):
    button = tk.Button(
        btns_frame, text=text, font=('Arial', 20, 'bold'),
        fg=fg_color, bg=btn_color,
        width=width*colspan, height=height,
        bd=0, relief="flat", command=command
    )
    button.grid(row=row, column=col, padx=5, pady=5, columnspan=colspan, sticky="nsew")

# Configure grid to expand equally
for i in range(5):   # 5 rows (0–4 digits + 1 equal)
    btns_frame.rowconfigure(i, weight=1)
for j in range(4):   # 4 columns
    btns_frame.columnconfigure(j, weight=1)

# Number buttons
numbers = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
    ('0', 3, 0), ('.', 3, 1), ('C', 3, 2)
]

for (text, row, col) in numbers:
    if text == "C":
        create_button(text, row, col, command=clear)
    else:
        create_button(text, row, col, command=lambda t=text: press(t))

# Operator buttons (right side)
create_button("÷", 0, 3, command=lambda: press("/"))
create_button("×", 1, 3, command=lambda: press("*"))
create_button("−", 2, 3, command=lambda: press("-"))
create_button("+", 3, 3, command=lambda: press("+"))

# Equal button (bottom full row)
create_button("=", 4, 0, colspan=4, command=equalpress)

root.configure(bg=bg_color)
root.mainloop()
