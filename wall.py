from PIL import Image, ImageDraw, ImageFont
import os
import ctypes
import getinfo
import getsub

if __name__ == "__main__":
    # Step 1: gets the amount of subs
    channel_id = getinfo.get_item('id')
    subs = getsub.returnsubs(channel_id)

    # Step 2: generates an image
    filename = "img01.png"
    fnt = ImageFont.truetype('arial.ttf', 1000)
    image = Image.new(mode = "RGB", size = (1920,1080), color = "white")
    draw = ImageDraw.Draw(image)
    draw.text((80,10), subs, font=fnt, fill=(0, 0, 0))
    image.save(filename)


    # Step 3: sets it as backround
    PATH = (getinfo.get_item('path') + '\img01.png')
    SPI_SETDESKWALLPAPER = 20

    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, PATH, 3)