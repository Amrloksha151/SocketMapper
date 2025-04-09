import tkinter as tk  # if not used delete it while finalizing
import ttkbootstrap as ttk
from port_scanning import Scanning
import time
from banner_grabbing import Grabbing
import threading


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
        cursor="hand2",
    )
    btnBannerGrapping = ttk.Button(
        master=btnFrame,
        text="Banner Grapping",
        style="danger-outline",
        command=Grabbing_GUI,
        cursor="hand2",
    )
    btnFrame.pack(pady=20)
    btnBannerGrapping.pack(side="left", padx=40)
    btnPortScanning.pack(side="left", padx=40)

    window.mainloop()


def clear(*args, hide=False):
    for element in args:
        if hide:
            element.pack_forget()
        else:
            element.destroy()


# Try to add restoring feature in the future in order to add a back button


def Scanning_GUI():
    clear(centralImage, btnFrame)
    title.configure(text="Port Scanner")

    # Host address or domain input box
    global hostVar, hostEntryFrame
    hostEntryFrame = ttk.Frame(master=window)
    hostLabel = ttk.Label(master=hostEntryFrame, text="Host:", font="Chiller 18 bold")
    hostVar = ttk.StringVar()
    hostEntry = ttk.Entry(master=hostEntryFrame, textvariable=hostVar)
    hostLabel.pack(side="left", padx=10)
    hostEntry.pack(side="left", padx=10)

    # Ports Range
    global rangeFrame, startVar, stopVar
    rangeFrame = ttk.Frame(master=window)
    rangeLabel = ttk.Label(master=rangeFrame, text="Range:", font="Chiller 18 bold")
    startVar = ttk.StringVar(value=0)
    startEntry = ttk.Entry(
        master=rangeFrame, width=5, textvariable=startVar
    )  # add a default value
    colon = ttk.Label(master=rangeFrame, text=":", font="Chiller 24 bold")
    stopVar = ttk.StringVar(value=25)
    stopEntry = ttk.Entry(
        master=rangeFrame, width=5, textvariable=stopVar
    )  # add a default value
    rangeLabel.pack(side="left", padx=10)
    startEntry.pack(side="left", padx=10)
    colon.pack(side="left", padx=5)
    stopEntry.pack(side="left", padx=10)

    # TCP or UDP
    global protocolVariable, protocolFrame
    protocolFrame = ttk.Frame(master=window)
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
    protocolLabel.pack(side="left", padx=10)
    UDP_RadioButton.pack(side="left", padx=10)
    TCP_RadioButton.pack(side="left", padx=10)

    # Features
    global featuresFrame, featuresLabel
    featuresLabel = ttk.Label(master=window, text="Features", font="Chiller 24 bold")
    featuresFrame = ttk.Frame(master=window)
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
    global submitBtn
    submitBtn = ttk.Button(
        master=window,
        text="Scan",
        style="outline",
        command=scan,
        cursor="hand2",
        width=20,
    )
    scan_packing()
    # pack the elements in the window


def scan_packing():
    # here you should add the packings in ordered form
    hostEntryFrame.pack(pady=20)
    rangeFrame.pack(pady=20)
    protocolFrame.pack(pady=20)
    featuresLabel.pack(pady=20)
    featuresFrame.pack()
    submitBtn.pack(pady=40)


def scan():
    scanner = Scanning(
        host=hostVar.get(),
        protocol=protocolVariable.get(),
        start=int(startVar.get()),
        stop=int(stopVar.get()),
        txt=txtVar.get(),
        csv=csVar.get(),
    )
    clear(
        hostEntryFrame,
        rangeFrame,
        protocolFrame,
        featuresLabel,
        featuresFrame,
        submitBtn,
        hide=True,
    )
    window.after(1000, lambda: threading.Thread(target=scanner.scan(), daemon=True))
    scan_packing()
    # fix not responding error


def Grabbing_GUI():
    clear(centralImage, btnFrame)
    title.configure(text="Banner Grabber")
    hostFrame = ttk.Frame(master=window)
    hostLabel = ttk.Label(master=hostFrame, text="Host:", font="Chiller 18 bold")
    if not "hostVar" in globals():
        global hostVar
        hostVar = ttk.StringVar()
    hostEntry = ttk.Entry(master=hostFrame, textvariable=hostVar)
    hostFrame.pack(pady=20)
    hostLabel.pack(side="left", padx=10)
    hostEntry.pack(side="left", padx=10)

    portFrame = ttk.Frame(master=window)
    portLabel = ttk.Label(master=portFrame, text="Port:", font="Chiller 18 bold")
    global portVar
    portVar = ttk.StringVar(value=80)
    portEntry = ttk.Entry(master=portFrame, textvariable=portVar)
    portFrame.pack(pady=20)
    portLabel.pack(side="left", padx=10)
    portEntry.pack(side="left", padx=10)

    # TCP or UDP
    protocolFrame = ttk.Frame(master=window)
    if not "protocolVariable" in globals():
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

    if not "txtVar" in globals():
        global txtVar
        txtVar = ttk.BooleanVar()
    txt = ttk.Checkbutton(
        master=window,
        text="TXT",
        style="round-toggle",
        variable=txtVar,
        onvalue=True,
        offvalue=False,
    )
    txt.pack()

    # submission button
    submit = ttk.Button(
        window, text="Grab", style="outline", command=grab, width=20, cursor="hand2"
    )
    submit.pack(side="bottom", pady=40)


def grab():
    grabber = Grabbing(hostVar.get(), int(portVar.get()), protocolVariable.get())
    if txtVar.get():
        window.after(
            1000, lambda: threading.Thread(target=grabber.save(), daemon=True).start()
        )
    else:
        window.after(
            1000, lambda: threading.Thread(target=print(grabber.grab()), daemon=True).start()
        )  # make it in the gui later


if __name__ == "__main__":
    main()


# Do some bug fixes!!
