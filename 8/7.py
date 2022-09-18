def make_album(artist_name, album_title, songs=''):
    """function to get the favourite album from artist"""
    if songs:
        album = {'name': artist_name.title(),'title': album_title.title(), 'songnumber': songs}
    else:
        album = {'name': artist_name.title(), 'title':album_title.title()}
    return(album)

while True:
    
    print("\nPlease tell me what about an artist and an album:")
    print("(enter 'q' at any time to quit)")

    a_name=input("Artist name:")
    if a_name == 'q':
        break
    al_name = input("Album title:")
    if al_name == 'q':
        break

    album_info = make_album(a_name, al_name)
    print(album_info)
