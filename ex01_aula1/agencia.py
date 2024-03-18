from aula_01 import Banco
class Agencia:
    def __init__(self, nome, endereco, numero) -> None:
        super().__init__(nome, endereco)
        self._numero = numero