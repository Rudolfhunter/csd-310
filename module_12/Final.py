#code from class- Allows a user to connect to the database
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}
#db = mysql.connector.connect(**config)
try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to conintue....")
finally: 
    exit
#Defining cursor
cursor = db.cursor()

#Function to login

def login():
    print("Welcome to WhataBook mobile app!")
    user_account = input("Do you have a user account? Enter 1 for yes and 2 for no.")
    if user_account == "1":
        print("Great!")
        user_id = input("What is your user ID?")
        user_id2 = tuple(user_id)
        try:
            cursor.execute(f"Select user_id FROM user WHERE user_id = (%s)", (user_id2))
            print("Account found!")
        except:
            print("Account not found")
            login()
    elif user_account == "2":
        print("Please create a free account.")
        user_email = input("What is your email?")
        user_first = input("What is your first name?")
        user_last = input("What is your last name?")
        cursor.execute(f"INSERT INTO user (first_name, last_name) VALUES(%s, %s)", (user_first, user_last))
        user_first = list(user_first)
        cursor.execute(f"SELECT user_id, first_name FROM user where first_name = (%s)", (user_first))
        test = cursor.fetchall()
        print("Your user id is: {}".format(test[0]))
        print("Thank you! Your account has been created!")
    else:
        login()
    return user_id
#now = login()

#List of books
def books():
    config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
    }
    db = mysql.connector.connect(**config)
    now = input("What is your User ID")
    now = tuple(now)
    print("-- List of Books --")
    try:
        cursor.execute("SELECT book_id, book_name, details, author FROM book")
        inventory = cursor.fetchall()
        for novels in inventory:
            print("Book ID: {}".format(novels[0]))
            print("Book Name: {}".format(novels[1]))
            print("Description: {}".format(novels[2]))
            print("Author: {}".format(novels[3]))
            print()
                
    except: 
        print("An error has occured please try again")
        menu()
    menu()


#view store location and hours
def store():
    print("-- STORE LOCATION AND HOURS --")
    try:
        cursor.execute("SELECT store_id, locale FROM store")
        locations = cursor.fetchall()
        for location in locations:
            print("Store ID: {}".format(location[0]))
            print("Location: {}".format(location[1]))
            print("Store Hours: M-S 9-5")
            print()
    except:
        menu()
    menu()
        
#View wishlist
def wishlist():
    config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
    }
    db = mysql.connector.connect(**config)
    now = input("What is your User ID")
    now = tuple(now)        
    cursor.execute(f"SELECT book.book_name from wishlist INNER JOIN book ON wishlist.book_id=book.book_id WHERE user_id = (%s)", (now))
    wishlist_books = cursor.fetchall()
    print("-- WISHLIST BOOKS --")
    try: 
        for book in wishlist_books:
            print(f"Book Name: {book}")
            print()
            wishlist_add()
    except: 
        menu()
    menu()
        
# add books to wishlist
def add_wishlist():
    config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
    }
    db = mysql.connector.connect(**config)
    now = input("What is your User ID")
    now = tuple(now)
    user_input = input("Do you want to add a book to your wishlist? Press 1 for yes 2 for no.")
    if user_input == "1":
        books()
        print("Please type the book ID you would like to add to your wishlist")
        add_book = input()
        add_book = tuple(add_book)
        print(now)
        cursor.execute(f"INSERT INTO wishlist (user_id, book_id) VALUES(%s, %s)", (now, add_book))
        print("The book has been added to your wishlist!")
        try: 
            cursor.execute(f"INSERT INTO wishlist (user_id, book_id) VALUES(%s, %s)", (now, add_book))
            print("The book has been added to your wishlist!")
        except:
            print("The book was unable to be added to your wishlist.")
            menu()
    elif user_input == "2":
        now = str(now)
        menu()
    menu()
#Menu
def menu():
    print("Press 1 to view of list of books available, press 2 to view your wishlist, press 3 to view store hours and locations.")
    response = input()
    if response == "1":
        books()
    elif response == "2":
        wishlist()
    elif response == "3":
        store()

#start program
#login()
menu()
#wishlist()
#books()