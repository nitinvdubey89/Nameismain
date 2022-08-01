class TooManypagesreaderror(ValueError):
    pass


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
              f"{ self.name}, {self.page_count}, {self.pages_read}")

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManypagesreaderror(f"you tried to lot too many pages")

        self.pages_read +=  pages
        print(f"You have now read {self.pages_read} pages out of {self.page_count}.")

python101 = Book("PYTHON 101", 50)
try:
   python101.read(35)
   python101.read(50)
except TooManypagesreaderror as e:
    print(e)
finally:
    print("Thank  you")