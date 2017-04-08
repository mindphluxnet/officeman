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

    @staticmethod
    def categories(dbfile):

        db = DB()

        conn = db.connect(dbfile)
        c = conn.cursor()

        c.execute("SELECT oid, name  FROM kategorien ORDER BY name ASC")
        kategorien = c.fetchall()

        db.disconnect(conn, False)

        return kategorien

    @staticmethod
    def setup_categories(dbfile):

        cat = []
        
        cat.append({ 'name': 'Bescheid Altersrente' })
        cat.append({ 'name': 'Bescheid Hinterbliebenenrente' })
        cat.append({ 'name': 'Bescheid EU-Rente' })
        cat.append({ 'name': 'Bescheid Waisenrente' })
        cat.append({ 'name': 'Bescheid Halbwaisenrente' })
        cat.append({ 'name': 'Bescheid Grundsicherung' })
        cat.append({ 'name': 'Bescheid SGBII' })
        cat.append({ 'name': 'Bescheid BaFOEg' })
        cat.append({ 'name': 'Bescheid Wohngeld' })
        cat.append({ 'name': 'Bescheid Pflegewohngeld' })
        cat.append({ 'name': 'Bescheid Hilfe zur Pflege' })
        cat.append({ 'name': 'Anforderung Jahresbericht' })
        cat.append({ 'name': 'Anforderung Verlaufsbericht' })
        cat.append({ 'name': 'Anforderung Rechnungslegung' })
        cat.append({ 'name': 'EC-Karte' })
        cat.append({ 'name': 'Gesundheitskarte' })
        cat.append({ 'name': 'Befreiungsausweis' })
        cat.append({ 'name': 'Rechnung' })
        cat.append({ 'name': 'Mahnung' })
        cat.append({ 'name': 'Forderungsaufstellung' })
        cat.append({ 'name': 'Sachstandsanfrage' })
        cat.append({ 'name': 'Mahnbescheid' })
        cat.append({ 'name': 'Vollstreckungsbescheid' })
        cat.append({ 'name': 'Pfaendungs- und Ueberweisungsbeschluss' })
        cat.append({ 'name': 'Betreuungsbeschluss' })
        cat.append({ 'name': 'Bestellungsurkunde' })
        cat.append({ 'name': 'Gutachterbestellung' })
        cat.append({ 'name': 'Begutachtungstermin' })
        cat.append({ 'name': 'Kostenuebernahme' })
        cat.append({ 'name': 'Bescheid Heimkostenuebernahme' })
        cat.append({ 'name': 'Beschluss Betreuungsende' })
        cat.append({ 'name': 'Beschluss Betreuungsabgabe' })
        cat.append({ 'name': 'Beschluss Abgabe an Amtsgericht' })
        cat.append({ 'name': 'Beschluss Entnahme von Sparkonto' })
        cat.append({ 'name': 'Beschluss Betreuungsbeginn' })
        cat.append({ 'name': 'Kostenerstattung' })
        cat.append({ 'name': 'Befreiung GEZ' })
        cat.append({ 'name': 'Brief von Klient' })
        cat.append({ 'name': 'Brief von Angehoerigen' })
        cat.append({ 'name': 'Belege zur Erstattung' })
        cat.append({ 'name': 'Bescheid Grundbesitzabgaben' })
        cat.append({ 'name': 'Jahresabrechnung' })
        cat.append({ 'name': 'Kontoauszug' })
        cat.append({ 'name': 'Unterlagen Kontoeinrichtung' })
        cat.append({ 'name': 'Unterlagen Onlinebanking' })
        cat.append({ 'name': 'Arztbrief' })
        cat.append({ 'name': 'Entlassungsbericht' })

        db = DB()

        conn = db.connect(dbfile)
        c = conn.cursor()

        for ca in cat:
            c.execute("INSERT OR IGNORE INTO kategorien (name) VALUES (?)", [ ca['name'] ])

        db.disconnect(conn, True)
