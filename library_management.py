
class library:
    def __init__(self,books):
        self.books=books

    def list_books(self):
        print("Available books: ")
        for books in self.books:
            print(books)
    def borrow_books(self,borrow_books):
        print("borrows_books")
        if borrow_books in self.books:
            print("Get your book now!")
            self.books.remove((borrow_books))
        else:
            print("not found")
    def recevie_books(self,recevie_books):
        print("You have return the book")
        self.books.append(recevie_books)
books=["c","c++","java","python"]
o=library(books)
msg='''
LIBRARY MANAGEMENT SYSTEM
 --------------------
   1.display books
   2.borrow books
   3.return books
 --------------------
'''
while True:
    print(msg)
    ch=int(input("Enter your choice:"))
    if ch==1:
        o.list_books()
    elif ch==2:
        book=input("Enter the book to borrow:")
        o.borrow_books(book)
    elif ch==3:
        book=input("Enter the book to return:")
        o.recevie_books(book)
    else:
        print("Thank You")
        quit()