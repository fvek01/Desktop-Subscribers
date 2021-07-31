import urllib.request
import json
import getinfo

def returnsubs(name):
    key = getinfo.get_item('key')
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+name+"&key="+key).read()
    return json.loads(data)["items"][0]["statistics"]["subscriberCount"]