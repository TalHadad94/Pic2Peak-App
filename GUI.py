# Import from pip:
import tkinter as tk
from tkinter import filedialog

# Debuging:
print("Tal: You are in the Canvas.py file")

# Working:
class GUI:

    def __init__(self, x, y):
        self.window = tk.Tk()

       # Frame:
        size = str(x+10) + 'x' + str(y+55)
        self.window.geometry(size)
        self.window.title('Pic2Peak')

        # Buttons:
        buttonsFrame = tk.Frame(self.window)
        buttonsFrame.columnconfigure(0, weight=1)
        button1 = tk.Button(buttonsFrame, text="Upload image", font=('Arial', 16), background='light grey', command=self.Loadfile)
        button1.grid(row=0, column=0, padx=2.5, pady=5)
        button2 = tk.Button(buttonsFrame, text="Clear image", font=('Arial', 16), background='light grey', command=self.LoadDefault)
        button2.grid(row=0, column=1, padx=2.5, pady=5)
        buttonsFrame.pack()
        
        # Workbox:
        canvas = tk.Canvas(self.window, width=x, height=y, bg='white')
        canvas.pack(anchor=tk.CENTER, expand=True)

        # Picture:
        photo = tk.PhotoImage(file = '.\Pictures\logo.png')#Need to add try here in case that logo not found.
        canvas.create_image((x/2, y/2), image=photo) 

        
        self.window.mainloop()

    
    def Loadfile(self):
        print("Uploading to Workbox...")
        self.load=filedialog.askopenfilename()
        print(self.load)

    def LoadDefault(self):
        print("Clearing Workbox...")