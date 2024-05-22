import random

def rolar_dados(lados):
    return random.randint(1, lados)

def definir_valor():
    numero_dados = int(input('Qual a quantidade de dados que deseja rolar? '))
    lados = int(input('Quantos lados terá o dado? '))

    resultados = [rolar_dados(lados) for _ in range(numero_dados)]
    soma = sum(resultados)
    print(f'\nRolando {numero_dados}d{lados}. Resultados: {resultados}')
    print(f'A soma dos resultados é {soma}')

definir_valor()