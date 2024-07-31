'''
exercicio 1 do Desafio 2 -  Faça um Programa que peça dois números e imprima o maior deles.
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
    while len(numeros) < 2:
        numero = input_int("\tNúmero: ")
        numeros.append(numero)
    return numeros

def exibir_maior_numero(numeros: list[int]) -> int:
    '''
    Obtem os numeros e exibe o maior
    '''
    numeros.sort()
    max_sum = sum(numeros[1:])
    return max_sum

def main() -> None:
    '''
    Fluxo principal do programa.
    '''
    limpar_console()
    numeros = obter_numeros()
    maior_numero = exibir_maior_numero(numeros)
    print(verde('\n\t########## Resultado #############'))
    print(verde(f"\n\t\tMaior número: {maior_numero}"))
    print(verde('\n\t##################################'))

if __name__ == '__main__':
    main()
   
