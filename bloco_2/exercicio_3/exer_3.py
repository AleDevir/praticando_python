'''
exercicio 3 do Desafio 2  - Faça um programa que peça uma nota, entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o usuário
informe um valor válido.
'''

import os
import platform
from typing import Final
from typing import Any

LINHA_TRACEJADA: Final[str] = '-' * 31
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
            print(bright_vermelho('\tApenas números inteiros são aceitos. Por favor, tente novamente.\n'))

def obter_nota() -> float:
    '''
    Obtem uma nota de 0 a 10.
    Retorna a nota.
    '''
    while True:
        nota = input_int("\tEntre com uma nota de 0 a 10: ")
        if nota < 0 or nota > 10:
            print(f"\n\tNota {bright_vermelho(nota)} inválida! A nota deve ser um número de 0 a 10. Por favor tente novamente.\n") # pylint: disable=line-too-long
        else:
            return nota

def main() -> None:
    '''
    Fluxo principal do programa.
    '''
    limpar_console()
    obter_nota()

if __name__ == '__main__':
    main()
