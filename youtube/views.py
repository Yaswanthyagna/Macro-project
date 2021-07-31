from django.shortcuts import render, redirect
from django.http import HttpResponse
import youtube_dl
from django.contrib import messages
import re
import requests as r
import wget



# Create your views here.
def home(request):
    return render(request, 'pages/home.html')



def download_video(request):
    if request.method == 'POST':
        video_url = request.POST['url']
        if video_url:
            ydl_opts = {'outtmp1': 'D:/'}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            messages.success(request, 'Video Downloaded.')
            return redirect('home')
        else:
            messages.warning(request, 'Please Enter Video URL')
            return redirect('home')
    return redirect('home')



def facebook(request):
    if request.method == 'POST':
        LINK = input("Enter a Facebook Video Post URL: ")
        html = r.get(LINK)
        hdvideo_url = re.search('hd_src:"(.+?)"', html.text)[1]

        hd_url = hdvideo_url.replace('hd_src:"', '')
        wget.download(hd_url)
        return render(request,'pages/facebook.html')
    else:
        messages.warning(request, 'Please Enter Video URL')
        return redirect('facebook')
