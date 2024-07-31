'''
Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros.
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


def input_float(msg: str) -> float:
    '''
    Obtem número inteiro informado pelo usuário.
    Retorna o número.
    '''
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print(bright_vermelho('\tApenas números são aceitos. Por favor, tente novamente.\n'))

def obter_quilometro() -> float:
    '''
    Obtem o quilômetro iformado pelo usuário.
    Retorna o quilômetro válido.
    '''
    while True:
        quilometro_informado =  input_float('\tQuilômetro (km): ')
        if quilometro_informado > 0:
            return quilometro_informado    
        print(bright_vermelho('\tValor do quilômetro inválido. Entre com um valor acima de zero.'))

def converter(quilometro: float) -> list[float]:
    '''
    Converte o quilômetro em metros, centímetros e milímetros.
    Retorna uma lista com os valores metros, centímetros e milímetros.
    '''
    metros = quilometro * 1000
    centimetros = quilometro * 100_000
    milimetros = quilometro *  1e+6
    conversoes = [metros, centimetros, milimetros]
    return conversoes

def main() -> None:
    '''
    Fluxo principal do programa.
    '''
    limpar_console()
    print(verde('\tConverter quilômetro em metros, centímetros e milímetros.\n'))
    quilometro =  obter_quilometro()
    resultado = converter(quilometro)
    print(verde('\n\t############ Resultado ###############'))
    print(verde(f"\n\t\tMetros: {resultado[0]}\n\t\tCentímetros: {resultado[1]} \n\t\tMilímetros: {resultado[2]}"))
    print(verde('\n\t######################################'))
if __name__ == '__main__':
    main()
