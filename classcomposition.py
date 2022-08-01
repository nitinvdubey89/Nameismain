class Bookshelf:
    def __init__(self, quantity):
        self.quantity = quantity
        print("this is 2nd",id(quantity) )
        print(quantity)


    def __str__(self):
        return f"Bookshelf with {self.quantity} books"

shelf = Bookshelf(300)

class Book(Bookshelf): # this is conceptually wrong because i am saying a book is a booksheld
    def __init__(self,name,quantity):
        print(id(quantity))
        print(quantity)
        super().__init__(quantity)
        self.name = name

    def __str__(self):  ## this str as it did not call the self.quantity then no point inheriting
        return f"Book is {self.name}"

book = Book("Harry potter", 120)
print(book)



########### rewriting the above code as class composition way

class Bookshelf1:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books"

class Book3: # this is conceptually wrong because i am saying a book is a booksheld
    def __init__(self,name):
        self.name = name

    def __str__(self):  ## this str as it did not call the self.quantity then no point inheriting
        return f"Book is {self.name}"

book1 = Book3("Harry potter")
book2 = Book3("Harry potter")

shelf = Bookshelf1(book1, book2)

print(shelf)

### so composition is essentially a class that takes objects of many other claseses
# in addition we can have access to shelf.books and that gives you all the books stored within the book shelf
# whereas earlier you would not have had acecss to that
