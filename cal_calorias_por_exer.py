'''
Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.

'''

import os
import platform
from typing import Final
from typing import Any


LINHA_TRACEJADA: Final[str] = '-' * 51
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

def obter_horas_de_treino_por_semana() -> float:
    '''
    Obtem a quantidade de horas de treino por semana.
    Retorna o quantidade válida.
    '''
    while True:
        quantidade_de_horas_de_treino_por_semana = input_float('\n\tHoras de treino por semana: ') 
        if 0 < quantidade_de_horas_de_treino_por_semana:
            return quantidade_de_horas_de_treino_por_semana
        else:
            print(bright_vermelho('\tQuantidade iválida! O valor deve ser maior que zero.'))

def calcular_calorias_queimadas(horas_por_semana: float) -> float:
    '''
    Calcula quantidade de calorias queimadas em um mês de acordo com as 
    horas de exercicio fornecidas pelo usuário. Base calculo calorico: 5cal/minuto de exercicio
    Retorna o total calorico queimado.
    '''
    media_calorica_por_minuto = 5
    calorias_gastas_por_hora = media_calorica_por_minuto * 60
    horas_no_mes = horas_por_semana * 4
    calorias_queimadas_no_mes = calorias_gastas_por_hora * horas_no_mes
    return calorias_queimadas_no_mes

def main() -> None:
    '''
    Fluxo principal do programa.
    '''
    limpar_console()
    print(verde('\tCalcule seu gasto calórico por mês.\n'))
    horas_de_treino_por_semana = obter_horas_de_treino_por_semana()
    gasto_calorico = calcular_calorias_queimadas(horas_de_treino_por_semana)
    print(bright_amarelo(f"\n\tPara {horas_de_treino_por_semana} horas de treino por semana, você queima {gasto_calorico:.2f} calorias por mês."))
    

if __name__ == '__main__':
    main()
   
