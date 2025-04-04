"""
Arquivo que conterá funções úteis ao sistema
Author: Tom Bittencourt
Version: 2025-04-03
"""
def cabecalho(titulo="Olá mundo!", colunas = 60): 
    #colunas = 60
    espacos =(colunas-len(titulo)) //2
    texto = " " * espacos + titulo + " " * espacos
    print(texto)

def fatorial(valor):
    ret = 1 #coloca 1 para não multiplicar por 0
    for i in range(valor,1,-1):
        ret*= i
    return ret #retorna o valor (sem return ele manda None)

def fatorial_rec(valor): #fatorial usando recursividade
    if valor == 1: return 1
    return valor * fatorial_rec(valor - 1)

if __name__ == "__main__": #só executa quando chamar funcoes.py (import)
    cabecalho("Olá Mundo!", 20)