from lib.album import Album

'''
Album constructs with a title, release year, artist id and id
'''
def test_albums_constructs():
    album = Album(1, 'Artpop', 2013, 'Pop')
    assert album.id == 1
    assert album.title == 'Artpop'
    assert album.release_year == 2013
    assert album.genre == 'Pop'