'''
Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.
'''

import os
import locale
import platform
from typing import Final
from typing import Any
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

LINHA_TRACEJADA: Final[str] = '-' * 51
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

def formatar_valor_monetario(valor:float) -> str:
    '''
    Formata valor para  moeda brasileira.
    '''
    moeda_formatada = locale.currency(valor, grouping=True)
    return moeda_formatada

def obter_horas_trabalhadas() -> float:
    '''
    Obtem as horas trabalhadas no mês usuario.
    Retorna a quantidade de horas válidas.
    '''
    while True:
        horas_trabalhadas_em_um_mes = input_float('\n\tHoras trabalhadas no mês: ') 
        if 0 < horas_trabalhadas_em_um_mes < 480:
            return horas_trabalhadas_em_um_mes
        else:
            print(bright_vermelho('\tQuantidade de horas está iválida. A quantidade deve ser maior que 0 e menor 480 horas.'))

def obter_valor_hora() -> float:
    '''
    Obtem o valor de uma hora trabalhada.
    Retorna o valor válido.
    '''
    while True:
        valor_hora = input_float('\n\tValor por hora: ')
        if 0 < valor_hora:
            return valor_hora
        else:
            print(bright_vermelho('\tValor da hora iválido! O valor deve ser maior que zero.'))

def calcular_salario_mensal_por_horas_trabalhadas(horas: float, valor_hora: float) -> float:
    '''
    Calcula o salario com base no numero de horas trabalhadas e o 
    valor recebido por hora.
    Retorna o salário do mês.
    '''
    salario_mensal = horas * valor_hora
    return salario_mensal

def main() -> None:
    '''
    Fluxo principal do programa.
    '''
    limpar_console()
    print(bright_amarelo('\tCalcule o valor do seu salário do mês.\n'))
    horas = obter_horas_trabalhadas()
    valor_hora = obter_valor_hora()
    resultado = calcular_salario_mensal_por_horas_trabalhadas(horas, valor_hora)
    print(bright_amarelo('\n\t#################### Resultado ######################'))
    print(bright_amarelo(f"\n\t\tO valor do salário é: {formatar_valor_monetario(resultado)}."))
    print(bright_amarelo('\n\t#####################################################'))

if __name__ == '__main__':
    main()
   
