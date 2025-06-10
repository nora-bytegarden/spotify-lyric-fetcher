import requests

def get_lyrics(song_title, artist):
    url = f"https://api.lyrics.ovh/v1/{artist}/{song_title}"
    response = requests.get(url)
    if response.status_code == 200:
        print("\nLyrics:\n")
        print(response.json()["lyrics"])
    else:
        print("Lyrics not found.")

if __name__ == "__main__":
    title = input("Enter song title: ")
    artist = input("Enter artist name: ")
    get_lyrics(title, artist)
