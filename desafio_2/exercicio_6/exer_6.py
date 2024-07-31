'''
exercicio 6 do Desafio 2 - Crie um programa que solicite ao usuário um login e uma senha. O
programa deve permitir o acesso apenas se o usuário for "admin" e a senha
for "admin123", caso contrário imprima uma mensagem de erro.
'''

import os
import platform
from getpass import getpass
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
    print(bright_amarelo('\tFazer login.\n'))

def obter_username() -> str:
    '''
    Obtem o username.
    Retorna o username.
    '''
    while True:
        username = input("\tUsername: ")
        if username == "":
            print(bright_vermelho('\tO campo username deve ser preenchido\n'))
        else:
            return username

def obter_senha() -> str:
    '''
    Obtem senha.
    Retorna a senha.
    '''
    while True:
        senha = getpass("\tEntre sua senha: ")
        if senha == "":
            print(bright_vermelho('\tO campo senha deve ser preenchido\n'))
        else:
            return senha

def fazer_login(username: str, senha: str) -> bool:
    '''
    fazer login - credênciais válidas
    '''
    if username == 'admin' and senha == 'admin123':
        return True
    return False

def main() -> None:
    '''
    Fluxo principal do programa.
    '''
    exibir_cabecalho()
    username = obter_username()
    senha = obter_senha()
    logado = fazer_login(username, senha)
    if not logado:
        print(bright_vermelho('\n\tCredênciais inválidas.\n'))
    else:
        print(bright_amarelo(f'\n\tOlá {username}.'))


if __name__ == '__main__':
    main()
