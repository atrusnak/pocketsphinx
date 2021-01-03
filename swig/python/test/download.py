import os
import subprocess
import youtube_dl
from pydub import AudioSegment



def downloadVideos(urls):
    ydl_opts = {
        'outtmpl': 'swig/python/test/data/test2.mp3',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)





downloadVideos(["https://www.youtube.com/watch?v=YjY7kQGG1Ps&ab_channel=GMHikaru"])
#toWav("videoMp3s/test.mp3","videoWavs/test.wav")

#for /r %i in (*) do ffmpeg -i %i -acodec pcm_s16le -ac 1 -ar 16000 %i.wav
os.chdir('C:/Users/alex/Documents/GitHub/pocketsphinx/swig/python/test/data')
subprocess.call(['ffmpeg', '-i', "test2.mp3", "-acodec", "pcm_s16le", "-ac", "1", "-ar", "16000", "test2.wav"])
