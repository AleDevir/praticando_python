'''
exercicio 5 do Desafio 2 - Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
    equilátero: todos os lados com o mesmo valor
    isósceles: dois lados com o mesmo valor
    escaleno: todos os lados com medidas distintas.
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
    print(bright_amarelo('\tEntre com os comprimentos e saiba qual é o tipo de triângulo.\n'))

def input_int(msg: str) -> int:
    '''
    Obtem número informado pelo usuário.
    Retorna o número.
    '''
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print(bright_vermelho('\tApenas números são aceitos. Por favor, tente novamente.\n'))

def obter_comprimento(lado: int) -> int:
    '''
    Obtem um comprimento.
    Retorna comprimento.
    '''
    while True:
        lado_informado = input_int(f"\t{lado}° comprimento: ")
        if lado_informado <= 0:
            print(bright_vermelho("\tValor inválido! Por favor tente novamente.\n"))
        else:
            return lado_informado

def obter_comprimentos(qtd_lados: int = 3) -> list[int]:
    '''
     Obtem as três comprimentos inseridos pelo usuário na ordem ['1°', '2°' , '3°'].
     Retorna uma lista com as três comprimentos.
    '''
    lados: list[float] = []
    for numero in range(1, qtd_lados+1):
        lado = obter_comprimento(numero)
        lados.append(lado)
    return lados

def classificar_triangulo(lado_1: int, lado_2: int, lado_3: int) -> str:
    '''
    Classifica o tipo de triângulo comparando as medidas:
    equilátero (os lados com o mesmo valor); 
    isósceles (dois lados com o mesmo valor);
    escaleno (todos os lados com medidas distintas).
    '''
    if lado_1 == lado_2 == lado_3:
        return 'Triângulo equilátero'
    if lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        return 'Triângulo isósceles'
    return 'Triângulo escaleno'

def main() -> None:
    '''
    Fluxo principal do programa.
    '''
    exibir_cabecalho()
    lados = obter_comprimentos()
    classificacao = classificar_triangulo(lados[0], lados[1], lados[2])
    print(f'\n\tClassificação: {bright_amarelo(classificacao)}')

if __name__ == '__main__':
    main()
