Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        if not books:
            print("No books found.")
        else:
            print("\n*** Available Books ***")
            print("------------------------")
            for idx, book in enumerate(books, start=1):
                title, author, release_date, num_pages = book.split(',')
                print(f"{idx}. {title} by {author}")

    def add_book(self):
        print("\n*** Add a New Book ***")
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_date = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")
...         self.file.write(f"{title},{author},{release_date},{num_pages}\n")
...         print("Book added successfully.")
... 
...     def remove_book(self):
...         print("\n*** Remove a Book ***")
...         title = input("Enter the title of the book you want to remove: ")
...         self.file.seek(0)
...         books = self.file.readlines()
...         updated_books = [book for book in books if title not in book]
...         if len(books) == len(updated_books):
...             print(f"Book '{title}' not found.")
...         else:
...             self.file.seek(0)
...             self.file.truncate()
...             self.file.writelines(updated_books)
...             print(f"Book '{title}' removed successfully.")
... 
... 
... library_instance = Library()
... 
... while True:
...     print("\n*** Library Management System ***")
...     print("1) List Books")
...     print("2) Add Book")
...     print("3) Remove Book")
...     print("q) Exit")
...     choice = input("Enter your choice: ")
... 
...     if choice == "1":
...         library_instance.list_books()
...     elif choice == "2":
...         library_instance.add_book()
...     elif choice == "3":
...         library_instance.remove_book()
...     elif choice == "q":
...         print("Thank you for using the Library Management System. Goodbye!")
...         break
...     else:
...         print("Invalid choice. Please enter a valid option.")
