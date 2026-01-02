# Fonte dos dados:
#https://github.com/guto-alves/loterias-api

url = "https://loteriascaixa-api.herokuapp.com/api/lotomania"

import requests as api
from megasena import contar_ocorrencias, numerosMaisfrequentes, numerosNuncaSorteados, quantidadeNumerosImparesSorteados, quantidadeNumerosParesSorteados


resultadosLotomania = api.get(url).json()
# print(resultadosLotomania)

todos_os_numeros = list() 
for resultado in resultadosLotomania:
    dezenas = resultado['dezenas']
    for numero in dezenas:
        todos_os_numeros.append(int(numero))  
todos_os_numeros.sort()
# print(f"Números: {todos_os_numeros}")

ocorrencias = contar_ocorrencias(todos_os_numeros)
# print(f"Ocorrências dos números: {ocorrencias}")

frequentes = numerosMaisfrequentes(resultadosLotomania)
print("Números mais frequentes na Lotomania:")
for numero, frequencia in frequentes:
    print(f"Número {numero}: {frequencia} vezes")

numerosNuncaSorteados(resultadosLotomania,101)
print("Números que nunca foram sorteados na Lotomania:")
for numero in numerosNuncaSorteados(resultadosLotomania,101):
    print(numero)

impares = quantidadeNumerosImparesSorteados(todos_os_numeros)
print(f"Quantidade de números ímpares sorteados: {impares}")        

pares = quantidadeNumerosParesSorteados(todos_os_numeros)
print(f"Quantidade de números pares sorteados: {pares}")    