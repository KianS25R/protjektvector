"""brugerflade til protjekt"""

## imports ##

import tkinter
import matplotlib

## main window ##

def window():
    """vindue/GUI"""
    vindue = tkinter.Tk()
    vindue.title("GUI")
    vindue.geometry("875x800")

    sumframe = tkinter.Frame(vindue, height=125, width=275, bg="#e9e9e9")
    v1label = tkinter.Label(sumframe, text="V1:")
    v1label.place(x=0, y=25)
    v1 = tkinter.Entry(sumframe)
    v1.place(x=0, y=50)
    v2label = tkinter.Label(sumframe, text="V2:")
    v2label.place(x=150, y=25)
    v2 = tkinter.Entry(sumframe)
    v2.place(x=150, y=50)


    difframe = tkinter.Frame(vindue, height=125, width=275, bg="#e9e9e9")
    difv1label = tkinter.Label(difframe, text="V1:")
    difv1label.place(x=0, y=25)
    difv1 = tkinter.Entry(difframe)
    difv1.place(x=0, y=50)
    difv2label = tkinter.Label(difframe, text="V2:")
    difv2label.place(x=150, y=25)
    difv2 = tkinter.Entry(difframe)
    difv2.place(x=150, y=50)


    dotframe = tkinter.Frame(vindue, height=125, width=275, bg="#e9e9e9")
    dotv1label = tkinter.Label(dotframe, text="V1:")
    dotv1label.place(x=0, y=25)
    dotv1 = tkinter.Entry(dotframe)
    dotv1.place(x=0, y=50)
    dotv2label = tkinter.Label(dotframe, text="V2:")
    dotv2label.place(x=150, y=25)
    dotv2 = tkinter.Entry(dotframe)
    dotv2.place(x=150, y=50)


    def dott():
        dotv1vec = str(dotv1.get()).replace("(", "").replace(")", "").split(",")
        dotv2vec = str(dotv2.get()).replace("(", "").replace(")", "").split(",")
        print(*dotv1vec, *dotv2vec)

    def summ():
        sumv1vec = str(v1.get()).replace("(", "").replace(")", "").split(",")
        sumv2vec = str(v2.get()).replace("(", "").replace(")", "").split(",")
        print(sumv1vec, sumv2vec)

    def diff():
        difv1float = float(difv1.get())
        difv2float = float(difv2.get())
        print(difv1float, difv2float)

    dot = tkinter.Button(dotframe, text="dot dem", command=dott)
    dot.place(x=100, y=100)
    dotframe.place(x=600, y=0)

    dif = tkinter.Button(difframe, text="minus dem", command=diff)
    dif.place(x=100, y=100)
    difframe.place(x=300, y=0)

    sumb = tkinter.Button(sumframe, text="læg sammen", command=summ)
    sumb.place(x=100, y=100)
    sumframe.place(x=0, y=0)

    vindue.mainloop()