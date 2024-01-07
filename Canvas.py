# Import from pip:
import tkinter as tk

# Debuging:
print("Tal: You are in the Canvas.py file")

# Variables:
path = '.\Pictures\logo.png'

# Working:
def Canvas(x, y):
    window = tk.Tk()
    window.geometry('800x600')
    window.title('Pic2Peak')

    button = tk.Button(window, text="Upload image", font=('Arial', 16), background='light grey')
    button.pack(pady=2)

    canvas = tk.Canvas(window, width=x, height=y, bg='white')
    canvas.pack(anchor=tk.CENTER, expand=True)

    logo = tk.PhotoImage(file = path)
    canvas.create_image((x/2, y/2), image=logo)

    window.mainloop()