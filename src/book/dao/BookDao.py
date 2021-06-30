"""

BookDao class - CRUD operations for the Book resource thru REST

"""


from database.db import get_db


def insert_book(title, author, isbn, dop):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO books(title, author, isbn, dateOfPublication) VALUES (?, ?, ?, ?)"
    cursor.execute(statement, [title, author, isbn, dop])
    db.commit()
    return True


def update_book(id, title, author, isbn, dop):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE books SET title=?, author=?, isbn=?, dateOfPublication =? WHERE id= ?"
    cursor.execute(statement, [title, author, isbn, dop, id])
    db.commit()
    return True


def delete_book(bookid):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM books WHERE id = ?"
    cursor.execute(statement, [bookid])
    db.commit()
    return True


def get_by_id(bookid):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, title, author, isbn, dateOfPublication FROM books WHERE id = ?"
    cursor.execute(statement, [bookid])
    desc = cursor.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))
            for row in cursor.fetchall()]
    return data


def get_books():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, title, author, isbn, dateOfPublication FROM books"
    cursor.execute(query)
    desc = cursor.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))
            for row in cursor.fetchall()]
    return data


def get_bookids(ids):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, title, author, isbn, dateOfPublication FROM books WHERE id IN ("+str(ids)+")"
    cursor.execute(statement)
    desc = cursor.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))
            for row in cursor.fetchall()]
    return data


def get_bookid(title):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id FROM books WHERE title = ?"
    cursor.execute(statement, [title])
    return cursor.fetchone()
