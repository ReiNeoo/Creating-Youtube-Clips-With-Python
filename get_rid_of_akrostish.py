import os
import time
from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

from termcolor import colored

class akrostish_parent:
    def __init__(self) -> None:
        pass

    def create_directory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def hour_minute_second_converter(self, target_time: str): # saat dakika saniye formatını sadece saniyeye dönüştüren kod
        hours, minutes, seconds = map(int, target_time.split(':'))
        calc_seconds = hours *3600 + minutes *60 + seconds 
        return calc_seconds

class akrostish(akrostish_parent):
    def __init__(self, video_url: str ,video_path: str, clips_path: str, download_res: str = "720p") -> None:
        self.video_url = video_url
        self.video_dir = video_path
        self.clips_dir = clips_path

        self.create_directory(video_path)
        self.create_directory(clips_path)

        self.download_res = download_res

    def download_the_video(self): #viyo indiren kod
        yt = YouTube(self.video_url)
        available_streams = yt.streams.filter(progressive=True, file_extension='mp4')
        stream = available_streams.filter(progressive=True, file_extension='mp4', resolution= self.download_res).first()

        print(colored("Yayına ulaşıldı...", "light_green"))

        video_dir_path = os.path.join(self.video_dir, yt.title)

        if stream is None:
            print(colored("Spesifik çözünürlükte yayın bulunamadı. Mevcut Çözünürlük: ", "red"))
            for s in available_streams:
                print(s.resolution)
        else:
            if not os.path.exists(video_dir_path):
                print(colored("vidyo indiriliyor", "blue", attrs= ["bold"]))
                stream.download(video_dir_path)
                print(colored("vidyo başarıyla indirildi...", "blue", attrs= ["bold"]))
            else:
                print(colored("vidyo zaten var...", "blue"))
    
    def cut_clip_from_video(self, input_path, clip_name, start_time, end_time): # klip alan kod
        start_time_seconds = self.hour_minute_second_converter(start_time)
        end_time_seconds = self.hour_minute_second_converter(end_time)
        
        clip_dir_path = os.path.join(self.clips_dir, clip_name)
        clip_dir_path = clip_dir_path + ".mp4"

        ffmpeg_extract_subclip(input_path, start_time_seconds, end_time_seconds, clip_dir_path) #Asıl kesme işleminin gerçekleştiği yer

        print(colored("{} isimli klip kaydedildi...".format(clip_name), "green", attrs= ["bold"]))