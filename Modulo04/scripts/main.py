"""
Programa principal
Author: Tom Bittencourt
Version: 2025-04-03
"""
import funcoes
from click import clear #importando somente a função clear
clear() #limpa o console
funcoes.cabecalho("Bem vindo!")
funcoes.cabecalho("Boa noite", 30)
funcoes.cabecalho()
funcoes.cabecalho(colunas=15)
print ("fatorial de 5 =", funcoes.fatorial(5))
print("fatorial de 5 =", funcoes.fatorial_rec(5))