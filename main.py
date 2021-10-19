""" Desafio 01 e 03 - Programa para executar algumas perguntas para o usuário informar."""
from Pessoa import *

def info():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo: ")
    cidade = input("Digite sua cidade: ")
    estado = input("Digite seu Estado: ")
    return nome, idade, sexo, cidade, estado


print(info())

pessoa = Pessoa(input("Digite seu nome: "), int(input("Digite sua idade: " )), input("Digite seu sexo: "), 
input("Digite sua cidade: "), input("Digite seu Estado: ")) 

print(pessoa.Nome)