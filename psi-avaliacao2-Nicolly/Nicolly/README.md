1- 
rotasestavam fora do controller
3-
para fzr com que rode as rotas dos blueprints em arquivos diferentes
@servicos_bp.route("/servicos")
def listar_servicos():
    return render_template("catalog.index.html", servicos=models.servicos)

