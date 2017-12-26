import sqlite3
from flask import Flask
from flask import render_template, request, redirect, url_for, g
app = Flask(__name__)

DATABASE = "data.db"

# Gestion de la base de données (copier-coller de la doc de FLASK)
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def change_db(query,args=()):
    cur = get_db().execute(query, args)
    get_db().commit()
    cur.close()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Routage des URL et traitement

@app.route('/')
def index():
    contact_list=query_db("SELECT * FROM contact")
    return render_template("index.html",contact_list=contact_list)

@app.route('/create', methods=['GET', 'POST'])
def create():
    
    if request.method == "GET":
        return render_template("create.html",contact=None)
    
    if request.method == "POST":
        contact=request.form.to_dict()
        values=[contact["nom"],contact["prenom"],contact["mail"],contact["tel"]]
        change_db("INSERT INTO contact (nom,prenom,mail,tel) VALUES (?,?,?,?)",values)
        return redirect(url_for("index"))

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def udpate(id):

    if request.method == "GET":
        contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
        return render_template("update.html",contact=contact)
    
    if request.method == "POST":
        contact=request.form.to_dict()
        values=[contact["nom"],contact["prenom"],contact["mail"],contact["tel"],id]
        change_db("UPDATE contact SET nom=?, prenom=?, mail=?, tel=? WHERE ID=?",values)
        return redirect(url_for("index"))

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    
    if request.method == "GET":
        contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
        return render_template("delete.html",contact=contact)

    if request.method == "POST":
        change_db("DELETE FROM contact WHERE id = ?",[id])
        return redirect(url_for("index"))
