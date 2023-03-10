import os
from flet import *
from pytube import YouTube
from http.client import RemoteDisconnected 
import sys
import math


link = 'https://youtu.be/Hxj2nNVm2QI'
home_dir = os.path.expanduser('~/Downloads/TEST')


def progress_bar(stream,chunk, bytes_remaining):
    # Get the file size in bytes
    file_size = stream.filesize

    # Calculate the percentage of bytes that have been downloaded
    size = stream.filesize
    progress = (size - bytes_remaining) / size
    
    # Define the granularity (in percentage points) at which to display progress
    granularity = 10
    
    # Calculate the number of percentage points to round down to
    progress_floor = math.floor(progress * 100 / granularity) * granularity

    # Only display progress if it has changed since the last update
    if hasattr(progress_bar, 'last_update') and progress_floor == progress_bar.last_update:
        return
    progress_bar.last_update = progress_floor

    # Display the progress
    print("{:.0%} downloaded".format(progress))


def downloader(d_link):
    
    # d_link = input('Paste link here: ')
    yt = YouTube(d_link , on_progress_callback=progress_bar)
    video = yt.streams.filter(res="720p",mime_type="video/mp4").first()
    video.download(output_path = home_dir)
    print(f'Downloaded to {os.path.join(home_dir, video.default_filename)}' , end='\n')
    

def download_video():
    d_link = input('Paste link here: ')
    thread = threading.Thread(target=downloader, args=(d_link,))
    thread.start()

try:
    download_video()
except  RemoteDisconnected:
    print('Error: Failed to download video due to a connection error.')