import tkinter as tk  # if not used delete it while finalizing
import ttkbootstrap as ttk
from port_scanning import Scanning


# hello world
def main():
    global window
    window = ttk.Window(
        title="Socket Mapper",
        size=[800, 600],
        themename="superhero",
        iconphoto="cable.png",
    )
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
    btnPortScanning = ttk.Button(
        master=btnFrame,
        text="Port Scanning",
        style="success-outline",
        command=Scanning_GUI,
    )
    btnBannerGrapping = ttk.Button(
        master=btnFrame,
        text="Banner Grapping",
        style="danger-outline",
        command=Grapping_GUI,
    )
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
    title.configure(text="Port Scanning")

    # Host address or domain input box
    hostEntryFrame = ttk.Frame(master=window)
    hostLabel = ttk.Label(master=hostEntryFrame, text="Host:", font="Chiller 18 bold")
    global hostVar
    hostVar = ttk.StringVar()
    hostEntry = ttk.Entry(master=hostEntryFrame, textvariable=hostVar)
    hostEntryFrame.pack(pady=20)
    hostLabel.pack(side="left", padx=10)
    hostEntry.pack(side="left", padx=10)

    # Ports Range
    rangeFrame = ttk.Frame(master=window)
    rangeLabel = ttk.Label(master=rangeFrame, text="Range:", font="Chiller 18 bold")
    global startVar
    startVar = ttk.StringVar(value=0)
    startEntry = ttk.Entry(
        master=rangeFrame, width=5, textvariable=startVar
    )  # add a default value
    colon = ttk.Label(master=rangeFrame, text=":", font="Chiller 24 bold")
    global stopVar
    stopVar = ttk.StringVar(value=25)
    stopEntry = ttk.Entry(
        master=rangeFrame, width=5, textvariable=stopVar
    )  # add a default value
    rangeFrame.pack(pady=20)
    rangeLabel.pack(side="left", padx=10)
    startEntry.pack(side="left", padx=10)
    colon.pack(side="left", padx=5)
    stopEntry.pack(side="left", padx=10)

    # TCP or UDP
    protocolFrame = ttk.Frame(master=window)
    global protocolVariable
    protocolVariable = ttk.StringVar(value="TCP")  # TCP is the default value
    protocolLabel = ttk.Label(
        master=protocolFrame, text="Protocol:", font="Chiller 18 bold"
    )
    TCP_RadioButton = ttk.Radiobutton(
        master=protocolFrame,
        text="TCP",
        variable=protocolVariable,
        value="TCP",
        style="Outline.Toolbutton",
    )
    UDP_RadioButton = ttk.Radiobutton(
        master=protocolFrame,
        text="UDP",
        value="UDP",
        variable=protocolVariable,
        style="Outline.Toolbutton",
    )
    protocolFrame.pack(pady=20)
    protocolLabel.pack(side="left", padx=10)
    UDP_RadioButton.pack(side="left", padx=10)
    TCP_RadioButton.pack(side="left", padx=10)

    # Features
    featuresLabel = ttk.Label(master=window, text="Features", font="Chiller 24 bold")
    featuresLabel.pack(pady=20)
    featuresFrame = ttk.Frame(master=window)
    featuresFrame.pack()
    # Multithreading
    global threadingVar
    threadingVar = ttk.BooleanVar()
    threadingToggle = ttk.Checkbutton(
        master=featuresFrame,
        text="Multithreading",
        style="round-toggle",
        variable=threadingVar,
        onvalue=True,
        offvalue=False,
    )
    threadingToggle.pack(side="left", padx=10)
    # CSV... CSVT short for Comma Seprated Values Toggle button
    global csVar
    csVar = ttk.BooleanVar()
    csvT = ttk.Checkbutton(
        master=featuresFrame,
        text="CSV",
        style="round-toggle",
        variable=csVar,
        onvalue=True,
        offvalue=False,
    )
    csvT.pack(side="left", padx=10)
    # TXT
    global txtVar
    txtVar = ttk.BooleanVar()
    txt = ttk.Checkbutton(
        master=featuresFrame,
        text="TXT",
        style="round-toggle",
        variable=txtVar,
        onvalue=True,
        offvalue=False,
    )
    txt.pack(side="left", padx=10)

    # submit button
    submitBtn = ttk.Button(master=window, text="Submit", style="outline", command=scan)
    submitBtn.pack(pady=40)

def scan():
    scanner = Scanning(host=hostVar.get(), protocol=protocolVariable.get(), start=int(startVar.get()), stop=int(stopVar.get()), txt=txtVar.get(), csv=csVar.get())
    scanner.scan()
    scanner.save()
    # fix not responding error

def Grapping_GUI():
    clear(centralImage, btnFrame)
    title.configure(text="Banner Grapping")


if __name__ == "__main__":
    main()
