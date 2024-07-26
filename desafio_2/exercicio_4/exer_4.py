'''
exercicio 4 do Desafio 2 - Implemente um programa que classifique um aluno com base em sua
pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
reprovado.
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

def exibir_cabecalho() -> None:
    '''
    Exibe o cabeçalho.
    '''
    limpar_console()
    print("\tEntre com uma nota.")

def input_float(msg: str) -> float:
    '''
    Obtem número informado pelo usuário.
    Retorna o número.
    '''
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print(bright_vermelho('\tApenas números são aceitos. Por favor, tente novamente.\n'))

def obter_nota() -> float:
    '''
    Obtem uma nota de 0 a 10.
    Retorna a nota.
    '''
    while True:
        nota = input_float("\tNota: ")
        if nota < 0 or nota > 10:
            print(f"\n\t Nota {bright_vermelho(nota)} inválida! A nota deve ser um número de 0 a 10. Por favor tente novamente.\n") # pylint: disable=line-too-long
        else:
            return nota
def main() -> None:
    '''
    Fluxo Principal do Programa.
    '''
    exibir_cabecalho()
    nota = obter_nota()
    if nota >= 7:
        print(f"\tNota = {verde(nota)}, situação: {verde('Aprovado')}.\n")
    else:
        print(f"\tNota = {bright_vermelho(nota)}, situação: {bright_vermelho('Reprovado.')}\n")

if __name__ == '__main__':
    main()
