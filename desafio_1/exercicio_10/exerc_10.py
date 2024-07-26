'''
exercício 10 do Desafio_1 - Faça um Programa que utilize 4 variáveis como preferir e no final print
uma mensagem amigável utilizando as variáveis criadas.
Exemplos de variáveis: nome, idade, lugar, profissão ....
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo
também e estou migrando de área..
'''

import os
import platform
from typing import Final
from typing import Any

COR_BRANCA: Final[str] = '\033[0;0m'
COR_BRIGHT_AMARELA: Final[str] = '\033[93m'
COR_VERDE: Final[str] = '\033[32m'
COR_BRIGHT_VERMELHA: Final[str] = '\033[91m'

# Habilita os caracteres ANSI escape no terminal Windows.
os.system("")

def bright_amarelo(conteudo: Any) -> Any:
    '''
    Colore o texto informado em amarelo brilhante.
    Retorna o texto colorido.
    '''
    return f"{COR_BRIGHT_AMARELA}{conteudo}{COR_BRANCA}"

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
            print(bright_vermelho('\tApenas números inteiros são aceitos. Por favor, tente novamente.\n'))

def exibir_mensagem_de_apresentacao(nome: str, idade: int, cidade: str, lazer: str) -> str:
    '''
    Monta uma mensagem com as entradas: nome, idade, cidade e adoro e exibi a mensagem.
    '''
    print(bright_amarelo(f"\n\tMeu nome é {nome}, tenho {idade} anos, moro em {cidade} e meu lazer preferido é {lazer}.") )

def obter_nome() -> str:
    '''
    Obtem o nome do usuário.
    Retorna o nome.
    '''
    while True:
        nome = input('\tSeu nome: ').title() 
        if nome != "":
            return nome
        else:
            print(bright_vermelho('\tO nome deve ser informado. Por favor, entre com o nome.'))

def obter_idade() -> int:
    '''
    Obtem a idade do usuário.
    Retorna a idade.
    '''
    while True:
        idade = input_int('\tSua idade: ') 
        if 6 < idade < 130:
            return idade
        else:
            print(bright_vermelho('\tValor da idade inválido.A idade deve ser maior que 6 e menor que 130.'))

def obter_cidade() -> str:
    '''
    Obtem a cidade informada pelo usuário.
    Retorna a cidade.
    '''
    while True:
        cidade = input('\tA cidade onde mora: ').title()  
        if cidade != "":
            return cidade
        else:
            print(bright_vermelho('\tA cidade deve ser informadA. Por favor, entre com a cidade.'))

def obter_lazer() -> str:
    '''
    Obtem o lazer informada pelo usuário.
    Retorna o lazer.
    '''
    while True:
        lazer = input('\tQual seu lazer preferido? ')  
        if lazer != "":
            return lazer
        else:
            print(bright_vermelho('\tUm lazer deve ser informadA. Por favor, entre com o lazer.'))

def main() -> None:
    '''
    Fluxo principal do programa.
    '''
    limpar_console()
    print(verde('\tEntre com os dados solicitados e receba uma mensagem de apresentação.\n'))
    nome = obter_nome()
    idade = obter_idade()
    cidade = obter_cidade()
    lazer = obter_lazer()
    exibir_mensagem_de_apresentacao(nome, idade, cidade, lazer)

if __name__ == '__main__':
    main()
   
