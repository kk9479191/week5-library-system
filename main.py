from library_system.library import Library


def main():

    library = Library()

    while True:

        print("\n==============================")
        print("LIBRARY MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add Book")
        print("2. Register Member")
        print("3. View Books")
        print("4. View Members")
        print("5. Search Book")
        print("0. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":

            title = input("Book Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")

            library.add_book(
                title,
                author,
                isbn
            )

        elif choice == "2":

            name = input("Member Name: ")
            member_id = input("Member ID: ")

            library.register_member(
                name,
                member_id
            )

        elif choice == "3":

            library.view_books()

        elif choice == "4":

            library.view_members()

        elif choice == "5":

            keyword = input("Enter Book Name: ")

            library.search_book(keyword)

        elif choice == "0":

            print("Thank You")
            break

        else:

            print("Invalid Choice")