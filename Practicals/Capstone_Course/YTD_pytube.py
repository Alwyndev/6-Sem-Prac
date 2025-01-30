from pytube import YouTube


url = input("Enter the video url to download  :  ")
yt = YouTube(url)
downloader = yt.streams.get_highest_resolution()
print("Downloading ...")
downloader.download(filename=input("Enter the name to save the file as  :  "))
print("Finished Downloading!")
