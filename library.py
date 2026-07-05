from library_system.book import Book
from library_system.member import Member


class Library:

    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author, isbn):

        book = Book(title, author, isbn)

        self.books.append(book)

        print("Book Added Successfully")

    def register_member(self, name, member_id):

        member = Member(name, member_id)

        self.members.append(member)

        print("Member Registered Successfully")

    def view_books(self):

        if not self.books:
            print("No Books Found")
            return

        for book in self.books:
            print(book)

    def view_members(self):

        if not self.members:
            print("No Members Found")
            return

        for member in self.members:
            print(member)

    def search_book(self, keyword):

        found = False

        for book in self.books:

            if keyword.lower() in book.title.lower():

                print(book)

                found = True

        if not found:
            print("Book Not Found")