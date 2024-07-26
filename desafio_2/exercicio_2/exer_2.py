'''
exercicio 2 do Desafio 2 - Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
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

def exibir_menu(opcoes: dict[str, str]) -> None:
    '''
    Exibi o menu de opções.
    '''
    print('')
    print(verde(f'\t{LINHA_TRACEJADA}'))
    cabecalho = 'MENU DE OPÇÕES \n'
    print(verde(cabecalho.center(50)))


    for key, value in opcoes.items():
        opcao = '|' + key + '|' + "  "  + value
        print(f"\t\t{verde(opcao)} ")
    print(verde(f'\t{LINHA_TRACEJADA}'))

opcoes_de_turno:  dict[str, str ] = {
    'M': 'Matutino',
    'V': 'Vespertino',
    'N': 'Noturno'  
}

def input_opcoes(msg: str, opcoes: dict[str, str ]) -> str:
    '''
    Obtem a opção válida.
    Retorna a opção.
    '''
    while True:
        opcao = input(msg).upper()
        if opcao in opcoes:
            return opcao
        print(f"\n\t{bright_vermelho(opcao)} Opção inválida! As opções válidas são: {verde(', '.join(opcoes))}\n") 

def exibir_mensagem(opcao) -> None:
    '''
    Exibe uma mensagem de acordeo com a opção escolhida.
    '''
    if opcao == "M":
        print(verde("\n\tBom dia!"))
    elif opcao == "V":
        print(verde("\n\tBoa tarde!"))
    elif opcao == "N":
        print(verde("\n\tBom noite!"))

def obter_turno() -> str:
    '''
    Obtem a opção de turno.
    Retorna a opção.
    '''
    while True:
        opcao = input_opcoes('\tEm que turno você estuda? ', opcoes_de_turno)
        exibir_mensagem(opcao)
        break

def main() -> None:
    '''
    Fluxo principal do programa.
    '''
    limpar_console()
    exibir_menu(opcoes_de_turno)
    obter_turno()

if __name__ == '__main__':
    main()
