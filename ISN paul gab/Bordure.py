#!/usr/bin/env python
from  PIL import Image



def transfo(img):
    x,y=img.size
    img2 = Image.new("RGB",(x,y),"red")#(colonne,ligne)
    for i in range(x):
        for j in range(y):
            if i<50:
                R,G,B=0,0,255
            elif j<50:
                R,G,B=0,0,255
            elif i>x-50:
                R,G,B=0,0,255
            elif j>y-50:
                R,G,B=0,0,255
            else:
                R,G,B=img.getpixel((i,j))
                R=R
                G=G
                B=B
            img2.putpixel((i,j),(R,G,B))
    return img2

img = Image.open("pap2.jpg")
img.show()

img=transfo(img)

img.save("bordure.jpg")
img.show()

