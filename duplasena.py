# Fonte dos dados:
#https://github.com/guto-alves/loterias-api

url = "https://loteriascaixa-api.herokuapp.com/api/duplasena"

import requests as api
from megasena import contar_ocorrencias, numerosMaisfrequentes, numerosNuncaSorteados, quantidadeNumerosImparesSorteados, quantidadeNumerosParesSorteados


resultadosDuplaSena = api.get(url).json()
# print(resultadosDuplaSena)

todos_os_numeros = list() 
for resultado in resultadosDuplaSena:
    dezenas = resultado['dezenas']
    for numero in dezenas:
        todos_os_numeros.append(int(numero))  
todos_os_numeros.sort()
# print(f"Números: {todos_os_numeros}")

ocorrencias = contar_ocorrencias(todos_os_numeros)
# print(f"Ocorrências dos números: {ocorrencias}")

frequentes = numerosMaisfrequentes(resultadosDuplaSena)
print("Números mais frequentes na Dupla Sena:")
for numero, frequencia in frequentes:
    print(f"Número {numero}: {frequencia} vezes")

numerosNuncaSorteados(resultadosDuplaSena,51)
print("Números que nunca foram sorteados na Dupla Sena:")
for numero in numerosNuncaSorteados(resultadosDuplaSena,51):
    print(numero)

impares = quantidadeNumerosImparesSorteados(todos_os_numeros)
print(f"Quantidade de números ímpares sorteados: {impares}")        

pares = quantidadeNumerosParesSorteados(todos_os_numeros)
print(f"Quantidade de números pares sorteados: {pares}")    




