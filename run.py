# import ffmpeg as ff
import yt_dlp as yt
from yt_dlp.utils import download_range_func
# Video link
link = input("Enter the youtube link: ")
# Start time
stime = input("Enter the start time: ")
hours, minutes, seconds = map(int, stime.split(":"))
stime = hours*3600 + minutes*60 + seconds
# End time
etime = input("Enter the end time: ")
hours, minutes, seconds = map(int, etime.split(":"))
etime = hours*3600 + minutes*60 + seconds
# Function to download the video
def download_video(youtube_link,start_time, end_time):
    yt_opts = {
        'verbose': False,
        'quiet': True,
        'format': 'worst[height>=360]',
        'download_ranges': download_range_func(None, [(int(start_time), int(end_time))]),
        'force_keyframes_at_cuts': True,
        
    }
    with yt.YoutubeDL(yt_opts) as ydl:
        info_dict = ydl.extract_info(youtube_link, download=False)
        # I the link is a playlist link
        if info_dict['webpage_url'].startswith('https://www.youtube.com/playlist?list='):
            video_id = input("Enter the video index from the playlist: ")
            yt_opts['playlist_items'] = video_id
            try:
                print("Please wait...")
                ydl.download([youtube_link])
            except:
                print("Invalid index/link/start time/end time")
        # If the link is a single video link
        elif info_dict['webpage_url'].startswith('https://www.youtube.com/watch?v='):
            print("Please wait...")
            ydl.download([youtube_link])
        # if the link is invalid
        else:
            print("Invalid link")
download_video(link,stime,etime)
