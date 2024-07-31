'''
Peça ao usuário para informar o ano de nascimento. Em seguida,
calcule e imprima a idade atual.
'''

import os
import platform
from datetime import datetime
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

def input_int(msg: str) -> int:
    '''
    Obtem número inteiro informado pelo usuário.
    Retorna o número.
    '''
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print(bright_vermelho('\tApenas números inteiros são aceitos. Por favor, tente novamente.\n'))

def obter_ano() -> int:
    '''
    Obtem o ano de nascimento informado pelo usuário.
    Retorna o ano válido.
    '''
    ano_atual = datetime.now().year
    ano_limite = ano_atual - 130
    while True:
        ano_nacimento =  input_int('\n\tDigite o seu ano de nascimento: ')  
        if ano_nacimento > ano_limite:
            return ano_nacimento
        else:
            print(bright_vermelho('\tValor do ano inválido.'))

def calcular_idade_atual(ano_nacimento: int) -> int:
    '''
    Recebe o ano informado pelo usuário para calcular sua idade atual.
    Retorna a idade do usuário.
    '''
    year = datetime.today().year
    idade_atual = year - ano_nacimento
    return idade_atual

def main() -> None:
    '''
    Fluxo principal do programa.
    '''
    limpar_console()
    print('\tSaíba sua idade atual.')
    ano_nacimento_informado =  obter_ano() 
    ano_nacimento = calcular_idade_atual(ano_nacimento_informado)
    print(bright_amarelo('\n\t############## Resultado ################'))
    print(bright_amarelo(f"\n\t\tSua idade atual é: {ano_nacimento}") )
    print(bright_amarelo('\n\t#########################################'))


if __name__ == '__main__':
    main()

