#200 300, pixely sachovnicovo striedaju
from PIL import Image

obr = Image.new('RGB',(200,300), 'pink')
pixels = obr.load()

for y in range(obr.size[1]):
    for x in range(obr.size[0]):
        if (x % 2 == 0 and y % 2 == 1) or (x % 2 == 1 and y % 2 == 0):
            pixels[x,y] = (0,60,150)
        
obr.show()


