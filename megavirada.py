from database_megavirada import resultadosMegaVirada
import random

todos_os_numeros = list() 
for sorteios in resultadosMegaVirada:
    for numeros in sorteios:
        todos_os_numeros.append(numeros)
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


#números que mais foram sorteados:
def numerosMaisfrequentes(database: list):
    ocorrencias = {}    

    for sorteios in database:
        for numero in sorteios:
            if numero in ocorrencias:
                ocorrencias[numero] += 1
            else:
                ocorrencias[numero] = 1
    # Ordenar os números pela quantidade de ocorrências em ordem decrescente
    numeros_ordenados = sorted(ocorrencias.items(), key=lambda x: x[1], reverse=True)   
    # print("Números mais frequentes:")
    # for numero, quantidade in numeros_ordenados:
    #     print(f"Número {numero}: {quantidade} vezes")  

# numerosMaisfrequentes(resultadosMegaVirada)
 

#números que nunca foram sorteados:
def numerosNuncaSorteados(database: list):
    todos_numeros = set(range(1, 61))  
    numeros_sorteados = set()           

    for sorteios in database:
        for numero in sorteios:
            numeros_sorteados.add(numero)  

    numeros_nunca_sorteados = todos_numeros - numeros_sorteados  

    # print("Números que nunca foram sorteados:")
    # for numero in sorted(numeros_nunca_sorteados):
    #     print(numero)

# numerosNuncaSorteados(resultadosMegaVirada)


# numeros gerados aleatoriamente para a mega virada
def gerarNumerosAleatoriosMegaVirada():
    numeros_aleatorios = random.sample(range(1, 61), 6)
    numeros_aleatorios.sort()
    return numeros_aleatorios
# print(gerarNumerosAleatoriosMegaVirada())

def quantidadeNumerosImparesSorteados():
    numeros_impares = [num for num in todos_os_numeros if num % 2 != 0]
    return len(numeros_impares) 
    
print(quantidadeNumerosImparesSorteados())
    

def quantidadeNumerosParesSorteados():
    numeros_pares = [num for num in todos_os_numeros if num % 2 == 0]
    return len(numeros_pares) 
    
print(quantidadeNumerosParesSorteados())
