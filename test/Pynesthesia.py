from PIL import Image
import os

def generate_map():
    # Constants:
    # folder Pynesthesia is in:
    root_folder = os.path.dirname(__file__)
    # folder for input file
    input_folder = os.path.join(root_folder, "input")
    # folder for sprites
    sprite_folder = os.path.join(root_folder, "sprites")
    # folder for output
    output_folder = os.path.join(root_folder, "output")
    # tile size for images being drawn over input pixels
    tile_size = 16
    # Colors
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)

    im = Image.open(os.path.join(input_folder, "jpark.jpeg")) # Can be many different formats.
    im = im.resize((59, 59))
    pix = im.load()



    width, height = im.size
    print (im.size)  # Get the width and hight of the image for iterating over
    #print (pix[1,1])  # Get the RGBA Value of the a pixel of an image
    #pix[x,y] = value  # Set the RGBA Value of the image (tuple)
    #im.save('alive_parrot.png')  # Save the modified pixels as .png

    output_image = Image.new("RGB", (tile_size*width, tile_size*height), "white")
    # Loads all the tiles into the program
    block = Image.open(os.path.join(sprite_folder, "block.png"))
    block = block.resize((tile_size, tile_size))



    for w in range(width):
        for h in range(height):
            #if the color is black:
            if (pix[w,h] == BLACK):
                #print("BLACK")
                output_image.paste(block, (w*tile_size, h*tile_size, w*tile_size+tile_size , h*tile_size+tile_size), mask=None)

        #print("Endline")

    print("OUTPUT INFO: ", output_image.size)
    output_image.show(title=None, command="xv")

    output_image.save(os.path.join(output_folder, "gen_map.png"))

    print (im.size)  # Get the width and hight of the image for iterating over

generate_map()
