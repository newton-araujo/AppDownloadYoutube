import yt_dlp
class Download:
    def __init__(self,url,paste) -> None:
        
        self.url = url
        self.paste = paste
    
    
    def download_video(self,url,paste):
        yt_opts = {
            'format':'best',
            'outtmpl':f'{paste}/%(title)s.%(ext)s'
        }
        
        try:
            with yt_dlp.YoutubeDL(yt_opts) as ydl:
                ydl.download([url])
            return "Download concluído!"
        
        except Exception as e:
            return f"Ocoreeu um erro:{e}"
