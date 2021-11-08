# Dictionary Comprehension em Python - (Compreensão de dicionários)
# var - Variável qualquer dentro da Comprehension

l1 = [1, 2, 3, 4, 5, 6]
l2 = [var * 2 for var in l1]
print(f'\n l1 = [1, 2, 3, 4, 5, 6]: \n {l1}')
print(f'\n l2 = [var * 2 for var in l1]:\n {l2}')
# ------------------------------------------------------
lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2')
]
# ch - variável da chave
# val - variavel da chave
var1 = {ch: val for ch, val in lista}
print(f'\n var = ch: val for ch, val in lista \n {var1}')
# ------------------------------------------------------
var2 = dict(lista)
print(f'\n var2 = dict(lista): \n {var2}')
# ------------------------------------------------------
var3 = {ch: val.replace('a', '@') for ch, val in lista}
print(f'\n var3 = ch: val.replace("a", "@") for ch, val in lista: \n {var3}')
# ------------------------------------------------------
var4 = {f"chave_{cha}": cha ** 2 for cha in range(10)}

print(f'\n var4 = f"chave_ cha ": cha ** 2 for cha in range(10): \n {var4}')
