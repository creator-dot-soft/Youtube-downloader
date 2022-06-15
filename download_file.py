from pytube import Playlist
from pytube import Channel
from pytube import YouTube
from tkinter import messagebox
import os
from winreg import *
#нахождение папки "Загрузки"
with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
    Downloads = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]



class Downloader():
    def __init__(self):
        self.mainDir = Downloads
        os.chdir(self.mainDir)
    def download_one_video(self,href):
        """Download one video"""
        self.video = YouTube(href).streams
        self.download(self.video,"video",None)
    def download_video_from_playlist(self,href):
        """Download from playlist"""
        self.videos = Playlist(href)
        self.nameOfDir = self.videos.playlist_id
        self.download(self.videos,"playlist",self.nameOfDir)
    def download_video_from_channel(self,href):
        """Download from channel"""
        self.videos = Channel(href)
        self.nameOfDir = self.videos.channel_name
        self.download(self.videos,"channel",self.nameOfDir)
    def download(self,videosArray,type,nameOfDir):
        """General download function"""
        messagebox.showinfo("Downloading...","Videos have started downloading")
        if(type != "video"):
            self.newPath = self.mainDir+f"\\{nameOfDir}"
            os.mkdir(self.newPath)
            os.chdir(self.newPath)

            for href_video in videosArray:
                print(href_video)
                filesStreams = YouTube(href_video).streams
                video = filesStreams.filter(mime_type="video/mp4").filter(res="720p").first()
                video.download()
                print(f"video uploaded {href_video}")
            os.chdir(self.mainDir)
        else:
            video = videosArray.filter(mime_type="video/mp4").filter(res="720p").first()
            video.download()
        messagebox.showinfo("Downloading...","Videos have downloaded")
downloader = Downloader()
