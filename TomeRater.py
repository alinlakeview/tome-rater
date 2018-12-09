class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
        
    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("User email has been updated")

    def __repr__(self):
        ret = "User {}, email: {}, books read: {}".format(
            self.name,self.email,len(self.books))
        return ret

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        if rating != None:
            self.books[book] = rating
        
        

    def get_average_rating(self):
        ratings = list(self.books.values())
        average = sum(ratings)/len(ratings)
        #print(average)
        return average
    


        
class Book:
    def __init__(self,title,isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __repr__(self):
        ret = "{} by {}".format(self.title, self.isbn)
        return ret

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self,new_isbn):
        self.isbn = new_isbn
        print("This book's ISBN has been updated")

    def add_rating(self,rating):
        if rating != None and rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        #else:
         #   print("Invalid Rating", rating)

    def get_average_rating(self):
        average = sum(self.ratings)/len(self.ratings)
        return average
                

    def __eq__(self,other_book):
        if self.title == other_book:
            return True
        else:
            return False
        
    def __hash__(self):
        
        return hash((self.title, self.isbn))
 
class Fiction(Book):
    def __init__(self,title,author,isbn):
        super().__init__(title,isbn)
        self.author = author
    def get_author(self):
        return self.author
    def __repr__(self):
        ret = "{} by {}".format(self.title, self.author)
        return ret

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
        
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level

    def __repr__(self):
        ret = "{}, a {} manual on {}".format(self.title,self.level,self.subject)
        return ret


class TomeRater:
    def __init__(self):
        self.users = {} # key: email addr,  val: user obj
        self.books = {} # key: book obj,  val: count of users

    def create_book(self,title,isbn):
        new_book = Book(title,isbn)
        print(new_book)
        return new_book
    def create_novel(self,title,author,isbn):
        new_nov = Fiction(title,author,isbn)
        return new_nov
    def create_non_fiction(self,title,subject,level,isbn):
        new_nf = Non_Fiction(title,subject,level,isbn)
        return new_nf
    def add_book_to_user(self, book, email,rating=None):
        
        if email in self.users:
            user = self.users[email]
            user.read_book(book,rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {}".format(email))

    def add_user(self,name,email,user_books=None):
        new_user = User(name,email)
        self.users[email] = new_user
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book,email)

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users:
            print(user)

    def most_read_book(self):
        max_count = 0
        most_read = None
        for book, count in self.books.items():
            if count > max_count:
                max_count = count
                most_read = book
        return most_read

    def highest_rated_book(self):
        best_book = None
        high_rating = 0
        for book in self.books:
            rating = book.get_average_rating()
            if rating > high_rating:
                high_rating = rating
                best_book = book
        return best_book

    def most_positive_user(self):
        pos_user = None
        high_rating = 0

        for user in self.users.values():
            rating = user.get_average_rating()
            if  rating > high_rating:
                high_rating = rating
                pos_user = user
        #print("in most_positive_user  pos_user is", pos_user)
        return pos_user

    def __repr__(self):
        ret = "Readers in our group; {}".format(len(self.users))
        print(ret)

    def __eq__(self,other_TR):
        # return True if self.users and self.books are identical
        if self.users == other_TR.users and self.books == other_TR.books:
            return True
        else:
            return False
    
        
        

if __name__ == "__main__":
    fred = User('Fred Smith', 'fs@gmail.com')
    print(fred)
    book1 = Book('Merry', 123)
    book2 = Book('Blah', 356)
    nfb1 = Non_Fiction("Society of the Mind","AI","beginner", 345)
    fred.read_book(book1, 2)
    fred.read_book(book2, 3)
    print('Fred:  ', fred)
    print('avg rating')
    print(fred.get_average_rating())
    print(nfb1.__repr__())

    tr = TomeRater()
    bk = tr.create_book("The rise and fall","Godot")
    print('new book is', bk)
    Alfred = User("Alfred", "fred@nowhere.com")
    nu = tr.add_user("Alfred","fred@nowhere.com", [bk])
    ww = tr.create_book("Wind in the Willows", "Carroll")
    print("new book is", ww)
    for reader in tr.users:
        print(reader)

    import copy
    tr2 = copy.deepcopy(tr)
    print('Equal? :', tr == tr2)




    

    

    # addbook = TomeRater()
    # newbook = addbook.add_book_to_user("Wind in the willows", "fred@nowhere.com",4)
    # print(newbook)
    
 
          
    
