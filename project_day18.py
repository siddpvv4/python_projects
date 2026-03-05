import random
import string

urls = {}

def shorten(url):
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    urls[key] = url
    return key

def get_url(key):
    return urls.get(key, "Not found")

while True:
    print("1.Shorten URL 2.Open URL 3.Exit")
    ch = input()

    if ch == "1":
        url = input("Enter URL: ")
        print("Short code:", shorten(url))

    elif ch == "2":
        code = input("Enter code: ")
        print("Original URL:", get_url(code))

    else:
        break