'''
exercicio 10 do Desafio 2 -  Faça um programa que lê três números inteiros e os mostra em ordem
crescente.
'''

import os
import platform
from typing import Final
from typing import Any

COR_BRANCA: Final[str] = '\033[0;0m'
COR_VERDE: Final[str] = '\033[32m'
COR_BRIGHT_VERMELHA: Final[str] = '\033[91m'

# Habilita os caracteres ANSI escape no terminal Windows.
os.system("")

def verde(conteudo: Any) -> Any:
    '''
    Colore o texto informado em verde.
    Retorna o texto colorido.
    '''
    return f"{COR_VERDE}{conteudo}{COR_BRANCA}"

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

def input_int(msg: str) -> int:
    '''
    Obtem número inteiro informado pelo usuário.
    Retorna o número.
    '''
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print(bright_vermelho('\tApenas números são aceitos. Por favor, tente novamente.\n'))

def obter_numeros() -> int:
    '''
    Obtem dois números inseridos pelo usuário.
    Retorna os números.
    '''
    numeros: list[int] = []
    while len(numeros) < 3:
        numero = input_int("\tNúmero: ")
        numeros.append(numero)
    return numeros

def main() -> None:
    '''
    Fluxo principal do programa.
    '''
    limpar_console()
    numeros = obter_numeros()
    numeros.sort()
    print(verde('\n\t################## Resultado #####################'))
    print(verde(f"\n\t\tNúmeros digitados em ordem crescente: {numeros}"))
    print(verde('\n\t##################################################'))

if __name__ == '__main__':
    main()
