from pytube import YouTube

# YouTube video URL
video_url = input("Enter url of a video")

# Create a YouTube object
yt = YouTube(video_url)

# Get the highest resolution stream
stream = yt.streams.get_highest_resolution()

# Download the video
stream.download()

"""_
from pytube import Playlist

# URL of the YouTube playlist
playlist_url = 'https://www.youtube.com/playlist?list=PLAYLIST_ID_HERE'

# Create a Playlist object
playlist = Playlist(playlist_url)

# Loop through each video in the playlist
for video in playlist.videos:
    try:
        # Download the video
        video.streams.get_highest_resolution().download()
        print(f"Downloaded: {video.title}")
    except Exception as e:
        print(f"Error downloading {video.title}: {e}")
"""