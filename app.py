from lib.ml_database_connection import MusicDatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.bs_database_connection import BookDatabaseConnection
from lib.book_repository import BookRepository

# Connect to the database
connection = MusicDatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# List them out
for artist in artists:
    print(artist)

# Retrieve all albums
album_repo = AlbumRepository(connection)
albums = album_repo.all()

for album in albums:
    print(album)

# Connnect to book store database
book_connection = BookDatabaseConnection()
book_connection.connect()

book_connection.seed('seeds/book_store.sql')

book_repo = BookRepository(book_connection)
books = book_repo.all()

for book in books:
    print(book)