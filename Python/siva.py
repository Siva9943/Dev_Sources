import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("VLC MEDIA")

# Function to handle button click
def button_clicked():
    messagebox.showinfo("Message", "Button clicked!")

# Create a label
label = tk.Label(window, text="Welcome to Desktop App!", font=("Arial", 20))
label.pack(pady=20)

# Create a button
button = tk.Button(window, text="Click Me", command=button_clicked)
button.pack()

# Run the application
window.mainloop()
