class Book:
    def __init__(self,title,author,year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")
        print("~" * 20)

book1 = Book("To Kill Mockingbird", "Harper Lee", 2020)
book2 = Book("The Last White Hunter", "Donald Anderson with Joshua Mathew", 2018)
book3 = Book("The Testaments", "Margaret Atwood", 2019)

book1.describe()
book2.describe()
book3.describe()
