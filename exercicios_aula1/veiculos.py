'''
    Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, marca e modelo.
    A classe deve ter um atributo protegido _ligado inicializado como False por padrão.
'''
class Veiculo:
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ligado = False
    

    '''
        Construa o Método Especial str: Adicione um método especial str à classe Veiculo que retorna uma mensagem formatada com a marca, modelo e o estado de ligado/desligado do veículo.
    '''
    def __str__(self) -> str:
        status =    'Ligado' if self.ligado else 'Deligado'
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Ligado? {status}'
    