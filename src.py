from pytubefix import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

import os
import sys

def download_yt(link):
    stream = YouTube(link, client='WEB_CREATOR').streams.first()
    return stream.download(output_path="./", filename="test.mp4")

yt_path = ''
start_end = []

if len(sys.argv) <= 1:
    print("pass an argument")
    exit()

with open(str(sys.argv[1])) as f:
    lines = f.read().splitlines()
    for i in range(len(lines)):
        if(i == 0):
            yt_path = download_yt(lines[i])
        else:
            start_end.append(lines[i])
    f.close()

if(yt_path == ''):
    print("yt path never came")
    exit()

savefile = "clip"
it = 0

def convert_time(time_str):
    minu, sec = map(float, time_str.split(':'))
    return minu*60.0 + sec

for i in range(0, len(start_end), 2):
    ffmpeg_extract_subclip(yt_path, convert_time(start_end[i]), convert_time(start_end[i+1]), targetname=savefile+str(it)+".mp4")
    print(start_end)
    it+=1

os.remove(yt_path)
