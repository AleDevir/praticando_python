'''
exercicio 1 do Desafio 3 - Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime.
As perguntas são:
    ""Telefonou para a vítima?""
    ""Esteve no local do crime?""
    ""Mora perto da vítima?""
    ""Devia para a vítima?""
    ""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
""Assassino"".
Caso contrário,ele será classificado como""Inocente"".

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
    print("\t\tPerguntas sobre o crime:")
    print('\t#####################################\n')

def input_sim_nao(pergunta: str) -> str:
    '''
    Obtem uma resposta sim ou não.
    retorna a resposta.
    '''
    while True:
        resposta = input(pergunta).upper()
        if resposta in ('S', 'N'):
            return resposta.upper()
        print(bright_vermelho('\tVocê deve responder S ou N'))

def obter_respostas() -> list[str]:
    '''
    Obtem as respostas.
    '''
    respostas_sim: list[str] = []
    perguntas: list[str] = [
        "\n\tTelefonou para a vítima?",
        "\n\tEsteve no local do crime?",
        "\n\tMora perto da vítima?",
        "\n\tDevia para a vítima?",
        "\n\tJá trabalhou com a vítima?"
        ]
    for pergunta in perguntas:
        resposta = input_sim_nao(f'{pergunta} (S ou N): ')
        if resposta == 'S':
            respostas_sim.append(resposta)
    return respostas_sim


def classificar_participacao_no_crime(respostas: list[str]) -> str:
    '''
    Classifica como Suspeita, Cúmplice, Assassino ou Inocente de acordo
    com a quantidade de respostas positivas.
    '''
    if len(respostas) == 2:
        return 'Suspeita'
    elif 3 <= len(respostas) <= 4:
        return'Cúmplice'
    elif len(respostas) == 5:
        return 'Assassino'
    return 'Inocente'


def main() -> None:
    '''
    Fluxo principal do programa.
    '''
    exibir_cabecalho()
    respostas = obter_respostas()
    classificacao_pessoa_no_crime = classificar_participacao_no_crime(respostas)
    print(bright_amarelo(f'\n\tPessoa considerada {classificacao_pessoa_no_crime}'))


if __name__ == '__main__':
    main()
