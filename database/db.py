"""

This class creates table and dummy data into the database

"""

import sqlite3

DATABASE_NAME = "wishlist.sqlite"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS user(
                uid INTEGER PRIMARY KEY AUTOINCREMENT,
                firstName TEXT NOT NULL,
                lastName TEXT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                status TEXT NOT NULL
            )
            """,
        """CREATE TABLE IF NOT EXISTS wishlist(
                        wishlistId INTEGER PRIMARY KEY AUTOINCREMENT,
                        userId INTEGER NOT NULL,
                        wishlistName TEXT NOT NULL,
                        description TEXT,
                        bookIds TEXT,
                        FOREIGN KEY (userId) REFERENCES user(uid)
                    )
                    """,
        """CREATE TABLE IF NOT EXISTS books(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        author TEXT,
                        isbn TEXT NOT NULL,
                        dateOfPublication TEXT NOT NULL
                    )
                    """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)


def create_records():
    book_records = [("The Time Keeper1", "Mitch Albom", "978-1401312855", "July 23, 2021"),
                    ("The Time Keeper2", "Mitch Niffenegger", "978-0143125471", "August 23, 2021"),
                    ("The Time Keeper3", "Niffenegger Albom", "978-014312542123", "June 23, 2021"),
                    ("The Time Keeper4", " Albom", "978-01431254343", "Jan 23, 2021"),
                    ("The Time Keeper5", "Niffenegger", "978-01431254897", "Feb 23, 2021")]

    wishlist_records = [(1, "BirthdayGift", "test", "1,2"),
                        (2, "BusinessCategory", "978-test", "2,3"),
                        (3, "HorryStories", "978-test", "3,4"),
                        (4, "Leadership", "978-test", "4,5"),
                        (5, "Personal", "978-test", "5,1")]

    user_records = [("Andrew", "user", "test1@abc.com", "pwd1", "ACTIVE"),
                    ("Alex", "user", "test2@abc.com", "pwd1", "ACTIVE"),
                    ("Anna", "user", "test3@abc.com", "pwd1", "ACTIVE"),
                    ("Amex", "user", "test4@abc.com", "pwd1", "ACTIVE"),
                    ("Alan", "user", "test5@abc.com", "pwd1", "ACTIVE")]

    db = get_db()
    cursor = db.cursor()
    try:
        cursor.executemany('INSERT INTO wishlist(userId, wishlistName, description, bookIds ) VALUES(?,?,?,?);',
                       wishlist_records);
        print('We have inserted', cursor.rowcount, 'records to the table.')
    except Exception as error:
        print(error)

    try:
        cursor.executemany('INSERT INTO books(title, author, isbn, dateOfPublication) VALUES(?,?,?,?);', book_records);
        print('We have inserted', cursor.rowcount, 'records to the table.')
    except Exception as error:
        print(error)

    try:
        cursor.executemany('INSERT INTO user(firstName, lastName, email, password, status)  VALUES(?,?,?,?,?);',
                           user_records);
        print('We have inserted', cursor.rowcount, 'records to the table.')
    except Exception as error:
        print(error)

    db.commit()
