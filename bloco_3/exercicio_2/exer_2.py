'''
exercicio 2 do Desafio 3-  Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0.
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
ALUNOS:Final[list[str]] = ['João', 'Maria', 'Eduarda', 'Felipe', 'Ana Clara']


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
    print('\t#######################################')
    print("\tEntre com notas para saber a aprovação")
    print('\t#######################################\n')

def input_float(msg: str) -> float:
    '''
    Obtem número inteiro informado pelo usuário.
    Retorna o número.
    '''
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print(bright_vermelho('Apenas números são aceitos. Por favor, tente novamente.\n'))

def obter_nota(numero: float) -> float:
    '''
    Obtem uma nota de 0 a 10.
    Retorna a nota.
    '''
    while True:
        nota = input_float(f"\t{numero}° nota: ")
        if nota < 0 or nota > 10:
            print(f"\n\tNota {bright_vermelho(nota)} inválida! A nota deve ser um número de 0 a 10. Por favor tente novamente.\n") # pylint: disable=line-too-long
        else:
            return nota

def obter_notas(numero_de_notas: int = 4) -> list[float]:
    '''
    Obtem as quatro notas inseridas pelo usuário na ordem ['1°', '2°' , '3°', '4°'].
    Retorna uma listacom as notas.
    '''
    notas: list[float] = []
    for numero in range(1, numero_de_notas+1):
        nota = obter_nota(numero)
        notas.append(nota)
    return notas

def calcular_media(numeros: list[float], precisao: int = 1) -> float:
    '''
    Calcula a média das notas informadas pelo usuário.
    Retorna a média com precisão de uma casa decimal.
    '''
    somar = sum(numeros)
    media = somar / len(numeros)
    return round(media, precisao)

def main() -> None:
    '''
    Fluxo Principal do Programa.
    '''
    exibir_cabecalho()
    notas_do_aluno:list[float] = []
    numero_de_alunos_aprovados = 0
    for aluno in ALUNOS:
        print(bright_amarelo(f'\n\tAluno: {aluno}\n'))
        notas = obter_notas()
        notas_do_aluno.append(notas)
        media = calcular_media(notas, 2)
        if media >= 7:
            numero_de_alunos_aprovados += 1

    print(f"\n\tNúmero de alunos aprovados = {verde(numero_de_alunos_aprovados)}\n")


if __name__ == '__main__':
    main()
