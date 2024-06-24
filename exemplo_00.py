def soma(valor1: float, valor2: float) -> float:
    resultado = valor1 + valor2
    return resultado


#Calcular Média de Valores em uma Lista
from typing import List
lista_de_numeros = [1,2,3,4,5,67,68,69]

def calcularmedia(valores:list[float]) -> float:
    return sum(valores)/len(valores)

#calcularmedia(lista_de_numeros)

#Filtrar Dados Acima de um Limite
lista_de_numeros = [1,2,3,4,5,67,68,69]
def filtrar_acima_de(valores: list[float], limite: float) -> list[float]:
    numeros_filtrados = []
    for valor in valores:
        if valor > limite:
           numeros_filtrados.append(valor)
    print(numeros_filtrados)       

#filtrar_acima_de(lista_de_numeros, 60)

#Contar Valores Únicos em uma Lista
lista_de_numeros = [1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 8, 9, 10]

def contar_valores_unicos(valores):
    '''
    extraindo valores unicos iterando sobre a lista
    '''
    lista_de_numeros_exlusivos = []
    for valor in valores:
        if valor not in lista_de_numeros_exlusivos:
            lista_de_numeros_exlusivos.append(valor)

    print(lista_de_numeros_exlusivos)        

#contar_valores_unicos(lista_de_numeros)

lista_de_numeros = [1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 8, 9, 10]
def contar_valores_unicos(valores):
    '''
    extraindo valores unicos transformando a lista em um set
    SET: Os itens definidos são desordenados, imutáveis ​​e não permitem valores duplicados.
    '''
    print(set(valores))

#contar_valores_unicos(lista_de_numeros)

#Converter Celsius para Fahrenheit em uma Lista
def converter_temperatura_celsius_fahrenheit(temperatura_celsius: List[float]) -> list[float]:
    ''''
    Onde C é a temperatura em graus Celsius e F, a temperatura em Fahrenheit. 
    Ao simplificarmos a fórmula, temos: F = C x 1,8 + 32.
    '''
    lista_conversao = []
    fahrenheit = (temperatura_celsius * 1.8) + 32
    lista_conversao.append(fahrenheit)
    print(lista_conversao)

#converter_temperatura_celsius_fahrenheit(32)

def celsius_para_fahrenheit(temperaturas_celsius: List[float]) -> List[float]:
    print ([(9/5) * temp + 32 for temp in temperaturas_celsius])

#celsius_para_fahrenheit([32])