"""

WishListDao class - CRUD operations for the WishList resource thru REST

"""


from database.db import get_db


def insert_wishlist(name, description, userid):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO wishlist(wishlistName, description, userId) VALUES (?, ?, ?)"
    cursor.execute(statement, [name, description, userid])
    db.commit()
    return True


def update_wishlist(wid, name, description, userid):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE wishlist SET wishlistName=?, description=? WHERE wishlistId= ? and userId=? "
    cursor.execute(statement, [name, description, wid, userid])
    db.commit()
    return True

def update_wishlist_bookids(wid, userid, bookids):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE wishlist SET bookids=? WHERE wishlistId= ? and userId=? "
    cursor.execute(statement, [bookids, wid, userid])
    db.commit()
    return True

def delete_wishlist(wid, userid):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM wishlist WHERE wishlistId = ? and userId=?"
    cursor.execute(statement, [wid, userid])
    db.commit()
    return True


def get_by_wishlistid(uid, wid):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT wishlistId, wishlistName, description, bookIds, userId FROM wishlist WHERE wishlistId = ? and " \
                "userId=? "
    cursor.execute(statement, [wid, uid])
    desc = cursor.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))
            for row in cursor.fetchall()]
    return data


def get_all_wishlist(uid):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT wishlistId, wishlistName, description, bookIds, userId FROM wishlist WHERE userId= ? "
    cursor.execute(query, [uid])
    desc = cursor.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))
            for row in cursor.fetchall()]
    return data


def get_wishlist_id(uid, name):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT wishlistId FROM wishlist WHERE userId= ? and " \
                "wishlistName=? "
    cursor.execute(statement, [uid, name])
    return cursor.fetchone()


def get_by_wishlist_books(uid, wid):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT bookIds FROM wishlist WHERE wishlistId = ? and " \
                "userId=? "
    cursor.execute(statement, [wid, uid])
    return cursor.fetchone()

