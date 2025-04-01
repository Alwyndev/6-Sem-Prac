import yt_dlp


def download(url):
    ydl_opts = {'format': 'bestvideo[height <=2160]',
                'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == '__main__':
    video_url = input("Enter the Video url to Download  :   ")
    download(video_url)
