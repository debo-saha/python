from pytube import YouTube
YouTube('https://youtube.com/shorts/IeDoNizjY1M?si=rdhyk4lWODXiWTuu').streams.first().download()