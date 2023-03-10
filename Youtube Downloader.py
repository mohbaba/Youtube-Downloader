import os
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
    print("{:.1%} downloaded".format(progress))


def downloader():
    
    d_link = input('Paste link here: ')
    yt = YouTube(d_link , on_progress_callback=progress_bar)
    video = yt.streams.filter(res="720p",mime_type="video/mp4").first()
    video.download(output_path = home_dir)
    print(f'Downloaded to {os.path.join(home_dir, video.default_filename)}' , end='\n')
    



    
    

# def file_path():
    
#     pass


try:
    downloader()
except  RemoteDisconnected:
    print('Error: Failed to download video due to a connection error.')