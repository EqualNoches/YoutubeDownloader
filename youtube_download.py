import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog



def Widgets():
    
    head_label = Label(root, text="Youtube video Downloader using Tkinter", padx=15, pady=15, font=("Colibri 15"), bg="palegreen1", fg="red")
    head_label.grid(row=1, column=1, pady=10, padx=5, columnspan=3)
    
    link_label = Label(root, text="Link for youtube", bg="salmon", pady=5, padx=5,)
    link_label.grid(row=2, column=0, pady=5, padx=5,)
    
    root.linkText = Entry(root, width=35,textvariable=video_link, font= "Arial 14")
    root.linkText.grid(row=2, column=1, padx=5, pady=5, columnspan=2)
    
    root.destinationText = Entry(root, width=27, textvariable=download_path, font="Arial 14 ")
    root.destinationText.grid(row=3, column=1, padx=5,pady=5)
    
    button_browse= Button(root, text="Browse",command=browse,width=10,bg="bisque",relief=GROOVE)
    button_browse.grid(row=3, column=3, padx=1, pady=1)
    
    button_download = Button(root, text="Download Video", command=download_video, width=20, bg= "thistlel", padx=15, pady=10, )
    
def browse():
    download_directory=filedialog.askdirectory(initialdir="Your directory path", title="Save Video")
    download_path=set(download_directory)
    
def download_video():
    youtube_link = video_link.get()
    download_folder = download_path.get()
    get_video= YouTube(youtube_link)
    video_stream = get_video.streams.first()
    video_stream.download(download_folder)
    messagebox.showinfo("Success", "Download saved in \n {download_destination}" .format(download_destination = download_folder))
    
    
root = tk.Tk()
root.geometry("520x280")
root.resizable(False, False)
root.title("Youtube Video Downloader")
root.config(background="PaleGreen1")

video_link = StringVar()
download_path= StringVar()

Widgets()

root.mainloop()
