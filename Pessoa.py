""" Desafio 02: Criar uma classe Pessoa e um método construtor com os atributos"""
class Pessoa: 
    def __init__(self, nome, idade, sexo, cidade, estado):
        self.Nome = nome
        self.Idade = idade
        self.Sexo = sexo
        self.Cidade = cidade
        self.Estado = estado


pessoa = Pessoa('Leonardo', '25', 'M', 'Fortaleza', 'Ceará')

