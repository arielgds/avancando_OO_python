'''
    Crie uma nova classe chamada Carro que herda da classe Veiculo.
    No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.
'''

from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor) -> None:
        super().__init__(marca, modelo)
        self.cor = cor

    def __str__(self):
        return f'Marca {self.marca} | Modelo {self.modelo} | cor {self.cor}'
    
    def ligar(self):
        return f'O carro {self.modelo} está ligado'