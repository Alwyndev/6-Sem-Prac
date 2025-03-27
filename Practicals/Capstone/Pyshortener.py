import pyshorteners
url = input("Enter the URL to shorten  :  ")
shortUrl = pyshorteners.Shortener().tinyurl.short(url)
print(f"Shortened URL : {shortUrl} ")

# print(pyshorteners.Shortener().available_shorteners)
