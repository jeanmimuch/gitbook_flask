#!/usr/bin/python
from flask import Flask
app = Flask(__name__)

contact_list=[{"nom":"Einstein","prenom":"Albert","tel":"06.00.00.00.00","mail":"albert@e_mc2.com"},
              {"nom":"Shannon","prenom":"Claude","tel":"06.00.00.00.00","mail":"claude&fe_sup_2fmax.com"},
              {"nom":"Fourier","prenom":"Joseph","tel":"09.00.03.00.01","mail":"joseph&ma_serie.fr"}]
              
@app.route('/')
def index():
    #construction de la chaine html
    html="<table>\n"
    html=html+"<tr>\n"
    html=html+"<th>Nom</th><th>Prenom</th><th>Telephone</th><th>Email</th>"
    html=html+"</tr>\n"

    for indice in range(len(contact_list)):
        mon_contact=contact_list[indice]

        html=html+"<tr>\n"
        html=html+"<td>"+mon_contact["nom"]+"</td>\n"
        html=html+"<td>"+mon_contact["prenom"]+"</td>\n"
        html=html+"<td>"+mon_contact["tel"]+"</td>\n"
        html=html+"<td>"+mon_contact["mail"]+"</td>\n"
        html=html+"</tr>\n"

    html=html+"</table>\n"
    return html
