#!/usr/bin/python3

## TODO slice the image into chunks and do the average colors of pixel within those, slice will be proceeded according to a given size (width, height)
## process_image func will probably be divided in more subfunctions

from PIL import Image, ImageDraw, ImageFont
import math
import argparse


def pixToChar(value):
    chars = "@$B%8&WM#;:=+-'\". " [::-1]
    charArray = list(chars)
    interval = len(charArray) / 256
    return charArray[math.floor(value*interval)]
    

def write_pixel(gv, pixels, w, h, negative, image):
    if negative:
        gv = 255 - gv
        pixels[w,h] = (gv, gv, gv)
        image.write(pixToChar(gv))
    else:
        pixels[w,h] = (gv, gv, gv)
        image.write(pixToChar(gv))


def process_img(path:str, neg=False, out_path="output.nfo", scale=0.0009):
    out = open(out_path, "w")
    img = Image.open(path)
    width, height = img.size
    # img.resize((int(scale*width), int(scale*height)), Image.NEAREST)
    ## The image still too big to be displayed
    ## by doing the average of pixel color we doesnt need to resize the image (TODO maybe rezise to optimize pixel seeking)
    img.resize((16, 9))

    width, height = img.size
    pixels = img.load()

    print (width,height)

    for h in range(height):
        for w in range(width):
            r = pixels[w,h][0]
            g = pixels[w,h][1]
            b = pixels[w,h][2]

            gv = int(r/3 + g/3 + b/3)
            write_pixel(gv, pixels, w, h, neg, out)
            
        out.write('\n')
            
    # img.save("output.png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("img", help="path to the img you want to convert")
    
    parser.add_argument("-16", "--ansi", help="Converts the given image to an ANSI-art", action="store_true")
    parser.add_argument("-n", "--negative", help="inverts the image's colors", action="store_true")
    parser.add_argument("-o", "--output", help="path of the output")
    parser.add_argument("-s", "--scale", help="apply the given scale to the ascii art image")

    args = parser.parse_args()

    if args.negative:
        if args.output:
            process_img(args.img,neg=True,out_path=args.output)
        else:
            process_img(args.img,neg=True)
    else:
        if args.output:
            process_img(args.img,out_path=args.output)
        else:
            process_img(args.img)