import sqlite3
from modules.db import DB

class Clients:

    @staticmethod
    def get(dbfile):

        db = DB()

        conn = db.connect(dbfile)
        c = conn.cursor()

        c.execute("SELECT oid, * FROM klienten ORDER BY nachname, vorname DESC")
        klienten = c.fetchall()

        db.disconnect(conn, False)

        return klienten

    @staticmethod
    def getsingle(dbfile, id):

        db = DB()

        conn = db.connect(dbfile)
        c = conn.cursor()

        c.execute("SELECT oid, * FROM klienten WHERE oid = ?", [ id ])
        klient = c.fetchone()

        db.disconnect(conn, False)

        return klient


    @staticmethod
    def put(dbfile, klient):

        db = DB()

        conn = db.connect(dbfile)
        c = conn.cursor()

        c.execute("INSERT INTO klienten (vorname, nachname, geburtsdatum, archiviert) VALUES (?, ? ,?, ?)", [ klient['vorname'], klient['nachname'], klient['geburtsdatum'], 0 ])
        db.disconnect(conn, True)

    @staticmethod
    def update(dbfile, klient):

        db = DB()

        conn = db.connect(dbfile)
        c = conn.cursor()

        c.execute("UPDATE klienten SET vorname = ?, nachname = ?, geburtsdatum = ? WHERE oid = ?", [ klient['vorname'], klient['nachname'], klient['geburtsdatum'], klient['id'] ])
        db.disconnect(conn, True)

    @staticmethod
    def archive(dbfile, id):

        db = DB()

        conn = db.connect(dbfile)
        c = conn.cursor()

        c.execute("SELECT archiviert FROM klienten WHERE oid = ?", [ id ])
        archived = c.fetchone()

        if(archived['archiviert'] == 0):
            c.execute("UPDATE klienten SET archiviert = 1 WHERE oid = ?", [ id ])
        else:
            c.execute("UPDATE klienten SET archiviert = 0 WHERE oid = ?", [ id ])

        c.execute("SELECT oid, archiviert FROM klienten WHERE oid = ?", [ id ])
        klient = c.fetchone()

        db.disconnect(conn, True)

        return klient
