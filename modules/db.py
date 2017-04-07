import sqlite3

class DB:

    #: from http://stackoverflow.com/questions/811548/sqlite-and-python-return-a-dictionary-using-fetchone
    @staticmethod
    def dict_factory(cursor, row):
        d = {}
        for idx,col in enumerate(cursor.description):
            d[col[0]] = row[idx]

        return d

    @staticmethod
    def setup(dbfile):

        conn = sqlite3.connect(dbfile)
        c = conn.cursor()

        try:
            c.execute("CREATE TABLE termine (terminart INT, klient_id INT, beginndatum TEXT, ablaufdatum TEXT, kommentar TEXT, bearbeitungskommentar TEXT, archiviert INT(1))")
        except Exception:
            pass

        try:
            c.execute("CREATE TABLE klienten (vorname TEXT, nachname TEXT, geburtsdatum TEXT, archiviert INT(1))")
        except Exception:
            pass


        conn.commit()
        conn.close()

    @staticmethod
    def connect(dbfile):

        conn = sqlite3.connect(dbfile)
        conn.row_factory = DB.dict_factory

        return conn

    @staticmethod
    def disconnect(connection, with_commit = False):

        if(with_commit):
            connection.commit()

        connection.close()
