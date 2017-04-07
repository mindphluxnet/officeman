import sqlite3
from modules.db import DB

class Documents:

    @staticmethod
    def get(dbfile, klient_id):

        db = DB()

        conn = db.connect(dbfile)
        c = conn.cursor()

        c.execute("SELECT oid, * FROM dokumente WHERE klient_id = ?", [ id ])
        dox = c.fetchall()

        db.disconnect(conn, False)

        return dox

    @staticmethod
    def getsingle(dbfile, id):

        db = DB()

        conn = db.connect(dbfile)
        c = conn.cursor()

        c.execute("SELECT oid, * FROM dokumente WHERE oid = ?", [ id ])
        dox = c.fetchone()

        db.disconnect(conn, False)

        return dox

    @staticmethod
    def getbydate(dbfile, date):

        db = DB()

        conn = db.connect(dbfile)
        c = conn.cursor()

        c.execute("SELECT oid, * FROM dokumente WHERE add_datum = ?", [ date ])
        dox = c.fetchall()

        db.disconnect(conn, False)

        return dox

    @staticmethod
    def getbycategory(dbfile, kat):

        db = DB()

        conn = db.connect(dbfile)
        c = conn.cursor()

        c.execute("SELECT oid, * FROM dokumente WHERE kategorie = ?", [ kat ])
        dox = c.fetchall()

        db.disconnect(conn, False)

        return dox

    @staticmethod
    def getbycategory_byclient(dbfile, kat, client_id):

        db = DB()

        conn = db.connect(dbfile)
        c = conn.cursor()

        c.execute("SELECT oid, * FROM dokumente WHERE kategorie = ? AND klient_id = ?", [ kat, client_id ])
        dox = c.fetchall()

        db.disconnect(conn, False)

        return dox
