"""brugerflade til protjekt"""

## imports ##

import tkinter
import vectorlib
aop = "Sum"
toreturn = ""
## main window ##

def window():
    """vindue/GUI"""
    vindue = tkinter.Tk()
    vindue.title("GUI")
    vindue.geometry("275x155")
    global aop
    global toreturn

    def sumq():
        global aop
        aop = "Sum"
        v2label.config(text="V2:")
        v2label.config(state="normal")
        v2.config(state="normal")

    def dot():
        global aop
        aop = "Dot"
        v2label.config(text="V2:")
        v2label.config(state="normal")
        v2.config(state="normal")

    def sube():
        global aop
        aop = "Sub"
        v2label.config(text="V2:")
        v2label.config(state="normal")
        v2.config(state="normal")

    def scal():
        global aop
        aop = "Scalar"
        v2label.config(text="S:")
        v2label.config(state="normal")
        v2.config(state="normal")
    def length():
        global aop
        aop = "Length"
        v2label.config(state="disabled")
        v2.config(state="disabled")

    def vinkel():
        global aop
        aop = "Vinkel"
        v2label.config(text="V2:")
        v2label.config(state="normal")
        v2.config(state="normal")
    
    def Protjekter():
        global aop
        aop = "Protjekter"

    frame = tkinter.Frame(vindue, height=155, width=275, bg="#e9e9e9")
    menu = tkinter.Menu(vindue)
    operation = tkinter.Menu(menu)
    menu.add_cascade(menu=operation, label="Operation")
    operation.add_command(label="Sum", command=sumq)
    operation.add_command(label="Dot", command=dot)
    operation.add_command(label="Sub", command=sube)
    operation.add_command(label="Scalar", command=scal)
    operation.add_command(label="Længde", command=length)
    operation.add_command(label="Vinkel", command=vinkel)
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
        global toreturn
        dotv1vec = str(v1.get()).replace("(", "").replace(")", "").split(",")
        dotv2vec = str(v2.get()).replace("(", "").replace(")", "").split(",")
        dotv1vec = [float(x) for x in dotv1vec]
        if aop != "Length" and dotv2vec[0] != "":
            dotv2vec = [float(x) for x in dotv2vec]
            fuldvec2 = [*dotv1vec, *dotv2vec]
        if aop == "Length" or (aop == "Vinkel" and dotv2vec[0] == ""):
            fuldvec2 = dotv1vec
        if len(dotv1vec) == 2:
            if aop == "Scalar":
                if len(dotv2vec) == 1:
                    toreturn = f"resultat: {vectorlib.Vektor2DGangeSkalar(*fuldvec2)}"
            if aop != "Scalar" and aop != "Length" and dotv2vec[0] != "":
                if len(dotv2vec) == 2:
                    if aop == "Sum":
                        toreturn = f"resultat: {vectorlib.Sum2DVektor(*fuldvec2)}"
                    if aop == "Dot":
                        toreturn = f"resultat: {vectorlib.Prikprodukt2DVektor(*fuldvec2)}"
                    if aop == "Sub":
                        toreturn = f"resultat: {vectorlib.Differens2DVektor(*fuldvec2)}"
                    if aop == "Vinkel":
                        toreturn = f"resultat: {vectorlib.VinkelIForholdTilHindanen2DVektor(*fuldvec2)}"
            if aop == "Length":
                toreturn = f"resultat: |V1| = {vectorlib.KartesianTilPolær2DVektor(*fuldvec2)[0]}"
            
            if aop == "Vinkel" and dotv2vec[0] == "":
                toreturn = f"resultat: {vectorlib.KartesianTilPolær2DVektor(*fuldvec2)[0]}"
        if len(dotv1vec) == 3:
            if aop == "Scalar":
                if len(dotv2vec) == 1:
                    toreturn = f"resultat: {vectorlib.Vektor3DGangeSkalar(*fuldvec2)}"
            if aop != "Scalar" and aop != "Length" and dotv2vec[0] != "":
                if len(dotv2vec) == 3:
                    if aop == "Sum":
                        toreturn = f"resultat: {vectorlib.Sum3DVektor(*fuldvec2)}"
                    if aop == "Dot":
                        toreturn = f"resultat: {vectorlib.Prikprodukt3DVektor(*fuldvec2)}"
                    if aop == "Sub":
                        toreturn = f"resultat: {vectorlib.Differens3DVektor(*fuldvec2)}"
                    if aop == "Vinkel":
                        toreturn = f"resultat: {vectorlib.VinkelIForholdTilHindanen3DVektor(*fuldvec2)}"
            if aop == "Length":
                toreturn = f"resultat: |V1| =  {vectorlib.Længde3DVektor(*fuldvec2)}"
        res.config(text=toreturn)

    dot = tkinter.Button(frame, text="Beregn", command=dott)
    res = tkinter.Label(frame, text="")
    dot.place(x=100, y=100)
    res.place(x=100, y=130)
    frame.place(x=0, y=0)
    vindue.config(menu=menu)
    vindue.update()


    vindue.mainloop()