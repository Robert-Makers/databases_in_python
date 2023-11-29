from lib.book import Book

class BookRepository():
    def __init__(self, connection):
        self._connnection = connection

    def all(self):
        rows = self._connnection.execute("SELECT * FROM books")
        books = []
        for row in rows:
            item = Book(row['id'], row['title'], row['author_name'])
            books.append(item)
            # print(item.id)
            # print(item.title)
            # print(item.author_name)
        return books