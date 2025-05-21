import tkinter as tk
from tkinter import *
import yt_dlp as Youtube
from tkinter import messagebox, filedialog



def Widgets():
    
    ## Head label
    head_label = Label(root, text="Youtube video Downloader using Tkinter", padx=15, pady=15, font=("Colibri 15"), bg="palegreen1", fg="red")
    head_label.grid(row=1, column=1, pady=10, padx=5, columnspan=3)
    
    ## Label for links
    link_label = Label(root, text="Link for youtube", bg="salmon", pady=5, padx=5,)
    link_label.grid(row=2, column=0, pady=5, padx=5,)
    
    ## Textbox for link
    root.linkText = Entry(root, width=35,textvariable=video_link, font= "Arial 14")
    root.linkText.grid(row=2, column=1, padx=5, pady=5)
    
    ## Label for destination
    destination_label = Label(root, text="Destination :", bg="salmon", pady=5, padx=9)
    destination_label.grid(row=3, column=0, padx=5, pady=5)
    
    ## Textbox for destinations
    root.destinationText = Entry(root, width=27, textvariable=download_path, font="Arial 14 ")
    root.destinationText.grid(row=3, column=1, padx=5,pady=5)
    
    ## button to browse directory
    button_browse= Button(root, text="Browse",command=browse,width=10,bg="bisque",relief=GROOVE)
    button_browse.grid(row=3, column=2, padx=1, pady=1)
    
    ## Button to start download
    button_download = Button(root, text="Download Video", command=download_video, width=20, bg= "white", padx=15, pady=10, relief=GROOVE, font="Georgia,13")
    button_download.grid(row=4, column=1, padx=20, pady= 20)
    
    ## function to open file dialog for destination download
def browse():
    download_directory=filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="Save Video")
    download_path.set(download_directory)
    
    ## Function to start the download of the video
def download_video():
    youtube_link = video_link.get()
    download_folder = download_path.get()
    try:
        ydl_opts = {'outtmpl': f'{download_folder}/%(title)s.%(ext)s'}
        with Youtube.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_link])
        messagebox.showinfo("Success", f"Download saved in \n {download_folder}")
    except Exception as e:
        messagebox.showerror("Error", "Error when trying to download the requested video")
        print(e)
    
    ## Variables related to tkinter
root = tk.Tk()
root.geometry("600x280")
root.resizable(False, False)
root.title("Youtube Video Downloader")
root.config(background="PaleGreen1")

video_link = StringVar()
download_path= StringVar()

Widgets()

root.mainloop()
