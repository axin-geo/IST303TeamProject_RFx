from flask import Flask , render_template , redirect , url_for , request, abort, flash
import sqlite3 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

#create a function that creates a database connection and return it
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/rfx-owners")
def rfx_owners():
    conn = get_db_connection()
    rfx_owner_tbl = conn.execute('SELECT * FROM rfx_owner_tbl').fetchall()
    conn.close()
    return render_template('rfxowner.html', rfx_owner_tbl=rfx_owner_tbl)

@app.route("/edit/<id>",  methods=["GET", "POST" ])
def edit(id):
    return "in dev"

