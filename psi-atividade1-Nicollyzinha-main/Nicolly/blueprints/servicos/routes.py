# Este arquivo ainda não é usado pela aplicação.
from flask import render_template
import models
from blueprints.servicos import servicos_bp



@servicos_bp.route("/servicos")
def listar_servicos():
    return render_template("catalog.index.html", servicos=models.servicos)


@servicos_bp.route("/servico/<int:servico_id>")
def ver_servico(servico_id):
    servico = models.buscar_servico(servico_id)
    if servico is None:
        return "Serviço não encontrado", 404

    return f"""
    <h2>{servico['descricao']}</h2>
    <p>Categoria: {servico['categoria']}</p>
    <p>Prazo: {servico['prazo']}</p>
    <p>Valor: R$ {servico['valor']}</p>
    <a href='/'>Voltar para a oficina</a>
    """



