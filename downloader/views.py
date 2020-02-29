from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import youtube_dl
import os

STATIC_URL = 'downloader/static/'

# Create your views here.
def home(request):
    # Remove all mp3 files in static folder
    file_list = os.listdir(STATIC_URL)
    for file in file_list:
        os.remove(os.path.join(STATIC_URL, file))


    # Get the YouTube video if a URL was submitted
    if request.GET.get('yturl'):
        yturl = request.GET.get('yturl')
    
        ydl_opts = {
        'nocheckcertificate': True,
        'format': 'bestaudio/best',
        'forcetitle': True,
        'outtmpl': f'{STATIC_URL}%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
        

        url = yturl
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            filename = f"{ydl.extract_info(url, download=False)['title']}.mp3"
            print(f"Filename: {filename}.mp3")
            ydl.download([url])
        
        # fsock = open(f'{STATIC_URL}{filename}', 'r')
        # response = HttpResponse(fsock, content_type='audio/mpeg')
        # response['Content-Disposition'] = f"attachment; filename={STATIC_URL}{filename}"
        # return response
        with open(f'{STATIC_URL}{filename}', 'rb') as mp3:
            response = HttpResponse(mp3.read())
            response['content_type'] = 'audio/mpeg'
            response['Content-Disposition'] = f'attachment;filename={filename}'
            return response

    return render(request, 'downloader/home.html')