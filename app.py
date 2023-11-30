from lib.ml_database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.book_repository import BookRepository
from lib.recipe_repository import RecipeRepository

# Connect to the database
connection = DatabaseConnection()
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

album = album_repo.find(1)
print(album)

# Connnect to book store database
connection.seed('seeds/book_store.sql')

book_repo = BookRepository(connection)
books = book_repo.all()

for book in books:
    print(book)


# Connect to recipe database

connection.seed('seeds/recipes.sql')

recipes_repo = RecipeRepository(connection)
recipes = recipes_repo.all()

for recipe in recipes:
    print(recipe)