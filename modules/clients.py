import sqlite3
from modules.db import DB

class Clients:

    @staticmethod
    def get(dbfile, order = 'nachname'):

        db = DB()

        conn = db.connect(dbfile, True)
        c = conn.cursor()

        c.execute("SELECT oid, * FROM klienten ORDER BY ? ASC", [ order ])
        klienten = c.fetchall()

        db.disconnect(conn, False)

        return klienten

    @staticmethod
    def put(dbfile, klient):

        db = DB()

        conn = db.connect(dbfile)
        c = conn.cursor()

        c.execute("INSERT INTO klienten (vorname, nachname, geburtsdatum) VALUES (?, ? ,?)", [ klient['vorname'], klient['nachname'], klient['geburtsdatum'] ])

        db.disconnect(conn, True)
