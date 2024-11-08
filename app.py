from flask import Flask, render_template, redirect, url_for, request
from models import db, Cliente, Produto, Venda
from forms import ClienteForm, ProdutoForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loja.db'
app.config['SECRET_KEY'] = 'chave_secreta'

db.init_app(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/cadastrar_cliente', methods=['GET', 'POST'])
def cadastrar_cliente():
    form = ClienteForm()
    if form.validate_on_submit():
        cliente = Cliente(
            nome=form.nome.data,
            idade=form.idade.data,
            cpf=form.cpf.data,
            email=form.email.data,
            endereco=form.endereco.data
        )
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for('listar_clientes'))
    return render_template('cadastrar_cliente.html', form=form)

@app.route('/listar_clientes')
def listar_clientes():
    clientes = Cliente.query.all()
    return render_template('listar_clientes.html', clientes=clientes)

@app.route('/cadastrar_produto', methods=['GET', 'POST'])
def cadastrar_produto():
    form = ProdutoForm()
    if form.validate_on_submit():
        produto = Produto(
            nome=form.nome.data,
            preco=form.preco.data,
            descricao=form.descricao.data,
            quantidade_estoque=form.quantidade_estoque.data
        )
        db.session.add(produto)
        db.session.commit()
        return redirect(url_for('listar_produtos'))
    return render_template('cadastrar_produto.html', form=form)

@app.route('/listar_produtos')
def listar_produtos():
    produtos = Produto.query.all()
    return render_template('listar_produtos.html', produtos=produtos)

# Função para gerar gráfico de vendas
import matplotlib.pyplot as plt
from io import BytesIO
import base64

@app.route('/grafico_vendas')
def grafico_vendas():
    vendas = [10, 20, 30, 40, 50]  # Exemplo de dados de vendas
    dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex']

    plt.plot(dias, vendas)
    plt.xlabel('Dias')
    plt.ylabel('Vendas')
    plt.title('Vendas Diárias')

    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    grafico_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return render_template('grafico.html', grafico_url=grafico_url)

if __name__ == '__main__':
    app.run(debug=True)
