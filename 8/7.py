def make_album(artist, album, tracks='0'):
    album_dict = {
            'artist': artist.title(),
            'album': album.title()
            }   
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

title_prompt = "\n What are you thinking of? "
artist_prompt = "\n Who's the artist?"

print("Enter quit at any time to stop")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\n Thanks for respodnding")
