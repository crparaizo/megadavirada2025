import requests as api

from database_megasena import url

# resultados da mega sena desde 1996
resultadosMegaSena = api.get(url).json()
# print(resultadosMegaSena)


# dezenas sorteadas desde 1996
# for resultado in resultadosMegaSena:
#     print(f"Dezenas: {(resultado['dezenas'])}")


todos_os_numeros = list() 
for resultado in resultadosMegaSena:
    dezenas = resultado['dezenas']
    for numero in dezenas:
        todos_os_numeros.append(int(numero))
todos_os_numeros.sort()
# print(f"Números: {todos_os_numeros}")


def contar_ocorrencias(numeros: list):
    ocorrencias = {}
    for numero in numeros: 
        if numero in ocorrencias:
            ocorrencias[numero] += 1
        else:
            ocorrencias[numero] = 1
    return ocorrencias
ocorrencias = contar_ocorrencias(todos_os_numeros)
# print(f"Ocorrências dos números: {ocorrencias}")


# números que mais foram sorteados:
def numerosMaisfrequentes(database: list):
    todos_os_numeros = []
    for resultado in database:
        dezenas = resultado['dezenas']
        for numero in dezenas:
            todos_os_numeros.append(int(numero))
    ocorrencias = {}
    for numero in todos_os_numeros:
        if numero in ocorrencias:
            ocorrencias[numero] += 1
        else:
            ocorrencias[numero] = 1
    numeros_frequentes = sorted(ocorrencias.items(), key=lambda x: x[1], reverse=True)
    return numeros_frequentes
# frequentes = numerosMaisfrequentes(resultadosMegaSena)
# print("Números mais frequentes na Mega Sena:")
# for numero, frequencia in frequentes:
#     print(f"Número {numero}: {frequencia} vezes")

# números que nunca foram sorteados:
def numerosNuncaSorteados(database: list):
    todos_os_numeros = []
    for resultado in database:
        dezenas = resultado['dezenas']
        for numero in dezenas:
            todos_os_numeros.append(int(numero))
    numeros_sorteados = set(todos_os_numeros)
    todos_numeros = set(range(1, 61))
    numeros_nunca_sorteados = todos_numeros - numeros_sorteados
    return sorted(numeros_nunca_sorteados)
# nunca_sorteados = numerosNuncaSorteados(resultadosMegaSena)
# print("Números que nunca foram sorteados na Mega Sena:")
# for numero in nunca_sorteados:
#     print(numero)


def quantidadeNumerosImparesSorteados():
    numeros_impares = [num for num in todos_os_numeros if num % 2 != 0]
    return len(numeros_impares) 
    
# print(quantidadeNumerosImparesSorteados())
    

def quantidadeNumerosParesSorteados():
    numeros_pares = [num for num in todos_os_numeros if num % 2 == 0]
    return len(numeros_pares) 
    
# print(quantidadeNumerosParesSorteados())
