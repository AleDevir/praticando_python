'''
Receba do usuário a quantidade de litros de combustível consumidos e
a distância percorrida. Calcule e imprima o consumo médio em km/l.
'''

import os
import platform
from typing import Final
from typing import Any

COR_BRANCA: Final[str] = '\033[0;0m'
COR_VERDE: Final[str] = '\033[32m'
COR_BRIGHT_VERMELHA: Final[str] = '\033[91m'

# Habilita os caracteres ANSI escape no terminal Windows.
os.system("")

def input_float(msg: str) -> float:
    '''
    Obtem número inteiro informado pelo usuário.
    Retorna o número.
    '''
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print(bright_vermelho('\tApenas números são aceitos. Por favor, tente novamente.\n'))

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

def obter_quilometro() -> float:
    '''
    Obtem os quilômetros informados pelo usuário.
    Retorna os quilômetros válidos.
    '''
    
    while True:
        quilometros_informados =  input_float('\tQuilômetros percorridos (km): ')
        if quilometros_informados > 0:
            return quilometros_informados
        else:
            print(bright_vermelho('\tValor do quilômetro inválido. Entre com um valor acima de zero.'))

def obter_litro() -> float:
    '''
    Obtem os litros informado pelo usuário.
    Retorna os litros válidos.
    '''
    
    while True:
        litros_informados =  input_float('\tLitros consumidos (l): ') 
        if litros_informados > 0:
            return litros_informados
        else:
            print(bright_vermelho('\tValor do quilômetro inválido. Entre com um valor acima de zero.'))        

def calcular_consumo_km_por_litros(distancia: float, litros: float) -> float:
    '''
    Calcula o consumo médio de litros em determinada distância(km).
    Retorna o consumo.
    '''
    consumo = distancia / litros
    return consumo

def main() -> None:
    '''
    Fluxo principal do programa.
    '''
    limpar_console()
    print(verde('\tSaiba seu consumo médio de combustível por quilometro rodado.\n'))
    quilometros = obter_quilometro()   
    litros = obter_litro()
    consumo = calcular_consumo_km_por_litros(quilometros, litros)
    print(verde('\n\t########## Resultado #############'))
    print(verde(f"\n\t\tConsumo médio: {consumo:.2f}km/l"))
    print(verde('\n\t##################################'))

if __name__ == '__main__':
    main()
   
