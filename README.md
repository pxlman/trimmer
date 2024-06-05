# Trimmer

A simple python script to trim a clip from a Youtube video with a fixed quality (>=480p).

## Requirements
- Python 3
- yt-dlp
- ffmpeg

## Instructions
1. Copy the Youtube video URL.
2. Run the script and paste the URL.
3. Enter the start time and end time of the clip. (Format: HH:MM:SS, ex: 00:01:30)
4. The script will download the video and trim the clip. (Only the clip will be there in the same folder of the script)

## Note
- The script will download the video in the worst quality available where it must be 360p or above.
- Currently choosing a specific quality is not supported.
- Arguments are not supported.
