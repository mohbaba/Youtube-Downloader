import os
from pytube import YouTube
from http.client import RemoteDisconnected


link = 'https://youtu.be/qwFBXuEeg1U'
home_dir = os.path.expanduser('~/Downloads')

def downloader():
    d_link = input('Paste link here: ')
    yt = YouTube(d_link)
    video = yt.streams.filter(res="720p",mime_type="video/mp4").first()
    video.download(output_path = home_dir)
    print(f'Downloaded to {os.path.join(home_dir, video.default_filename)}')
    


def file_path():
    
    pass


try:
    downloader()
except  RemoteDisconnected:
    print('Error: Failed to download video due to a connection error.')