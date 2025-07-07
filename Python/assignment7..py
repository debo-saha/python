# Problem 2: Library System

#! In this task, you will build a simple library management system using classes and functions.

# Instructions:

#? Create a class Book with the following attributes:

#* title
#* author
#* isbn
#* available_copies (number of available copies of the book)
#* Create a class Library with the following methods:

#? add_book(book) – Adds a new book to the library collection.
#? remove_book(isbn) – Removes a book by its ISBN.
#? borrow_book(isbn) – Reduces the available copies of the book when it is borrowed. If no copies are available, display an error message.
#? return_book(isbn) – Increases the available copies when a book is returned.
#? In your Library class, implement the following additional methods:

#? search_by_title(title) – Searches for books by title.
#? list_books() – Displays a list of all books in the library with their details.
#? Create a few Book instances and demonstrate borrowing, returning, and searching functionality.


class Book:
    def __init__(self,title,author,isbn,available_copies=0):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.available_copies=available_copies

    def __str__(self):
        return f"Title:{self.title} , Author:{self.author} ,ISBN:{self.isbn} ,Available Copies:{self.available_copies}"

class Library:
    def __init__(self):
        self.book_collection={}
    def add_book(self,book):
        if book.isbn in self.book_collection:
            self.book_collection[book.isbn].available_copies+=book.available_copies
            print(f"'{book.title}' updated Successfully with new copies .Available Copies {self.book_collection[book.isbn].available_copies} .")
        else:
            self.book_collection[book.isbn]=book
            print(f"'{book.title}' Added Successfully .")
    def remove_book(self,isbn):
        if isbn in self.book_collection:
            del self.book_collection[isbn]
            print(f"The Book with '{isbn}' is removed succesfully .")
        else:
            print(f'The Book With "{isbn}" Not found .')
    def borrow_book(self,isbn):
        if isbn in self.book_collection:
            copies=self.book_collection[isbn]
            if copies.available_copies>0:
                copies.available_copies-=1
                print(f'Book Borrowed Succesfully . The remaining copies ares {copies.available_copies} .')
            else:
                print("Not Enough Quantity is availabe .")
        else :
            print(f'No Book Found with {isbn} isbn Number .')
    def return_book(self,isbn):
        if isbn in self.book_collection:
            copies=self.book_collection[isbn]         
            copies.available_copies+=1
            print(f'Book Returned Succesfully . Total copies ares {copies.available_copies} .')           
        else :
            print(f'No Book Found with {isbn} isbn Number .')


    def search_by_title(self):
        book_search=str(input("Enter The Book Name to search :"))
        results=[book for book in self.book_collection.values()
            if book_search.lower() in book.title.lower()]
        if not results:
            print("NO Search Found !!!")
        else:
            print("Your Desired Books are :")
            for book in results:
                print(book)

    def list_books(self):
        if self.book_collection:
            print("List of book in the library:")
            for book in self.book_collection.values():
                print(book)
        else:
            print("There is no book in Liibrary.")
        
 


book1=Book('ML For the beginers','A.J Roy',11111,1)
book2=Book('The era of AI','R Ramakrisnan',22222,8)
book3=Book('Math is galaxy','R g l',44444,10)
book4=Book('A to Z','DSaha',33333,18)


library=Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.remove_book(11111)
library.borrow_book(44444)
library.borrow_book(33333)
library.return_book(22222)
library.search_by_title()
library.list_books()
