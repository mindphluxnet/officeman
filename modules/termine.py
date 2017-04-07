import sqlite3
from modules.db import DB

class Termine:

    @staticmethod
    def get(dbfile):

        db = DB()

        conn = db.connect(dbfile)
        c = conn.cursor()

        c.execute("SELECT oid, * FROM termine WHERE archiviert = 0 ORDER BY beginndatum, ablaufdatum ASC")
        termine = c.fetchall()

        db.disconnect(conn, False)

        return termine
