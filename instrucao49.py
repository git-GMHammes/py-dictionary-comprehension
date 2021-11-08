#
# formatar string por ponto com List Comprehension
#
string = '0123456789012345678901234567890123456789012345678901234567890123456789'
print(f'\n {string}')
# ------------------------------------------------------------------------------------
n = 10
print(f'\n Variável n = {n}')
# ------------------------------------------------------------------------------------
separa = string[0:10]
print(f'\n separa = string[0:10]: {separa}')
# ------------------------------------------------------------------------------------
lista = [i for i in range(0, len(string), n)]
print(f'\n lista = [i for i in range(0, len(string), n)]:\n {lista}')
# ------------------------------------------------------------------------------------
lista2 = [(i, i + n) for i in range(0, len(string), n)]
print(f'\n lista2 = [(i, i + n) for i in range(0, len(string), n)]:\n {lista2}')
# ------------------------------------------------------------------------------------
lista3 = [string[i:i + n] for i in range(0, len(string), n)]  # range(inicio, total, salto)
print(f'\n lista3 = [string[i:i + n] for i in range(0, len(string), n)]:\n {lista3}')
# ------------------------------------------------------------------------------------
retorno = '.'.join(lista3)
print(f'\n {retorno}')
# ------------------------------------------------------------------------------------
# range() só em uma variável não retorna nada
# range() precisa estar um uma lista ou iteração
ran1 = list(range(50))
ran2 = list(range(25, 50))
ran3 = list(range(25, 50, 10))
print(f'\n {ran1}')
print(f'\n {ran2}')
print(f'\n {ran3}')
