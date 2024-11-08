from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, FileField
from wtforms.validators import DataRequired, Email, NumberRange, Length
from flask_wtf.file import FileAllowed

class ClienteForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    idade = IntegerField('Idade', validators=[DataRequired(), NumberRange(min=18, max=999)])
    cpf = StringField('CPF', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    endereco = StringField('Endereço', validators=[DataRequired()])

class ProdutoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(min=3)])
    preco = FloatField('Preço', validators=[DataRequired(), NumberRange(min=0.01)])
    descricao = StringField('Descrição')
    quantidade_estoque = IntegerField('Quantidade em Estoque', validators=[DataRequired(), NumberRange(min=0)])
