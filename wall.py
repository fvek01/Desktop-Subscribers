from PIL import Image, ImageDraw, ImageFont
import ctypes
import urllib.request
import json
import time
from datetime import datetime

def get_item(item):
    if item == 'id':
        line = 0
        char = 11
    elif item =='key':
        line = 1
        char = 8
    elif item == 'path':
        line = 2
        char = 5
    load_profile = open('notes.txt', "r")
    read_it = load_profile.read().splitlines()[line]
    read_it = read_it[char:]
    return read_it

def returnsubs(name):
    try:
        key = get_item('key')
    except:
        with open("Error_Log.txt", "a") as f:
                now = datetime.now()
                dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
                f.write(dt_string + " Could not get api key from notes.txt\n")
    try:
        data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+name+"&key="+key).read()
        return json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    except:
        with open("Error_Log.txt", "a") as f:
                now = datetime.now()
                dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
                f.write(dt_string + " Could not get channel statistics from youtube api. COuld be due to incorrect api key or channel id.\n")

def update():
    # Step 1: gets the amount of subs
    try:
        channel_id = get_item('id')
    except:
        with open("Error_Log.txt", "a") as f:
                now = datetime.now()
                dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
                f.write(dt_string + " Could not get channel id from notes.txt\n")
    subs = returnsubs(channel_id)

    # Step 2: generates an image
    filename = "img01.png"
    fnt = ImageFont.truetype('arial.ttf', 1000)
    image = Image.new(mode = "RGB", size = (1920,1080), color = "white")
    draw = ImageDraw.Draw(image)
    draw.text((80,10), subs, font=fnt, fill=(0, 0, 0))
    image.save(filename)


    # Step 3: sets it as backround
    try:
        PATH = (get_item('path') + '\img01.png')
    except:
        with open("Error_Log.txt", "a") as f:
                now = datetime.now()
                dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
                f.write(dt_string + " Could not get PATH from notes.txt\n")
    SPI_SETDESKWALLPAPER = 20

    try:
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, PATH, 3)
    except:
        with open("Error_Log.txt", "a") as f:
                now = datetime.now()
                dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
                f.write(dt_string + " PATH is not valid.\n")

if __name__ == "__main__":
    while True:
        try:
            update()
        except:
            with open("Error_Log.txt", "a") as f:
                now = datetime.now()
                dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
                f.write(dt_string + " An error has occured\n")
        wait_time = 10
        time.sleep(wait_time * 60)

