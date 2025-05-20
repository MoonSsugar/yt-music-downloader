from yt_dlp import YoutubeDL

async def download(url: str):
    ydl_opts = {
        "format": "m4a/bestaudio/best"
    }
    ydl = YoutubeDL(ydl_opts)
    with ydl:
        ydl.download(url)
