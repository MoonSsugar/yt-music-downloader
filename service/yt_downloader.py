from yt_dlp import YoutubeDL

async def download(url: str, id: str):
    ydl_opts = {
        "format": "m4a/bestaudio/best",
        "ffmpeg_location": "d:\\bin\\ffmpeg.exe",
        "outtmpl": id+"\\%(title)s.%(ext)s",
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
    }]
}
    ydl = YoutubeDL(ydl_opts)
    with ydl:
        ydl.download(url)
