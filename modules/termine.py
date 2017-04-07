import sqlite3
from modules.db import DB

class Termine:

    @staticmethod
    def get(dbfile):

        db = DB()

        conn = db.connect(dbfile)
        c = conn.cursor()

        c.execute("SELECT t.oid, t.*, k.vorname, k.nachname, k.archiviert AS klient_archiviert, ta.name, ta.icon FROM termine t LEFT JOIN klienten k ON(k.oid = t.klient_id) LEFT JOIN terminarten ta ON(ta.oid = t.terminart) WHERE k.archiviert = 0 ORDER BY t.beginndatum, t.ablaufdatum ASC")
        termine = c.fetchall()

        db.disconnect(conn, False)

        return termine

    @staticmethod
    def getsingle(dbfile, id):

        db = DB()

        conn = db.connect(dbfile)
        c = conn.cursor()

        c.execute("SELECT oid, * FROM termine WHERE oid = ?", [ id ])
        termin = c.fetchone()

        db.disconnect(conn, False)

        return termin

    @staticmethod
    def put(dbfile, termin):

        db = DB()

        conn = db.connect(dbfile)
        c = conn.cursor()

        c.execute("INSERT INTO termine (terminart, klient_id, beginndatum, ablaufdatum, kommentar, bearbeitungskommentar, archiviert) VALUES (?, ?, ?, ?, ?, ?, ?)", [ termin['terminart'], termin['klient_id'], termin['beginndatum'], termin['ablaufdatum'], termin['kommentar'], termin['bearbeitungskommentar'], 0 ])

        db.disconnect(conn, True)

    @staticmethod
    def update(dbfile, termin):

        db = DB()

        conn = db.connect(dbfile)
        c = conn.cursor()

        c.execute("UPDATE termine SET terminart = ?, klient_id = ?, beginndatum = ?, ablaufdatum = ?, kommentar = ?, bearbeitungskommentar = ? WHERE oid = ?", [ termin['terminart'], termin['klient_id'], termin['beginndatum'], termin['ablaufdatum'], termin['kommentar'], termin['bearbeitungskommentar'], termin['id'] ])

        db.disconnect(conn, True)

    @staticmethod
    def done(dbfile, id):

        db = DB()

        conn = db.connect(dbfile)
        c = conn.cursor()

        c.execute("UPDATE termine SET erledigt = 1 WHERE oid = ?", [ id ])

        db.disconnect(conn, True)

    @staticmethod
    def archive(dbfile, id):

        db = DB()

        conn = db.connect(dbfile)
        c = conn.cursor()

        c.execute("UPDATE termine SET archiviert = 1 WHERE oid = ?", [ id ])

        db.disconnect(conn, True)

    @staticmethod
    def terminarten(dbfile):

        db = DB()

        conn = db.connect(dbfile)
        c = conn.cursor()

        c.execute("SELECT oid, name, icon FROM terminarten ORDER BY name ASC")
        terminarten = c.fetchall()

        db.disconnect(conn, False)

        return terminarten

    @staticmethod
    def setup_terminarten(dbfile):

        terminarten = []

        terminarten.append({ 'name': 'Grundsicherung', 'icon': 'money' })
        terminarten.append({ 'name': 'Hartz IV', 'icon': 'money'})
        terminarten.append({ 'name': 'Wohngeld', 'icon': 'money'})
        terminarten.append({ 'name': 'BaFOEg', 'icon': 'money'})
        terminarten.append({ 'name': 'Kindergeld', 'icon': 'money'})
        terminarten.append({ 'name': 'Jahresbericht', 'icon': 'file-text-o'})
        terminarten.append({ 'name': 'Rechnungslegung', 'icon': 'file-excel-o'})
        terminarten.append({ 'name': 'GEZ-Befreiung', 'icon': 'television'})
        terminarten.append({ 'name': 'Schwerbehindertenausweis', 'icon': 'id-card-o'})
        terminarten.append({ 'name': 'Sonstiges', 'icon': 'bell-o'})
        terminarten.append({ 'name': 'Rechnungslegung', 'icon': 'file-excel-o'})
        terminarten.append({ 'name': 'Beiblatt', 'icon': 'id-card-o'})
        terminarten.append({ 'name': 'Rentenantrag', 'icon': 'money'})
        terminarten.append({ 'name': 'ABW LWL', 'icon': 'money'})
        terminarten.append({ 'name': 'Ambulante Eingliederungshilfe', 'icon': 'money'})
        terminarten.append({ 'name': 'Eingliederungshilfe Werkstatt', 'icon': 'money'})

        db = DB()

        conn = db.connect(dbfile)
        c = conn.cursor()

        for t in terminarten:
            c.execute("INSERT OR IGNORE INTO terminarten (name, icon) VALUES (?, ?)", [ t['name'], t['icon'] ])

        db.disconnect(conn, True)
