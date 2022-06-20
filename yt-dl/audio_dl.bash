#youtube-dl -x --audio-format mp3 video_URL
youtube-dl -o '/mnt/c/Users/gians/Desktop/yt-dl/videos/%(title)s.%(ext)s' -x $1
echo $1
