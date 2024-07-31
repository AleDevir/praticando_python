'''
exercicio 9 do Desafio 2 - O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário informar o valor zero. 
Certifique-se de incluir validações para garantir que apenas números positivos sejam considerados 
na contagem e cálculos.
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
            \n\tEntre com números para ver se eles são pares ou impares.
             \n\tPara sair do programa entre com 0.\n
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

def obter_numeros() -> list[int]:
    '''
     Obtem os números inseridas pelo usuário.
     Retorna uma lista de números.
    '''
    numeros: list[int] = []
    while True:
        numero = input_int("\tNúmero: ")
        if numero == 0:
            break
        numeros.append(numero)
    return numeros


def calcular_quantidade_de_numeros_pares_e_impares() -> list:
    '''
    Calcula a quantidade de números pares e imapres.
    Retorna a quantidade.
    '''
    quantidade_de_numeros_pares = 0
    quantidade_de_numeros_impares = 0
    numeros = obter_numeros()

    for numero in numeros:
        if numero  % 2 == 0:
            quantidade_de_numeros_pares += 1
        else:
            quantidade_de_numeros_impares +=1
    print(bright_amarelo(f'''
        \n\tQuantidade de números pares digitados: {quantidade_de_numeros_pares}
        \n\tQuantidade de números impares digitados: {quantidade_de_numeros_impares}
    '''))

def main() -> None:
    '''
    Fluxo Principal do Programa.
    '''
    exibir_cabecalho()
    calcular_quantidade_de_numeros_pares_e_impares()



if __name__ == '__main__':
    main()
