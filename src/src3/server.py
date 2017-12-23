from flask import Flask
from flask import render_template
app = Flask(__name__)

contact_list=[{"nom":"Einstein","prenom":"Albert","tel":"06.00.00.00.00","mail":"albert@e_mc2.com"},
              {"nom":"Shannon","prenom":"Claude","tel":"06.00.00.00.00","mail":"claude&fe_sup_2fmax.com"},
              {"nom":"Fourier","prenom":"Joseph","tel":"09.00.03.00.01","mail":"joseph&ma_serie.fr"}]
              
@app.route('/')
def index():
    return render_template("index.html",contact_list=contact_list)
