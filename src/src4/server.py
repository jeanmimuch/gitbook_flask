from flask import Flask
from flask import render_template, request, redirect, url_for
app = Flask(__name__)

contact_list=[{"nom":"Einstein","prenom":"Albert","tel":"06.00.00.00.00","mail":"albert@emc2.com"},
              {"nom":"Shannon","prenom":"Claude","tel":"06.00.00.00.00","mail":"claude@fesup2fmax.com"},
              {"nom":"Fourier","prenom":"Joseph","tel":"09.00.03.00.01","mail":"joseph@maserie.fr"}]
              
@app.route('/')
def index():
    return render_template("index.html",contact_list=contact_list)


@app.route('/create', methods=['GET', 'POST'])
def create():
    return render_template("create.html")

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def udpate(id):
    contact=contact_list[id-1]
    
    if request.method == "POST":
        contact={}
        contact["nom"] = request.values.get("nom")
        contact["prenom"] = request.values.get("prenom")
        contact["mail"]=request.values.get("mail")
        contact["tel"]=request.values.get("tel")
        contact_list[id-1]=contact
        return redirect(url_for("index"))
    
    if request.method == "GET":
        contact=contact_list[id-1]
        return render_template("update.html",contact=contact)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    contact=contact_list[id-1]
    return render_template("delete.html",contact=contact)
