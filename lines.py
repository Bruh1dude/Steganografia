from PIL import Image

pic = Image.new("RGB",(100, 100),"black")

pixels = pic.load()

A = input("zadaj suradnice prveho bodu (rozsah 0-99): ")
B= input("zadaj suradnice druheho bodu (rozsah 0-99): ")

a1, a2 = A.split()
a1 =int(a1)
a2 = int(a2)

b1, b2 = B.split()
b1 = int(b1)
b2 = int(b2)

if (a1 or a2 or b1 or b2) == 100:
    print("Error, suradnica 100 nefunguje")

if a1 > b1:
     a1, b1 = b1, a1
     a2, b2 = b2, a2
if a1 != b1:
    a = (a2 - b2)/(a1 - b1)
    b = a2 - a1 * ((a2-b2)/(a1-b1))

    if abs(a2 - b2) > abs(a1 - b1):
        for y in range(a2, b2 + 1):
            x = round((y-b)/a)
            pixels[x,y] = (0, 0, 0)      
    else:
        for x in range(a1, b1 + 1):
            y = round((a*x)+b)
            pixels[x,y] = (215, 0, 64) 
else:
    a = 1
    x = a1
    if b2 < a2:
         a2,b2 = b2,a2
    for y in range(a2, b2+1):
            pixels[x,y] = (215, 0, 64)        
    
pic.show()

