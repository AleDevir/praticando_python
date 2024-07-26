'''
exercicio 4 do Desafio 3 - Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome.
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

CONTATOS:Final[list[dict[str, int]] ]= [
    {
    'nome': 'Ale',
    'telefone': 999999999
    },
    {
    'nome': 'Amanda',
    'telefone': 888888888
    },
    {
    'nome': 'Leticia',
    'telefone': 212123698
    },

]


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
    print("\t\tPesquisar contato.")
    print('\t#####################################\n')

def obter_contato() -> str:
    '''
    Obtem um contato.
    Retorna o contato.
    '''
    contato_encontrado = {}
    nome_do_contato = input('\tEntre como o nome do contato: ').lower()
    for contato in CONTATOS:
        if contato['nome'].lower() == nome_do_contato.lower():
            contato_encontrado = contato.copy()

    if contato_encontrado:
        print(bright_amarelo(f'\n\tTelefone de {contato_encontrado['nome']} {contato['telefone']}'))
    else:
        print(bright_vermelho(f'\t{nome_do_contato} não exixte no cadastro.'))

def main() -> None:
    '''
    Fluxo Principal do Programa.
    '''
    exibir_cabecalho()
    obter_contato()

if __name__ == '__main__':
    main()
