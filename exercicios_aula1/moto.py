'''
    Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo.
    Adicione um novo atributo chamado tipo ao construtor, indicando se a moto é esportiva ou casual.
'''

from veiculos import Veiculo
class Moto(Veiculo):
    def __init__(self,marca, modelo, tipo) -> None:
        super().__init__(modelo, marca)
        self.tipo = tipo
    
    '''
        Implemente o Método Especial str na Classe Filha (Moto): Adicione um método especial str à classe Moto que estenda o método da classe pai (Veiculo) e inclua a informação sobre o tipo da moto.
    '''
    def __str__(self) -> str:
        tipo_m = 'Esportiva' if self.tipo else 'Casual'
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Esportiva? {tipo_m}'