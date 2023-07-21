import os

base_path = os.getcwd()
base_path = os.path.join(base_path, "web_app")
base_path = os.path.join(base_path, "Youtube")


def removeVideo(file_path):
    os.remove(file_path)


import pytube
from pydub import AudioSegment

def mp4towav(video_path):
    mp4_file_path = video_path
    wav_file_path = os.path.join(base_path, 'youtube.wav')
    print('mp4 path', mp4_file_path)
    print('wav path', wav_file_path)
    
    audio = AudioSegment.from_file(mp4_file_path, format='mp4')
    audio.export(wav_file_path, format='wav')

    return wav_file_path

def saveVideo(url):
    data = pytube.YouTube(url)

    video = data.streams.filter(file_extension='mp4').first()         # video를 위한 mp4 download
    video_path = video.download(base_path) # file name 설정 필요

    # video rename
    base, ext = os.path.split(video_path)
    new_video_path = os.path.join(base,'youtube.mp4')
    os.rename(video_path, new_video_path)

    audio_path = mp4towav(new_video_path)

    print(audio_path)

    return new_video_path, audio_path
