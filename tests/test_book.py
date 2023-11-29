from lib.book import Book

'''
Book is constructed with id, title and author
'''
def test_book_constucts_with_arguments():
    book = Book(1, "The Neverending Story", "Michael Ende")
    assert book.id == 1
    assert book.title == "The Neverending Story"
    assert book.author_name == "Michael Ende"

'''
Test format book string
'''
def test_format_book():
    book = Book(1, "The Neverending Story", "Michael Ende")
    assert str(book) == "Book(1, The Neverending Story, Michael Ende)"