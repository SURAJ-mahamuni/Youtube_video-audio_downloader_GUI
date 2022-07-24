import tkinter as tk
from pytube import YouTube
from tkinter import *
from tkinter import filedialog, messagebox
def create1():
    #label youtube link
    link_label=Label(root,text="YouTube Link:",fg="#FFFFFF",bg="#FF0000")
    Font_tuple = ("Khand",10,"bold")
    link_label.configure(font=Font_tuple)
    link_label.grid(row=1,column=0,pady=5,padx=5)
    #youtube link entery box
    root.link_url=Entry(root,textvariable=video_url,width=60).grid(row=1,column=1,padx=5,pady=5)
    #file save label
    Destination=Label(root,text="Destination:",fg="#FFFF00",bg="#0277A2")
    Font_tuple = ("Khand",10,"bold")
    Destination.configure(font=Font_tuple)
    Destination.grid(row=2,column=0,pady=5,padx=5)
    #file save path
    root.Destination_en=Entry(root,textvariable=desti_path,width=60).grid(row=2,column=1,padx=3,pady=3)
    #browse button 
    browse_but=Button(root,text="Browse",command=browse,width=10).grid(row=2,column=2,padx=1,pady=1)
    #Quality select button
    menu.set("Select Quality")
    drop= OptionMenu(root,menu,"360p", "720p","1080p").place(x=100,y=80)
    #Download button
    download_but=Button(root,text="Download Video",width=15,command=Download_v).place(x=230,y=80)
    #doenload audio button
    audio_but=Button(root,text="Download Audio",width=15,command=audio_d).place(x=360,y=80)

def browse():
    download_dir=filedialog.askdirectory(initialdir="Your Directory Path")
    desti_path.set(download_dir)

def Download_v():
    url=video_url.get()
    folder=desti_path.get()
    get_video=YouTube(url)
    Quality_video=menu.get()
    if Quality_video=="360p":
        get_stream=get_video.streams.get_by_itag(18)
        get_stream.download(folder)
        messagebox.showinfo("Success!","Download Successfully!!!")
    elif Quality_video=="720p":
        get_stream=get_video.streams.get_by_itag(22)
        get_stream.download(folder)
        messagebox.showinfo("Success!","Download Successfully!!!")
    elif Quality_video=="1080p":
        get_stream=get_video.streams.get_by_itag(137)
        get_stream.download(folder)
        messagebox.showinfo("Success!","Download Successfully!!!")

def audio_d():
    url=video_url.get()
    folder=desti_path.get()
    get_video=YouTube(url)
    audio_f=get_video.streams.get_by_itag(251)
    audio_f.download(folder)
    messagebox.showinfo("Success!","Download Successfully!!!")

root=Tk()
root.title("YouTube Downloader")
root.geometry("600x150")
root.resizable(False,False)
video_url=StringVar()
desti_path=StringVar()
menu= StringVar()
create1()

root.mainloop()