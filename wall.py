from PIL import Image, ImageDraw, ImageFont
import os
import ctypes
import getinfo
import getsub
import time
from datetime import datetime

def update():
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

if __name__ == "__main__":
    while True:
        try:
            update()
        except:
            with open("Error_Log.txt", "a") as f:
                now = datetime.now()
                dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
                f.write(dt_string + "An error has occured\n")
        wait_time = 10
        time.sleep(wait_time * 60)

