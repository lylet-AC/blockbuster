from PIL import Image
import os
from settings import *
import sys

def generate_map(in_file):
    im = Image.open(os.path.join(MAP_INPUT_FOLDER, in_file)) # Can be many different formats.
    im = im.resize((int(WIDTH / TILESIZE), int(HEIGHT*(.6)/TILESIZE)))
    pix = im.load()

    output_list = []
    line_list = []

    test = 0
    width, height = im.size

    for w in range(width):
        output_list.append([])
        for h in range(height):
            output_list[w].append(pix[w,h])

    return output_list

if __name__ == '__main__':

    if len(sys.argv) == 2:
         generate_map(sys.argv[1])
    else:
         print(" Usage: mapgen.py input_image.png")
         print(" For example: mapgen.py jpark.png")
         sys.exit(0)
