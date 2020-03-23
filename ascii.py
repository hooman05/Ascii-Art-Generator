from PIL import Image, ImageDraw, ImageFont

import math

chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

scaleFactor = 0.3

oneCharWidth = 10
oneCharHeight = 18

def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]

print('first insure the image file is in the same directory as this python script.')

text_file = open("Output.txt", "w")

fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

def main(): 
    try:
        file_to_open = input('input filename with extention e.g.[.png / .jpg ect.]=> ')
        im = Image.open(file_to_open)
        width, height = im.size
        im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
        width, height = im.size
        pix = im.load()

        for i in range(height):
            for j in range(width):
                r, g, b = pix[j, i]
                h = int(r/3 + g/3 + b/3)
                pix[j, i] = (h, h, h)
                text_file.write(getChar(h))
            text_file.write('\n')

        out = open("Output.txt", "r")
        print(out.read())
    except:
        print("couldn't find that file :(")
        restart()

def restart():
    main()

main()
