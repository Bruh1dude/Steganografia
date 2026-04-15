#400 400 obrazok, stvorit mriekzky 20 na 20, dalej ciary 20 odseba, dalej schody 20 vysoke a 20 siroke, a dve ciary ktore idu z rohov
from PIL import Image, ImageDraw

pic = Image.new("RGB", (400, 400), "white")
draw = ImageDraw.Draw(pic)
pixels = pic.load()

a1 = 200
a2 = 200
a3 = 200
a4 = 399
b1 = 399
b2 = 399
b3 = 399
b4 = 200

A1 = (a2 - b2)/(a1 - b1)
B1 = a2 - a1 * ((a2-b2)/(a1-b1))
A2 = (a4 - b4)/(a3 - b3)
B2 = a4 - a3 * ((a4-b4)/(a3-b3))

for i in range(0,201,20):
        draw.line((i,0,i,200), width=1, fill="black")
        draw.line((0,i,200,i), width=1,fill="black")
for i in range(200,401,20):
     draw.line((i,0,200,i-200),width=1, fill="black")
for i in range(0,201,20):
     draw.line((i,200+i,i,200 + (i+20)),width=1, fill="black")
     draw.line((i,220+i,(i+20),i+220),width=1,fill="black")
if (pic.size[0] and pic.size[1])  > 199:
    if abs(a2 - b2) > abs(a1 - b1):
        for y1 in range(a2, b2 + 1):
            x = round((y1-B1)/A1)
            pixels[x,y1] = (0, 0, 0)   
        for y2 in range(a4, b4 + 1):
            x = round((y2-B2)/A2)
            pixels[x,y2] = (0, 0, 0)    
    else:
        for x1 in range(a1, b1 + 1):
            y = round((A1*x1)+B1)
            pixels[x1,y] = (0, 0, 0)
        for x2 in range(a3, b3 + 1):
            y = round((A2*x2)+B2)
            pixels[x2,y] = (0, 0, 0)
pic.show()

