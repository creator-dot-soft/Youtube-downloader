import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import download_file as dw

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YouDownLoader")
        self.geometry("600x300")
        self.resizable(width = False, height = False)
        self.create_elements()
    def create_elements(self):
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('TButton',padding=(30,10,30,10),background = "#4E4E56",focusthickness=3, focuscolor='none',relief="flat",font = "Arial 12 bold",foreground = "#f7f3e9")
        s.map("TButton",background = [("pressed","#4E4E56"),("active","#2a2a2e")])

        s.configure("TRadiobutton",padding=(30,10,30,10),background = "#4E4E56",focusthickness=3, focuscolor='none',relief="flat",font = "Arial 12 bold",foreground = "#f7f3e9")
        s.map("TRadiobutton",background = [("pressed","#4E4E56"),("active","#2a2a2e")])


        self.titleOfApp = tk.Label(self,text = "YouDownLoader",font = ("Arial",20,"bold"),bg="#DA635D",fg = "#f7f3e9")
        self.titleOfApp.pack(side = TOP,fill = X)

        self.frame = tk.Frame(self,bg="#4E4E56")
        self.frame.pack(expand = 1,fill = BOTH)
        self.var = IntVar()

        self.radioVideo = ttk.Radiobutton(self.frame,text = "Video",variable = self.var, value = 1)
        self.radioPlayList = ttk.Radiobutton(self.frame,text = "Playlist",variable = self.var, value = 2)
        self.radioChannel = ttk.Radiobutton(self.frame,text = "Channel",variable = self.var, value = 3)

        self.radioVideo.grid(row = 1,column = 1,sticky=N+S+W+E,pady = 10)
        self.radioPlayList.grid(row = 2,column = 1,sticky=N+S+W+E,pady = 10)
        self.radioChannel.grid(row = 3,column = 1,sticky=N+S+W+E,pady = 10)

        self.link = StringVar()
        self.inputLink = ttk.Entry(self.frame,background = "#f7f3e9",width = 50,font = "Arial 12 bold",textvariable = self.link)
        self.inputLink.grid(row = 1,column = 2,pady = 10)

        self.downloadButton = ttk.Button(self.frame,text = "Download",command = self.button_func)
        self.downloadButton.grid(row = 3,column = 2,pady = 10)
    def button_func(self):
        self.state = self.var.get()
        self.href = self.link.get()
        if(self.state == 1):
            dw.downloader.download_one_video(self.href)
        elif(self.state == 2):
            dw.downloader.download_video_from_playlist(self.href)
        elif(self.state == 3):
            dw.downloader.download_video_from_channel(self.href)
        elif(self.href == ""):
            messagebox.showwarning("Link","Copy past a link you want!")
        else:
            messagebox.showwarning("Type","Choose a type of downloading!")
app = App()
app.mainloop()