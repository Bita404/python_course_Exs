import requests
import json

track_name = "grace"
Url = f"https://itunes.apple.com/search?term={track_name}&media=music"
respond = requests.get(Url)

if respond.status_code == 200:
    data = respond.json() 
else:
    print(f"{respond.status_code}:Failed!")
    
