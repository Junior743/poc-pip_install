import os

class Principal():

    def __init__(self, valor):
        print(Principal.calculaValor(valor))
        
    def calculaValor(valor):
        valor = valor + 1000
        return valor

