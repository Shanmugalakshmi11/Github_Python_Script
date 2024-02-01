class media():
    def __init__(self, title, author, year ):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")

class book(media):
    def __init__(self, title, author, year, num_pages ):
        super().__init__(title, author, year)  
        self.num_pages = num_pages

    def info_num_pages(self):
        print(f"No of Pages --> {self.num_pages}") 

mybook= book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 180)

mybook.info()
mybook.info_num_pages()

mymedia= media("The Great Gatsby", "F. Scott Fitzgerald", 1925)

class music(media):
    def __init__(self, title, author, year, genre ):
        super().__init__(title, author, year)  
        self.genre = genre

    def info_genre(self):
        print(f"Genre --> {self.genre}") 

mymusic= music("Thriller", "Michael Jackson", 1982, "Pop")

mymusic.info()
mymusic.info_genre()

mymedia= media("Thriller", "Michael Jackson", 1982)                

class film(media):
    def __init__(self, title, director, year, duration ):
        super().__init__(title, director, year)
        self.director = director  
        self.duration = duration 

    def info_duration(self):
        print(f"Director --> {self.director}")
        print(f"Duration --> {self.duration}") 

myfilm= film("Inception", "Christopher Nolan", 2010, 148)

myfilm.info()
myfilm.info_duration()

mymedia= media("Inception", "Christopher Nolan", 2010)  