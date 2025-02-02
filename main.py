import tkinter as tk
import ttkbootstrap as ttk

def main():
    window = ttk.Window(title="Socket Mapper", size=[800, 600], themename="superhero", iconphoto="cable.png")
    # Scalability | Set it false for now and change it later during optimization
    window.resizable(False, False)

    # The title of the running page
    title = ttk.Label(master=window, text="Socket Mapper", font="Jokerman 24 bold")
    title.pack()

    window.mainloop()

if __name__ == '__main__':
    main()