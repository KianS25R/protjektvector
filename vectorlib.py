import math

def Sum2DVektor(x1,y1,x2,y2):
    x=x1+x2
    y=y1+y2
    return(x,y)

def Sum3DVektor(x1,y1,z1,x2,y2,z2):
    x=x1+x2
    y=y1+y2
    z=z1+z2
    return(x,y,z)

def Differens2DVektor(x1,y1,x2,y2):
    x=x1-x2
    y=y1-y2
    return(x,y)

def Differens3DVektor(x1,y1,z1,x2,y2,z2):
    x=x1-x2
    y=y1-y2
    z=z1-z2
    return (x,y,z)

def Vektor2DGangeSkalar(x,y,s):
    x=x*s
    y=y*s
    return (x,y)

def Vektor3DGangeSkalar(x,y,z,s):
    x=x*s
    y=y*s
    z=z*s
    return (x,y,z)

def KartesianTilPolær2DVektor(x,y):
    længde=math.sqrt(x**2+y**2)
    vinkelMedXAksen=math.degrees(math.atan(y/x))
    return (længde,vinkelMedXAksen)

def Længde3DVektor(x,y,z):
    længde=math.sqrt(x**2+y**2+z**2)
    return længde

def PolærTilKartesian2DVektor(længde,vinkel):
    x=længde*math.cos(math.radians(vinkel))
    y=længde*math.sin(math.radians(vinkel))
    return (x,y)

def Prikprodukt2DVektor(x1,y1,x2,y2):
    prikprodukt=x1*x2+y1*y2
    return prikprodukt

def Prikprodukt3DVektor(x1,y1,z1,x2,y2,z2):
    prikprodukt=x1*x2+y1*y2+z1*z2
    return prikprodukt

def VinkelIForholdTilHindanen2DVektor(x1,y1,x2,y2):
    vinkel=math.degrees(math.acos((x1*x2+y1*y2)/(math.sqrt(x1**2+y1**2)*math.sqrt(x2**2+y2**2))))
    return vinkel

def VinkelIForholdTilHindanen3DVektor(x1,y1,z1,x2,y2,z2):
    vinkel=math.degrees(math.acos((x1*x2+y1*y2+z1*z2)/(math.sqrt(x1**2+y1**2+z1**2)*math.sqrt(x2**2+y2**2+z2**2))))
    return vinkel

def Vektor2DFraPunkter(x1,y1,x2,y2):
    x=x2-x1
    y=y2-y1
    return (x,y)

def Vektor3DFraPunkter(x1,y1,z1,x2,y2,z2):
    x=x2-x1
    y=y2-y1
    z=z2-z1
    return (x,y,z)

def Pilpunkt2DVektor(x1,y1,x2,y2):
    x=x1+x2
    y=y1+y2
    return (x,y)

def Pilpunkt3DVektor(x1,y1,z1,x2,y2,z2):
    x=x1+x2
    y=y1+y2
    z=z1+z2
    return (x,y,z)

#FørsteVærdiErVektorenOgAndenErPilpunktet#
def Startpunkt2DVektor(x1,y1,x2,y2):
    x=x2-x1
    y=y2-y1
    return (x,y)

#FørsteVærdiErVektorenOgAndenErPilpunktet#
def Startpunkt3DVektor(x1,y1,z1,x2,y2,z2):
    x=x2-x1
    y=y2-y1
    z=z2-z1
    return (x,y,z)

def TvaerVektor(x,y):
    x1=-y
    y1=x
    x2=y
    y2=-x
    return(x1,y1,"eller",x2,y2)

def EnhedsVektorFra2DVektor(x,y):
    return 0

def EnhedsVektorFra3DVektor(x,y,z):
    return 0

def Krydsprodukt(x,y,z):
    return 0

def Projekter2DVektor(x1,y1,x2,y2):
    return 0

def Projekter3DVektor(x1,y1,z1,x2,y2,z2):
    return 0
