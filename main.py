import tkinter as tk
import ttkbootstrap as ttk

def main():
    window = ttk.Window(title="Socket Mapper", size=[800, 600], themename="superhero")
    # Scalability | Set it false for now and change it later during optimization
    window.resizable(False, False)

    window.mainloop()

if __name__ == '__main__':
    main()