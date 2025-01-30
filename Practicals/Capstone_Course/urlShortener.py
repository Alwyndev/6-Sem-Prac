import hashlib

# URL shortener logic
def id_to_short_url(id):
    map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    shortURL = ""

    # for each digit find the base 62 representation
    while (id > 0):
        shortURL += map[id % 62]
        id //= 62

    # reversing the shortURL
    return shortURL[::-1]

def short_url_to_id(shortURL):
    id = 0
    for i in shortURL:
        val_i = ord(i)
        if ord('a') <= val_i <= ord('z'):
            id = id * 62 + val_i - ord('a')
        elif ord('A') <= val_i <= ord('Z'):
            id = id * 62 + val_i - ord('A') + 26
        else:
            id = id * 62 + val_i - ord('0') + 52
    return id

# A simple dictionary to simulate a URL database
url_database = {}

# Function to generate short URL for a given full URL
def generate_short_url(full_url):
    # Create a unique ID for the URL by using a hash (could also use a counter)
    url_hash = hashlib.md5(full_url.encode()).hexdigest()  # use md5 to generate a hash
    url_id = int(url_hash, 16)  # convert hash to an integer
    short_url = id_to_short_url(url_id)  # convert the ID to a short URL

    # Store the full URL against the short URL
    url_database[short_url] = full_url
    print(url_database)

    return short_url

# Function to get the original URL from the short URL
def get_original_url(short_url):
    return url_database.get(short_url, "URL not found.")

if __name__ == "__main__":
    try:
        # For creating a short URL
        url_input = input("Enter the URL to shorten: ")
        short_url = generate_short_url(url_input)
        print(f"Shortened URL: {short_url}")

        # For retrieving the original URL from the short URL
        short_url_input = input("Enter a short URL to retrieve the original URL: ")
        original_url = get_original_url(short_url_input)
        print(f"Original URL: {original_url}")

    except ValueError:
        print("Invalid input. Please enter a valid URL.")
    except Exception as e:
        print(f"Error: {e}")
