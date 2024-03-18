'''
    Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. No construtor da classe Carro, inclua um novo atributo chamado portas que indica a quantidade de portas do carro.
'''

from veiculos import Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, qnt_portas) -> None:
            super().__init__(marca, modelo)
            self.qnt_portas = qnt_portas

    '''
        Implemente o Método Especial str na Classe Filha: Adicione um método especial str à classe Carro que estenda o método da classe pai (Veiculo) e inclua a informação sobre a quantidade de portas do carro.    
    '''
    def __str__(self) -> str:
          status = "ligado" if self.ligado else "desligado"
          return f'Marca: {self.marca} | Modelo: {self.modelo} | Portas: {self.qnt_portas}'
          