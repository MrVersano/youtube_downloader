from __future__ import unicode_literals
import youtube_dl
import os


ydl_opts = {
    'nocheckcertificate': True,
    'format': 'bestaudio/best',
    # 'forcetitle': True,``
    'outtmpl': '/Users/kobi.versano/Downloads/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

url = 'https://www.youtube.com/watch?v=QNJL6nfu__Q'
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
    
