from modelos.restaurante import Restaurante
from modelos.bebida import Bebida
from modelos.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_coca_peq = Bebida('Coca-cola', 2.5, 'Pequeno')
prato_sushi = Prato('Sushi', 32.99, 'Sushi 15 peças')
prato_sushi.aplicar_desconto()
bebida_coca_peq.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_coca_peq)
restaurante_praca.adicionar_no_cardapio(prato_sushi)


def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()