# Fonte dos dados:
#https://github.com/guto-alves/loterias-api

url = "https://loteriascaixa-api.herokuapp.com/api/lotofacil"

import requests as api
from megasena import contar_ocorrencias, numerosMaisfrequentes, numerosNuncaSorteados, quantidadeNumerosImparesSorteados, quantidadeNumerosParesSorteados


resultadosLotofacil = api.get(url).json()
# print(resultadosLotofacil)

todos_os_numeros = list() 
for resultado in resultadosLotofacil:
    dezenas = resultado['dezenas']
    for numero in dezenas:
        todos_os_numeros.append(int(numero))  
todos_os_numeros.sort()
# print(f"Números: {todos_os_numeros}")

ocorrencias = contar_ocorrencias(todos_os_numeros)
# print(f"Ocorrências dos números: {ocorrencias}")

frequentes = numerosMaisfrequentes(resultadosLotofacil)
print("Números mais frequentes na Lotofácil:")
for numero, frequencia in frequentes:
    print(f"Número {numero}: {frequencia} vezes")

numerosNuncaSorteados(resultadosLotofacil,26)
print("Números que nunca foram sorteados na Lotofácil:")
for numero in numerosNuncaSorteados(resultadosLotofacil,26):
    print(numero)

impares = quantidadeNumerosImparesSorteados(todos_os_numeros)
print(f"Quantidade de números ímpares sorteados: {impares}")        

pares = quantidadeNumerosParesSorteados(todos_os_numeros)
print(f"Quantidade de números pares sorteados: {pares}")    