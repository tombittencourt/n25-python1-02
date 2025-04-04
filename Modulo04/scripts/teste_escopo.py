"""
Código para demonstrar escopo de variáveis no python
Author: Tom Bittencourt
Version: 2025-04-03
"""
from click import clear
#definindo uma função
def calculo():
    a= 5
    b = a + c
    # c = 30 # Se descomentado dá erro porque a variável c passa a ser local
    return b
#programa principal
c = 10
clear()
print(calculo())