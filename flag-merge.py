from PIL import Image
import glob
import os

path = ("./output/")

try: 
    os.makedirs(path)
except OSError:
    if not os.path.isdir(path):
        raise

flags = glob.glob("*.png")
print flags

while flags:
    currFlag = flags.pop()
    for f in flags:
        background = Image.open(currFlag)
        overlay = Image.open(f)
		
        backgroundName = currFlag.replace(".png","")
        overlayName = f.replace(".png","")

        background = background.convert("RGBA")
        overlay = overlay.convert("RGBA")

        new_img = Image.blend(background, overlay, 0.5)
        new_img.save("./output/"+backgroundName+"-"+overlayName+".png","PNG")
