from app import app, db, Produto  # Importando o Flask e o banco de dados de app.py

with app.app_context():  # Iniciando o contexto da aplicação Flask
    produtos = Produto.query.all()  # Fazendo a consulta no banco
    print(produtos)  # Imprimindo os produtos no terminal
