# Fonte dos dados:
#https://github.com/guto-alves/loterias-api

url = "https://loteriascaixa-api.herokuapp.com/api/maismilionaria"

import requests as api
from megasena import contar_ocorrencias, numerosMaisfrequentes, numerosNuncaSorteados, quantidadeNumerosImparesSorteados, quantidadeNumerosParesSorteados


resultadosMilionaria = api.get(url).json()
# print(resultadosMilionaria)

todos_os_numeros = list() 
for resultado in resultadosMilionaria:
    dezenas = resultado['trevos']
    for numero in dezenas:
        todos_os_numeros.append(int(numero))  
todos_os_numeros.sort()
# print(f"Números: {todos_os_numeros}")

ocorrencias = contar_ocorrencias(todos_os_numeros)
print(f"Ocorrências dos números: {ocorrencias}")

frequentes = numerosMaisfrequentes(resultadosMilionaria)
print("Números mais frequentes na Milionária:")
for numero, frequencia in frequentes:
    print(f"Número {numero}: {frequencia} vezes")

numerosNuncaSorteados(resultadosMilionaria,51)
print("Números que nunca foram sorteados na Milionária:")
for numero in numerosNuncaSorteados(resultadosMilionaria,51):
    print(numero)

impares = quantidadeNumerosImparesSorteados(todos_os_numeros)
print(f"Quantidade de números ímpares sorteados: {impares}")        

pares = quantidadeNumerosParesSorteados(todos_os_numeros)
print(f"Quantidade de números pares sorteados: {pares}")    