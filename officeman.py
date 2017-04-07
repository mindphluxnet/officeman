#!/usr/bin/env python

from flask import Flask, render_template, send_from_directory, request, redirect, url_for, send_file, make_response
import dateutil.parser
import time
import json
import webbrowser
import pdfkit
import os.path
import timestring

from modules.db import DB
from modules.clients import Clients

debug = True
bind_host = "0.0.0.0"
bind_port = 8080
version = '2.0'
dbfile = os.path.dirname(os.path.realpath(__file__)) + os.sep + "officeman.db"

app = Flask(__name__, static_url_path = '')

db = DB()

db.setup(dbfile)

@app.route('/assets/<path:path>')
def serve_asset(path):
        return send_from_directory('assets', path)

@app.route('/')
def show_index():

    return redirect(url_for('show_calendar'))

@app.route('/calendar')
def show_calendar():

    page_title = "Terminverwaltung"
    page_id = "calendar"

    termine = []

    return render_template('calendar.html', termine = termine, page_title = page_title, page_id = page_id, version = version)

@app.route('/clients')
def show_clients():

    page_title = "Klientenverwaltung"
    page_id = "clients"

    clients = Clients()

    klienten = clients.get(dbfile)

    return render_template('clients.html', klienten = klienten, page_title = page_title, page_id = page_id, version = version)


if __name__ == '__main__':
	app.run(debug = debug, host = bind_host, port = bind_port)
