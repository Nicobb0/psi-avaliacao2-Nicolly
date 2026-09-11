from flask import render_template, request, redirect, url_for, session
from blueprints.catalog import catalog_bp
import models

@catalog_bp.route("/")
def index():
    q = request.args.get("q", "")
    if q:
        lista = [s for s in models.servicos if q.lower() in s["descricao"].lower()]
    else:
        lista = models.servicos
    return render_template('index.html', servicos=lista, q=q,
                           categorias=models.todas_categorias())

@catalog_bp.route("/categoria/<nome>")
def ver_categoria(nome):
    lista = []
    for s in models.servicos:
        if s["categoria"].lower() == nome.lower():
            lista.append(s)
    return render_template('index.html', servicos=lista, q="",
                           categorias=models.todas_categorias())