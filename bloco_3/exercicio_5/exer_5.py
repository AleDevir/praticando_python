'''
exercicio 5 do Desafio 3 - Crie duas tuplas. Concatene-as para formar uma nova tupla.
'''


def main() -> None:
    '''
    Fluxo Principal do Programa.
    '''
    tupla_1 = (1, 2)
    tupla_2 = ('a', 'b')
    tupla_3 = tupla_1 + tupla_2
    print(f"\n\t Tupla 1: {tupla_1} Tupla 2: {tupla_2} e Tupla concatenada {tupla_3}\n")


if __name__ == '__main__':
    main()
