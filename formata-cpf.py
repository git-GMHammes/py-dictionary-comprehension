#
# formatar cpf por ponto com List Comprehension
#
cpf = input('Digite apenas os numeros do CPF: ')
print(f'\n CPF: {cpf}')
# ----------------------------------------------------------------------
verificador = cpf[9:11]
print(f'{verificador}')
n = 3
lista = [cpf[i:i + n] for i in range(0, 9, n)]
print(f'\n {lista}')
formata = '.'.join(lista) + '-' + verificador
print(f'\n CPF formatado: {formata}')
