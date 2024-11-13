from PIL import Image
import os
# import easygui
from easygui import *

def resizer():
    image_file = fileopenbox()
    filepath = os.path.join(os.getcwd(), image_file)

    filename, filextension = os.path.splitext(image_file)
    img = Image.open(filepath)
    text = "Enter quality on a scale of 10 to 100 (default value is 50)"

    if filextension == ".jpeg" or filextension == ".jpg":
        qual = integerbox(text,50,lowerbound=10,upperbound=100)
        img.save(
            filename + "_compressed" + ".jpeg",
            "JPEG",
            optimize= True,
            quality = qual
        )
        msgbox("Your compressed image has been saved in the orignal image folder")

    elif filextension == ".png":
        img.convert("P", palette=Image.ADAPTIVE,colors=256)
        img.convert("P", palette=Image.ADAPTIVE, colors=256)
        """Converts the image to an 8-bit palette mode with a maximum of 256 colors, 
        which can reduce the image size. "P" specifies the palette mode, and Image.
        ADAPTIVE uses an adaptive palette to maintain the quality as much as possible."""
        
        img.save(filename+"_compressed"+".png",optimize=True,quality = 10)
        msgbox("Please note that due to the file format being png it may not get compressed much")
        msgbox("Your compressed image has been saved in the orignal image folder")
        
    else:
        print("Invalid filetype")

    return

resizer()