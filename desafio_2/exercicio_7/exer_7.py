'''
exercicio 7 do Desafio 2 - Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.
'''

import os
import platform
from typing import Final
from typing import Any

LINHA_TRACEJADA: Final[str] = '-' * 31
COR_BRANCA: Final[str] = '\033[0;0m'
COR_BRIGHT_AMARELA: Final[str] = '\033[93m'
COR_BRIGHT_VERMELHA: Final[str] = '\033[91m'

# Habilita os caracteres ANSI escape no terminal Windows.
os.system("")


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
    print(bright_amarelo('''
            \tEntre com uma idade para saber a classicação:
             \tcriança, adolescente, adulto ou idoso.\n
    '''))

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

def obter_idade() -> int:
    '''
    Obtem a idade.
    Retorna a idade.
    '''
    while True:
        idade = input_int("\tEntre com idade: ")
        if  0 < idade < 120:
            return idade
        else:
            print(f"\n\tIdade {bright_vermelho(idade)} inválida! A idade deve ser um número de 0 a 120.\n") # pylint: disable=line-too-long


def main() -> None:
    '''
    Fluxo principal do programa.
    '''
    exibir_cabecalho()
    idade = obter_idade()

    if idade <= 12:
        print(f"""
            \tIdade de {bright_amarelo(idade)}
            classificada como {bright_amarelo('criança.')}
        """)
    elif 12 < idade < 18:
        print(f"""
            \tIdade de {bright_amarelo(idade)}
            classificada como {bright_amarelo('adolescente.')}
        """)
    elif 18 <= idade < 60:
        print(f"""
            \tIdade de {bright_amarelo(idade)}
            classificada como {bright_amarelo('adulto.')}
        """)
    elif idade >= 60:
        print(f"""
            \tIdade de {bright_amarelo(idade)}
            classificada como {bright_amarelo('idoso.')}
        """)



if __name__ == '__main__':
    main()
