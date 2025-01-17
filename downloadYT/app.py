import yt_dlp

link = "https://youtu.be/4fndeDfaWCg?si=qWpaEq4i1OD_VUX_"

ydl_opts = {
    'format': 'best';
    'outtmpl': '%(titles)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
    