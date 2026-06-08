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
    aop = "Sum"

    def sumq():
        global aop
        aop = "Sum"

    def dot():
        global aop
        aop = "Dot"

    def sube():
        global aop
        aop = "Sub"

    def scal():
        global aop
        aop = "Scalar"

    frame = tkinter.Frame(vindue, height=125, width=275, bg="#e9e9e9")
    menu = tkinter.Menu(vindue)
    operation = tkinter.Menu(menu)
    menu.add_cascade(menu=operation, label="Operation")
    operation.add_command(label="Sum", command=sumq)
    operation.add_command(label="Dot", command=dot)
    operation.add_command(label="Sub", command=sube)
    operation.add_command(label="Scalar", command=scal)
    v1label = tkinter.Label(frame, text="V1:")
    v1label.place(x=0, y=25)
    v1 = tkinter.Entry(frame)
    v1.place(x=0, y=50)
    v2label = tkinter.Label(frame, text="V2:")
    v2label.place(x=150, y=25)
    v2 = tkinter.Entry(frame)
    v2.place(x=150, y=50)


    def dott():
        global aop
        dotv1vec = str(v1.get()).replace("(", "").replace(")", "").split(",")
        dotv2vec = str(v2.get()).replace("(", "").replace(")", "").split(",")
        dotv1vec = [float(x) for x in dotv1vec]
        dotv2vec = [float(x) for x in dotv2vec]
        if len(dotv1vec) == 2:
            if aop == "Scalar":
                if len(dotv2vec) == 1:
                    pass
            if aop != "Scalar":
                if len(dotv2vec) == 2:
                    if aop == "Sum":
                        pass
                    if aop == "Dot":
                        pass
                    if aop == "Sub":
                        pass
        if len(dotv1vec) == 3:
            if aop == "Scalar":
                if len(dotv2vec) == 1:
                    pass
            if aop != "Scalar":
                if len(dotv2vec) == 3:
                    if aop == "Sum":
                        pass
                    if aop == "Dot":
                        pass
                    if aop == "Sub":
                        pass

    dot = tkinter.Button(frame, text="Beregn", command=dott)
    dot.place(x=100, y=100)
    frame.place(x=600, y=0)
    vindue.config(menu=menu)
    vindue.update()


    vindue.mainloop()