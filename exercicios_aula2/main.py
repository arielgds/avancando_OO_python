'''
    Em um arquivo chamado main.py, importe a classe Carro.
    No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.
'''

from carro import Carro

carro_gol = Carro('Volks', 'Gol', 'Azul')
carro_s10 = Carro('Chevy', 'S10', 'Cinza')
carro_uno = Carro('Fiat', 'Uno', 'Vermelho')

print(carro_gol)
print(carro_s10)
print(carro_uno)