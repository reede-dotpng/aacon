from PIL import Image, ImageDraw, ImageFont
import math
import argparse




def process_img(path:str):
    img = Image.open(path)
    width, height = img.size
    pixels = img.load()

    print (width,height)

    for h in range(height):
        for w in range(width):
            r = pixels[w,h][0]
            g = pixels[w,h][1]
            b = pixels[w,h][2]
            print(r,g,b)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("img", help="path to the img you want to convert")
    group.add_argument("-8", "--ascii", help="Converts the given image to an ASCII-art (default)", action="store_true")
    group.add_argument("-16", "--ansi", help="Converts the given image to an ANSI-art", action="store_true")

    args = parser.parse_args()

    process_img(args.img)