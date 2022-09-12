from PIL import Image
import numpy as np
import os 
import datetime

picture = "<picture>.jpg"
name = ""
for i in range(len(picture)-4):
    name += picture[i]
im = Image.open(picture, "r")
WIDTH, HEIGHT = im.size
pix_val = list(im.getdata())
pix_val = np.array(pix_val).reshape((WIDTH, HEIGHT, 3))
bright = []
chars = ["1", "0"]
time = datetime.datetime.now()
tag = time.strftime("%M%S")
revert = False
spacing = False

def luminescence(r, g, b):
    return (r + g + b) / 3

def pxl_char(n):
    if revert == False:
        return round((n-5)/255 * 2) + 1
    else:
        return round ((n-5)/255 * 2)

def main():

    for i in pix_val:
        for j in i:
            bright.append(luminescence(j[0], j[1], j[2]))
    bright_np = np.array(bright).reshape(HEIGHT, WIDTH)
    pic = ""
    if revert == False:
        for i in bright_np:
            for j in i:
                pic += chars[-pxl_char(j)]
                if spacing:
                    pic += " "
            pic += "\n"
    else:
        for i in bright_np:
            for j in i:
                pic += chars[pxl_char(j)]
                if spacing:
                    pic += " "
            pic += "\n"
    
    # ONLY WORKS ON MAC-OS crate folder named digitalImages in project directory, edited photos apper here
    os.system(f"touch digitalImages/{name}{tag}.txt & echo '{pic}' >> digitalImages/{name}{tag}.txt")

if __name__ == "__main__":
    main()