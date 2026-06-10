"""brugerflade til protjekt"""

## imports ##

import tkinter
import vectorlib
import webbrowser
import matplotlib.backends.backend_tkagg as plttk
from matplotlib.figure import Figure
aop = "Sum"
toreturn = ""
## main window ##

def window():
    """vindue/GUI"""
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot()
    line = ax.plot(10,10)
    vindue = tkinter.Tk()
    vindue.title("GUI")
    vindue.geometry("750x400")
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
        v2label.config(text="V2:")
        v2label.config(state="normal")
        v2.config(state="normal")

    def Enhed():
        global aop
        aop = "Enhed"
        v2label.config(text="V2:")
        v2label.config(state="normal")
        v2.config(state="normal")

    def convkart():
        global aop
        aop = "Convkart"
        v2label.config(text="V2:")
        v2label.config(state="disable")
        v2.config(state="disable")
    
    def Convpol():
        global aop
        aop = "Convpol"
        v2label.config(text="V2:")
        v2label.config(state="disable")
        v2.config(state="disable")

    def punkt():
        global aop
        aop = "Punkt"
        v2label.config(text="V2:")
        v2label.config(state="normal")
        v2.config(state="normal")
    
    def tvær():
        global aop
        aop = "tvær"
        v2label.config(text="V2:")
        v2label.config(state="disable")
        v2.config(state="disable")

    def kryds():
        global aop
        aop = "kryds"
        v2label.config(text="V2:")
        v2label.config(state="normal")
        v2.config(state="normal")

    def show():
        webbrowser.open("https://github.com/KianS25R/protjektvector/blob/main/LICENSE")
    canvas = plttk.FigureCanvasTkAgg(fig, vindue)
    canvas.draw()
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
    operation.add_command(label="Protjekter", command=Protjekter)
    operation.add_command(label="Enhed", command=Enhed)
    operation.add_command(label="Kart -> Polær", command=convkart)
    operation.add_command(label="Polær -> kart", command=Convpol)
    operation.add_command(label="Punkter til Vektor", command=punkt)
    operation.add_command(label="Tværvektor", command=tvær)
    operation.add_command(label="Kryds", command=kryds)
    v1label = tkinter.Label(frame, text="V1:")
    v1label.place(x=0, y=25)
    v1 = tkinter.Entry(frame)
    v1.place(x=0, y=50)
    v2label = tkinter.Label(frame, text="V2:")
    v2label.place(x=150, y=25)
    v2 = tkinter.Entry(frame)
    v2.place(x=150, y=50)
    canvas.get_tk_widget().place(x=276, y=0)


    def dott():
        global aop
        global toreturn
        dotv1vec = str(v1.get()).replace("(", "").replace(")", "").split(",")
        dotv2vec = str(v2.get()).replace("(", "").replace(")", "").split(",")
        dotv1vec = [float(x) for x in dotv1vec]
        if aop != "Length" and dotv2vec[0] != "" and aop != "Convpol" and aop != "tvær":
            dotv2vec = [float(x) for x in dotv2vec]
            fuldvec2 = [*dotv1vec, *dotv2vec]
        if aop == "Length" or aop == "Convpol" or aop == "tvær" or aop == "Convkart" or (aop == "Vinkel" and dotv2vec[0] == ""):
            fuldvec2 = dotv1vec
        if len(dotv1vec) == 2:
            if aop == "Scalar":
                if len(dotv2vec) == 1:
                    toreturn = f"resultat: {vectorlib.Vektor2DGangeSkalar(*fuldvec2)}"
                    ax.clear()
                    ax.arrow(0, 0, vectorlib.Vektor2DGangeSkalar(*fuldvec2)[0], vectorlib.Vektor2DGangeSkalar(*fuldvec2)[1], length_includes_head=True, head_width=vectorlib.Vektor2DGangeSkalar(*fuldvec2)[0]/20, head_length=vectorlib.Vektor2DGangeSkalar(*fuldvec2)[1]/20)
                    ax.set_aspect('equal')
                    canvas.draw()
            if aop != "Scalar" and aop != "Length" and dotv2vec[0] != "":
                if len(dotv2vec) == 2:
                    if aop == "Sum":
                        toreturn = f"resultat: {vectorlib.Sum2DVektor(*fuldvec2)}"
                        ax.clear()
                        ax.arrow(0, 0, *dotv1vec, length_includes_head=True, head_width=dotv1vec[0]/20, head_length=dotv1vec[1]/20, color="blue")
                        ax.arrow(*fuldvec2, length_includes_head=True, head_width=dotv2vec[0]/20, head_length=dotv2vec[1]/20, color="red")
                        ax.arrow(0,0,*vectorlib.Sum2DVektor(*fuldvec2), length_includes_head=True, head_width=vectorlib.Sum2DVektor(*fuldvec2)[0]/20, head_length=vectorlib.Sum2DVektor(*fuldvec2)[1]/20, color="green")
                        ax.set_aspect('equal')
                        canvas.draw()
                    if aop == "Dot":
                        toreturn = f"resultat: {vectorlib.Prikprodukt2DVektor(*fuldvec2)}"
                    if aop == "Sub":
                        toreturn = f"resultat: {vectorlib.Differens2DVektor(*fuldvec2)}"
                        ax.clear()
                        ax.arrow(0, 0, *dotv1vec, length_includes_head=True, head_width=dotv1vec[0]/20, head_length=dotv1vec[1]/20, color="blue")
                        ax.arrow(*dotv1vec, -dotv2vec[0], -dotv2vec[1], length_includes_head=True, head_width=dotv2vec[0]/20, head_length=dotv2vec[1]/20, color="red")
                        ax.arrow(0, 0, *vectorlib.Differens2DVektor(*fuldvec2), length_includes_head=True, head_width=-vectorlib.Differens2DVektor(*fuldvec2)[0]/20, head_length=-vectorlib.Differens2DVektor(*fuldvec2)[1]/20, color="green")
                        ax.set_aspect('equal')
                        canvas.draw()
                    if aop == "Protjekter":
                        toreturn = f"resultat: {vectorlib.Projekter2DVektorUdFraKartesian(*fuldvec2)}"
                    if aop == "Enhed":
                        toreturn = f"resultat: {[round(x, 3) for x in vectorlib.EnhedsVektorFra2DVektor(*vectorlib.Sum2DVektor(*fuldvec2))]}"
                    if aop == "Vinkel":
                        toreturn = f"resultat: {vectorlib.VinkelIForholdTilHindanen2DVektor(*fuldvec2)}"
                    if aop == "Punkt":
                        toreturn = f"resultat: {vectorlib.Vektor2DFraPunkter(*fuldvec2)}"
                        ax.clear()
                        ax.arrow(*fuldvec2, length_includes_head=True, head_width=fuldvec2[2]/20, head_length=fuldvec2[3]/20)
                        ax.set_aspect('equal')
                        canvas.draw()
            if aop == "Length":
                toreturn = f"resultat: |V1| = {vectorlib.KartesianTilPolær2DVektor(*fuldvec2)[0]}"
            if aop == "Convkart":
                        toreturn = f"længde: {round(vectorlib.KartesianTilPolær2DVektor(*fuldvec2)[0], 4)} vinkel: {round(vectorlib.KartesianTilPolær2DVektor(*fuldvec2)[1], 4)}"
            if aop == "Convpol":
                toreturn = f"resultat: ({round(vectorlib.PolærTilKartesian2DVektor(*fuldvec2)[0], 4)}, {round(vectorlib.PolærTilKartesian2DVektor(*fuldvec2)[1], 4)})"
            if aop == "Vinkel" and dotv2vec[0] == "":
                toreturn = f"resultat: {vectorlib.KartesianTilPolær2DVektor(*fuldvec2)[0]}"
            if aop == "tvær":
                toreturn = f"resultat: ({vectorlib.TvaerVektor(*fuldvec2)[0]}, {vectorlib.TvaerVektor(*fuldvec2)[1]})"
                ax.clear()
                ax.arrow(0, 0, *fuldvec2, length_includes_head=True, head_width=fuldvec2[0]/20, head_length=fuldvec2[1]/20, color="blue")
                ax.arrow(0, 0, vectorlib.TvaerVektor(*fuldvec2)[0], vectorlib.TvaerVektor(*fuldvec2)[1], head_width=vectorlib.TvaerVektor(*fuldvec2)[0]/20, head_length=vectorlib.TvaerVektor(*fuldvec2)[1]/20, color="green")
                ax.set_aspect('equal')
                canvas.draw()
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
                    if aop == "Protjekter":
                        toreturn = f"resultat: {vectorlib.Projekter3DVektorUdFraKartesian(*fuldvec2)}"
                    if aop == "Vinkel":
                        toreturn = f"resultat: {vectorlib.VinkelIForholdTilHindanen3DVektor(*fuldvec2)}"
                    if aop == "Enhed":
                        toreturn = f"resultat: {[round(x, 3) for x in vectorlib.EnhedsVektorFra3DVektor(*vectorlib.Sum3DVektor(*fuldvec2))]}"
                    if aop == "Punkt":
                        toreturn = f"reslutat: {vectorlib.Vektor3DFraPunkter(*fuldvec2)}"
                    if aop == "kryds":
                        toreturn = f"resultat: {vectorlib.Krydsprodukt(*fuldvec2)}"
            if aop == "Length":
                toreturn = f"resultat: |V1| =  {vectorlib.Længde3DVektor(*fuldvec2)}"
        res.config(text=toreturn)

    dot = tkinter.Button(frame, text="Beregn", command=dott)
    res = tkinter.Label(frame, text="")
    dot.place(x=100, y=100)
    res.place(x=100, y=130)
    frame.place(x=0, y=0)
    lisence = tkinter.Menu(menu)
    menu.add_cascade(menu=lisence, label="License")
    lisence.add_command(label="Show License", command=show)
    vindue.config(menu=menu)
    vindue.update()


    vindue.mainloop()