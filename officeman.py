#!/usr/bin/env python

from flask import Flask, render_template, send_from_directory, request, redirect, url_for, send_file, make_response, flash
import dateutil.parser
import time
import json
import webbrowser
import pdfkit
import os.path
import timestring
from datetime import datetime

from modules.db import DB
from modules.clients import Clients
from modules.termine import Termine
from modules.documents import Documents

debug = True
bind_host = "0.0.0.0"
bind_port = 8080
version = '2.0'
dbfile = os.path.dirname(os.path.realpath(__file__)) + os.sep + "officeman.db"

app = Flask(__name__, static_url_path = '')
app.secret_key = 'fgsdsdsdsdsrewfdd'

db = DB()
tm = Termine()
doc = Documents()

db.setup(dbfile)
tm.setup_terminarten(dbfile)
doc.setup_categories(dbfile)

@app.route('/assets/<path:path>')
def serve_asset(path):
        return send_from_directory('assets', path)

@app.route('/')
def show_index():

    return redirect(url_for('show_calendar'))

@app.route('/calendar')
def show_calendar():

    page_title = "Fristenverwaltung"
    page_id = "calendar"

    tm = Termine()
    kl = Clients()

    termine = tm.get(dbfile)
    klienten = kl.get(dbfile)
    terminarten = tm.terminarten(dbfile)

    today = datetime.now()

    for termin in termine:
        datum = timestring.Date(termin['beginndatum']).date
        termin['beginndatum'] = datetime.strftime(datum, '%d.%m.%Y')
        delta = datum - today
        if(delta.days < 0):
            termin['farbe'] = "danger"
        elif(delta.days < 30 and delta.days > 15):
            termin['farbe'] = "warning"

        datum = timestring.Date(termin['ablaufdatum']).date
        termin['ablaufdatum'] = datetime.strftime(datum, '%d.%m.%Y')
        delta = datum - today
        if(delta.days < 0):
            termin['farbe2'] = "danger"
        elif(delta.days < 30 and delta.days > 15):
            termin['farbe2'] = "warning"

    return render_template('calendar.html', termine = termine, klienten = klienten, terminarten = terminarten, page_title = page_title, page_id = page_id, version = version)

@app.route('/calendar/save', methods = ['POST'])
def calendar_save():

    tm = Termine()

    tm.put(dbfile, request.form)

    flash('Frist erfolgreich gespeichert', 'success')

    return redirect(url_for('show_calendar'))

@app.route('/calendar/update', methods = ['POST'])
def calendar_update():

    tm = Termine()

    tm.update(dbfile, request.form)

    flash('Frist erfolgreich aktualisiert', 'success')

    return redirect(url_for('show_calendar'))

@app.route('/calendar/getsingle', methods = ['POST'])
def calendar_getsingle():

    tm = Termine()

    termin = tm.getsingle(dbfile, request.form['id'])

    return json.dumps(termin)

@app.route('/calendar/done', methods = ['POST'])
def calendar_done():

    tm = Termine()

    tm.done(dbfile, request.form['id'])

    return 'ok'

@app.route('/calendar/archive', methods = ['POST'])
def calendar_archive():

    tm = Termine()

    tm.archive(dbfile, request.form['id'])

    return 'ok'


@app.route('/clients')
def show_clients():

    page_title = "Klientenverwaltung"
    page_id = "clients"

    clients = Clients()

    klienten = clients.get(dbfile)

    for klient in klienten:
        datum = timestring.Date(klient['geburtsdatum']).date
        klient['geburtsdatum'] = datetime.strftime(datum, '%d.%m.%Y')

    return render_template('clients.html', klienten = klienten, page_title = page_title, page_id = page_id, version = version)


@app.route('/clients/save', methods = ['POST'])
def save_client():

    clients = Clients()

    clients.put(dbfile, request.form)

    flash('Klient erfolgreich gespeichert', 'success')

    return redirect(url_for('show_clients'))

@app.route('/clients/update', methods = ['POST'])
def clients_update():

    clients = Clients()

    clients.update(dbfile, request.form)

    flash('Klient erfolgreich aktualisiert', 'success')

    return redirect(url_for('show_clients'))

@app.route('/clients/getsingle', methods = ['POST'])
def clients_getsingle():

    clients = Clients()

    klient = clients.getsingle(dbfile, request.form['id'])

    return json.dumps(klient)

@app.route('/clients/archive', methods = ['POST'])
def clients_archive():

    clients = Clients()

    result = clients.archive(dbfile, request.form['id'])

    return json.dumps(result)

@app.route('/documents')
def show_documents():

    page_title = "Dokumentenverwaltung"
    page_id = "documents"

    documents = Documents()
    clients = Clients()

    today = datetime.now().strftime("%Y-%m-%d")

    dox = documents.getbydate(dbfile, today)
    klienten = clients.get(dbfile)
    kategorien = documents.categories(dbfile)

    return render_template('documents.html', dox = dox, kategorien = kategorien, klienten = klienten, page_id = page_id, page_title = page_title, version = version)

if __name__ == '__main__':
	app.run(debug = debug, host = bind_host, port = bind_port)
