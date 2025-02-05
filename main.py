import tkinter as tk
import ttkbootstrap as ttk

def main():
    global window
    window = ttk.Window(title="Socket Mapper", size=[800, 600], themename="superhero", iconphoto="cable.png")
    # Scalability | Set it false for now and change it later during optimization
    window.resizable(False, False)

    # The title of the running page
    global title
    title = ttk.Label(master=window, text="Socket Mapper", font="Jokerman 24 bold")
    title.pack()

    # Central image only in the main page
    image = ttk.Image.open("cable.png")
    image = image.resize((400, 400))
    tkImage = ttk.ImageTk.PhotoImage(image)
    global centralImage
    centralImage = ttk.Label(master=window, image=tkImage)
    centralImage.pack()

    # The following buttons should navigate to two different pages
    global btnFrame
    btnFrame = ttk.Frame(master=window)
    btnPortScanning = ttk.Button(master=btnFrame, text="Port Scanning", style='success-outline', command=Scanning_GUI)
    btnBannerGrapping = ttk.Button(master=btnFrame, text="Banner Grapping", style='danger-outline', command=Grapping_GUI)
    btnFrame.pack(pady=20)
    btnBannerGrapping.pack(side="left", padx=40)
    btnPortScanning.pack(side="left", padx=40)

    window.mainloop()

def clear(*args):
    for element in args:
        element.destroy()

# Try to add restoring feature in the future in order to add a back button

def Scanning_GUI():
    clear(centralImage, btnFrame)
    title.configure(text='Port Scanning')

    # Host address or domain input box
    hostEntryFrame = ttk.Frame(master=window)
    hostLabel = ttk.Label(master=hostEntryFrame, text='Host:', font='Chiller 18 bold')
    hostEntry = ttk.Entry(master=hostEntryFrame)
    hostEntryFrame.pack()
    hostLabel.pack(side='left', padx=10)
    hostEntry.pack(side='left', padx=10)

    # TCP or UDP
    protocolFrame = ttk.Frame(master=window)
    protocolVariable = ttk.StringVar(value='TCP') # TCP is the default value
    protocolLabel = ttk.Label(master=protocolFrame, text='Protocol:', font='Chiller 18 bold')
    TCP_RadioButton = ttk.Radiobutton(master=protocolFrame, text='TCP', variable=protocolVariable, value='TCP', style='Outline.Toolbutton')
    UDP_RadioButton = ttk.Radiobutton(master=protocolFrame, text='UDP', value='UDP', variable=protocolVariable, style='Outline.Toolbutton')
    protocolFrame.pack(pady=20)
    protocolLabel.pack(side='left', padx=10)
    UDP_RadioButton.pack(side='left', padx=10)
    TCP_RadioButton.pack(side='left', padx=10)


def Grapping_GUI():
    clear(centralImage, btnFrame)
    title.configure(text='Banner Grapping')

if __name__ == '__main__':
    main()