"""

USerDao class - CRUD operations for the User resource thru REST

"""


from database.db import get_db


def insert_user(firstname, lastname, email, password, status):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO user(firstName, lastName, email, password, status) VALUES (?, ?, ?, ?,?)"
    cursor.execute(statement, [firstname, lastname, email, password, status])
    db.commit()
    return True


def update_user(uid, firstname, lastname, email, password):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE user SET firstName=?, lastName=?, email=?, password=? WHERE uid= ?"
    cursor.execute(statement, [firstname, lastname, email, password, uid])
    db.commit()
    return True


def delete_user(uid):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM user WHERE uid = ?"
    cursor.execute(statement, [uid])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT uid, firstName, lastName, email, password, status FROM user WHERE uid = ?"
    cursor.execute(statement, [id])
    desc = cursor.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))
            for row in cursor.fetchall()]
    return data


def get_users():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT uid, firstName, lastName, email, password, status FROM user"
    cursor.execute(query)
    desc = cursor.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))
            for row in cursor.fetchall()]
    return data


def get_by_email(email):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT uid FROM user WHERE email = ?"
    cursor.execute(statement, [email])
    return cursor.fetchone()
