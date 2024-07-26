'''
exercicio 3 do Desafio 3 - Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.
'''

import os
import platform
from typing import Final
from typing import Any

COR_BRANCA: Final[str] = '\033[0;0m'
COR_BRIGHT_AMARELA: Final[str] = '\033[93m'
COR_BRIGHT_VERMELHA: Final[str] = '\033[91m'
COR_VERDE: Final[str] = '\033[32m'

# Habilita os caracteres ANSI escape no terminal Windows.
os.system("")

CARRINHO_DE_COMPRAS:Final[dict[str, int]] = {
    'camisa': 5,
    'bone': 2,
    'calca': 3,
    'caneca': 15,
}

def verde(conteudo: Any) -> Any:
    '''
    Colore o texto informado em verde.
    Retorna o texto colorido.
    '''
    return f"{COR_VERDE}{conteudo}{COR_BRANCA}"

def bright_amarelo(conteudo: Any) -> Any:
    '''
    Colore o texto informado em amarelo brilhante.
    Retorna o texto colorido.
    '''
    return f"{COR_BRIGHT_AMARELA}{conteudo}{COR_BRANCA}"

def bright_vermelho(conteudo: Any) -> Any:
    '''
    Colore o texto informado em vermelho brilhante.
    Retorna o texto colorido.
    '''
    return f"{COR_BRIGHT_VERMELHA}{conteudo}{COR_BRANCA}"

def limpar_console():
    '''
    Limpa o console de acordo com a plataforma.
    '''
    if platform.system() == 'Windows':
        os.system('cls')
    if platform.system() == 'Linux':
        os.system('clear')

def exibir_cabecalho() -> None:
    '''
    Exibe o cabeçalho.
    '''
    limpar_console()
    print('\t#####################################')
    print("\t\tTotal de produtos no carrinho.")
    print('\t#####################################\n')

def main() -> None:
    '''
    Fluxo Principal do Programa.
    '''
    exibir_cabecalho()
    valor_do_carrinho = 0
    for valor in CARRINHO_DE_COMPRAS.values():
        valor_do_carrinho += valor

    print("\n\tProdutos no carrinho:\n")
    for produto, valor in CARRINHO_DE_COMPRAS.items():
        print(f"\t{produto}\tR$ {valor}")
    print(f"\n\tTotal do carrinho R$ {verde(valor_do_carrinho)}\n")


if __name__ == '__main__':
    main()
