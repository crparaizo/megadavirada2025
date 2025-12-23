from math import log10
from database_megavirada import resultadosMegaVirada

parametrosPrimeiraPosição = {
    'digito1': 0.301,   
    'digito2': 0.176,   
    'digito3': 0.125,   
    'digito4': 0.097,   
    'digito5': 0.079,   
    'digito6': 0.067,   
    'digito7': 0.058,   
    'digito8': 0.051,   
    'digito9': 0.046    
}            

# primeiroDigito = 1
# formula = 0
# formula = log10(1 + (1 / primeiroDigito))

parametrosSegundaPosição = {# frequência esperadas dos segundos digitos a Lei de Benford
    'digito0': 0.12,   
    'digito1': 0.114,   
    'digito2': 0.109, 
    'digito3': 0.104, 
    'digito4': 0.10, 
    'digito5': 0.97,  
    'digito6': 0.973, 
    'digito7': 0.9,   
    'digito8': 0.88,  
    'digito9': 0.85   
}            

# segundoDigito = 2
# formula = 0
# for primeiroDigito in range(1,10):  # primeiro dígito varia de 1 a 9
#     formula += log10(1 + (1 / ((10 * primeiroDigito)+segundoDigito)))


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
print(f"Ocorrências dos números: {ocorrencias}")


def pegar_primeiros_digitos(numeros: list):
    ocorrencias_digitos = {}
    for numero in numeros:
        primeiro_digito = numero // 10 
        if primeiro_digito in ocorrencias_digitos:
            ocorrencias_digitos[primeiro_digito] += 1
        else:
            ocorrencias_digitos[primeiro_digito] = 1
    return ocorrencias_digitos
ocorrencias_primeiros_digitos = pegar_primeiros_digitos(todos_os_numeros)
#print(f"Ocorrências dos primeiros dígitos: {ocorrencias_primeiros_digitos}")


def porcetagens_primeiros_digitos(ocorrencias_digitos: dict, total_numeros: int):
    porcentagens = {}
    for digito, ocorrencia in ocorrencias_digitos.items():
        porcentagem = (ocorrencia / total_numeros) * 100
        porcentagem = format(porcentagem, '.3f')
        porcentagens[digito] = porcentagem
    return porcentagens
porcentagens_primeiros_digitos = porcetagens_primeiros_digitos(ocorrencias_primeiros_digitos, len(todos_os_numeros))
# print(f"Porcentagens dos primeiros dígitos: {porcentagens_primeiros_digitos}")
 

def pegar_segundos_digitos(numeros: list):
    ocorrencias_digitos = {}
    for numero in numeros:
        segundo_digito = numero % 10
        if segundo_digito in ocorrencias_digitos:
            ocorrencias_digitos[segundo_digito] += 1
        else:
            ocorrencias_digitos[segundo_digito] = 1
    return ocorrencias_digitos    
ocorrencias_segundos_digitos = pegar_segundos_digitos(todos_os_numeros)
# print(f"Ocorrências dos segundos dígitos: {ocorrencias_segundos_digitos}")


def porcentagens_segundos_digitos(ocorrencias_digitos: dict, total_numeros: int):
    porcentagens = {}
    for digito, ocorrencia in ocorrencias_digitos.items():
        porcentagem = (ocorrencia / total_numeros) * 100
        porcentagem = format(porcentagem, '.3f')
        porcentagens[digito] = porcentagem
    return porcentagens
porcentagens_segundos_digitos = porcentagens_segundos_digitos(ocorrencias_segundos_digitos, len(todos_os_numeros))
# print(f"Porcentagens dos segundos dígitos: {porcentagens_segundos_digitos}")
