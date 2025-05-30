# YoutubeDownloader

Simple YouTube video and audio downloader built with Python and Tkinter. You paste a link, choose where to save it, and it downloads either MP4 or MP3.

## Features

- Download YouTube videos as MP4  
- Download audio as MP3  
- Choose where to save the file  
- Basic GUI interface  
- Shows progress messages

## Requirements

- Python 3.12+
- ffmpeg (for MP3 conversion)

Install the required packages:

```bash
pip install pytube moviepy
```

If you don't have ffmpeg, install it from https://ffmpeg.org/download.html and make sure it's added to your system PATH.

## How to Run

Clone the repo and run the app:

```bash
git clone https://github.com/EqualNoches/YoutubeDownloader.git
cd YoutubeDownloader
python main.py
```

## How to Use

1. Paste a YouTube URL  
2. Choose a folder to save the file  
3. Click **Download Video** 
4. Wait for it to finish (you'll see messages)

## Folder Structure

```
YoutubeDownloader/
│
├── assets/            # Icons or other files
├── screenshots/       # App preview images (optional)
├── downloader.py      # Handles download logic
├── main.py            # Starts the GUI
└── README.md          # This file
```

## Notes

- The GUI might freeze a bit during downloads. It still works.
- If MP3 isn’t working, make sure ffmpeg is installed and set up correctly.

## Author

Made by [@EqualNoches](https://github.com/EqualNoches)
