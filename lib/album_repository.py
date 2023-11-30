from lib.album import Album

class AlbumRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM albums')
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums
    
    def find(self, album_id):
        rows = self._connection.execute('SELECT * FROM albums WHERE id = %s', [album_id])
        album = Album(rows[0]['id'], rows[0]['title'], rows[0]['release_year'], rows[0]['artist_id'])
        return album
    
    def add(self, album):
        self._connection.execute(
            'INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)',
            [album.title, album.release_year, album.artist_id]
        )

    def delete(self, album_id):
        self._connection.execute(
            'DELETE FROM albums WHERE id = %s',
            [album_id]
        )