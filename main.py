from tkinter import *

def calculate_km():
    miles = float(label_input.get())  # Get the input value
    km = miles * 1.60934  # Convert miles to kilometers
    km_label_result.config(text=f"{km:.2f}")  # Update the result label

# Create main window
window = Tk()
window.minsize(width=200, height=200)
window.title("Miles to Km Converter")
window.config(padx=100, pady=20)

# Entry widget for input
label_input = Entry(width=10)
label_input.grid(column=1, row=0)

# Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

km_label_result = Label(text="0")
km_label_result.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button to trigger calculation
calculate_button = Button(text="Calculate", command=calculate_km)
calculate_button.grid(column=1, row=2)
# Run the main loop
window.mainloop()
