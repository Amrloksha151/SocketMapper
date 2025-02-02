import tkinter as tk
import ttkbootstrap as ttk

def main():
    window = ttk.Window(title="Socket Mapper", size=[800, 600], themename="superhero", iconphoto="cable.png")
    # Scalability | Set it false for now and change it later during optimization
    window.resizable(False, False)

    # The title of the running page
    title = ttk.Label(master=window, text="Socket Mapper", font="Jokerman 24 bold")
    title.pack()

    # Central image only in the main page
    image = ttk.Image.open("cable.png")
    image = image.resize((400, 400))
    tkImage = ttk.ImageTk.PhotoImage(image)
    centralImage = ttk.Label(master=window, image=tkImage)
    centralImage.pack()

    # The following buttons should navigate to two different pages
    btnFrame = ttk.Frame(master=window)
    btnPortScanning = ttk.Button(master=btnFrame, text="Port Scanning")
    btnBannerGrapping = ttk.Button(master=btnFrame, text="Banner Grapping")
    btnFrame.pack(pady=20)
    btnBannerGrapping.pack(side="left", padx=40)
    btnPortScanning.pack(side="left", padx=40)

    window.mainloop()

if __name__ == '__main__':
    main()