import tkinter as tk
from PIL import Image, ImageTk

# Declare entry and result_label as global variables
entry = None
result_label = None

# Function to perform calculations
def calculate():
    global entry, result_label  # Declare them as global so we can access them
    try:
        expression = entry.get()
        if expression:
            result = eval(expression)
            result_label.config(text=f"Result: {result}")
            history_listbox.insert(tk.END, f"{expression} = {result}")
        else:
            result_label.config(text="Input is empty")
    except Exception as e:
        result_label.config(text="Invalid Input")

# Function to clear the input field
def clear_input():
    entry.delete(0, tk.END)

# Function to resize an image while maintaining the aspect ratio
def resize_image(image, target_width, target_height):
    width, height = image.size
    if width > target_width or height > target_height:
        ratio = min(target_width / width, target_height / height)
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        return image.resize((new_width, new_height))
    return image

# Create the main application window
def create_main_window():
    global entry, result_label  # Declare them as global so we can access them
    root = tk.Tk()
    root.title("Calculator")

    # Load and display the "calculator.gif" image using Pillow
    calculator_image = Image.open("calculator.gif")
    calculator_image = resize_image(calculator_image, 200, 200)  # Adjust the width and height as needed
    calculator_image = ImageTk.PhotoImage(calculator_image)

    # Load and display the "formula.gif" image using Pillow
    formula_image = Image.open("formula.gif")
    formula_image = resize_image(formula_image, 200, 200)  # Adjust the width and height as needed
    formula_image = ImageTk.PhotoImage(formula_image)

    # Create and configure the calculator interface
    calculator_frame = tk.Frame(root)
    entry = tk.Entry(calculator_frame, width=25)
    calculate_button = tk.Button(calculator_frame, text="Calculate", command=calculate)
    result_label = tk.Label(calculator_frame, text="Result:")
    history_button = tk.Button(calculator_frame, text="Show History", command=show_history)

    # Display the "calculator.gif" image in a label
    image_label_calculator = tk.Label(calculator_frame, image=calculator_image)
    image_label_calculator.image = calculator_image

    # Display the "formula.gif" image in a label
    image_label_formula = tk.Label(calculator_frame, image=formula_image)
    image_label_formula.image = formula_image

    entry.pack()
    calculate_button.pack()
    result_label.pack()
    history_button.pack()
    image_label_calculator.pack()
    image_label_formula.pack()
    calculator_frame.pack()
    return root

# ... (rest of your code remains the same)

# Create a history window
def create_history_window(root):
    history_window = tk.Toplevel(root)
    history_window.title("Calculation History")
    history_listbox = tk.Listbox(history_window, width=40, height=10)
    history_listbox.pack()

    back_button = tk.Button(history_window, text="Back to Calculator", command=hide_history)
    back_button.pack()

    history_window.withdraw()  # Hide the history window initially
    return history_window, history_listbox

# Function to show the history window
def show_history():
    history_window.deiconify()

# Function to hide the history window
def hide_history():
    history_window.withdraw()

# Main entry point
if __name__ == "__main__":
    root = create_main_window()
    history_window, history_listbox = create_history_window(root)
    root.mainloop()
