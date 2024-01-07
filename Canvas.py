import tkinter as tk

print("You are in the Canvas.py file")

def Canvas(x, y):
    window = tk.Tk()
    window.geometry('800x600')
    window.title('Pic2Peak')

    button = tk.Button(window, text="Upload image", font=('Arial', 16), background='light grey')
    button.pack(pady=2)

    canvas = tk.Canvas(window, width=x, height=y, bg='white')
    canvas.pack(anchor=tk.CENTER, expand=True)

    logo = tk.PhotoImage(file = 'E:\My projects\Pic2Peak App\Pictures\logo.png')
    canvas.create_image((x/2, y/2), image=logo)

    window.mainloop()