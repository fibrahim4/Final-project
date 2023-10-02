import tkinter as tk

# Function to perform calculations
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        result_label.config(text=f"Result: {result}")
        history_listbox.insert(tk.END, f"{expression} = {result}")
    except Exception as e:
        result_label.config(text="Invalid Input")

# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Create and configure the calculator interface
calculator_frame = tk.Frame(root)
entry = tk.Entry(calculator_frame, width=25)
calculate_button = tk.Button(calculator_frame, text="Calculate", command=calculate)
result_label = tk.Label(calculator_frame, text="Result:")
history_button = tk.Button(calculator_frame, text="Show History", command=lambda: history_window.deiconify())

entry.pack()
calculate_button.pack()
result_label.pack()
history_button.pack()
calculator_frame.pack()

# Create a history window
history_window = tk.Toplevel(root)
history_window.title("Calculation History")
history_listbox = tk.Listbox(history_window, width=40, height=10)
history_listbox.pack()
history_window.withdraw()  # Hide the history window initially

# Start the main loop
root.mainloop()
