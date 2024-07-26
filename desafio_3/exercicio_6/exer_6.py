'''
exercicio 6 do Desafio 3 - Faça um programa que permita ao usuário digitar o seu nome e
em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.
Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou
minúsculas.
'''
import os
import platform
from typing import Final
from typing import Any

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
    print('\t#####################################')
    print("\t\tSeu nome de trás para frente ")
    print('\t#####################################\n')

def obter_nome() -> str:
    '''
    Obtem nome.
    Retorna nome.
    '''
    while True:
        nome = input("\n\tNome: ").upper()
        if nome:
            return nome
        print(bright_vermelho('\n\tO nome deve ser preenchido! Por favor tente novamente.\n'))

def main() -> None:
    '''
    Fluxo Principal do Programa.
    '''
    exibir_cabecalho()
    nome = obter_nome()
    nome_reverso = nome[::-1]
    print(bright_amarelo(f"\tSeu nome de trás para frente é : {nome_reverso}"))

if __name__ == '__main__':
    main()