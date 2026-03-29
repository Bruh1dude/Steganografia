from PIL import Image

sprava = input("zadaj mi spravu :")
obr = "Nature.png"


def sprava_to_bin(message):
    message += '#'
    output = ''
    for char in message:
        temp = bin(ord(char))[2::]
        if len(temp) < 7:
            pocet = 7 - len(temp)
            temp = '0'*pocet + temp
        output += temp
    return output

def picture_shreder(bin_message,pic,pic2):
    obr = Image.open(pic).convert("RGB")
    pixels = obr.load()
    for i in range (len(bin_message)):
        x = i % obr.size[0]
        y = i// obr.size[0]
        blue_bin = bin(pixels[x,y][2])[2:-1:]
        blue_bin = blue_bin + bin_message[i]
        new_blue = int(blue_bin, 2)
        pixels[x,y] = (pixels[x,y][0], pixels[x,y][1], new_blue)
    obr.save(pic2)





obr_out = 'sprava.png'


bin_message = sprava_to_bin(sprava)
picture_shreder(bin_message, obr, obr_out)
