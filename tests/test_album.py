from lib.album import Album

'''
Album constructs with a title, release year, artist id and id
'''
def test_albums_constructs():
    album = Album(1, 'Artpop', 2013, 1)
    assert album.id == 1
    assert album.title == 'Artpop'
    assert album.release_year == 2013
    assert album.artist_id == 1

"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    album = Album(1, "Test Artist", 2000, 1)
    assert str(album) == "Album(1, Test Artist, 2000, 1)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    album_1 = Album(1, "Test Artist", 2000, 1)
    album_2 = Album(1, "Test Artist", 2000, 1)
    assert album_1 == album_2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.
