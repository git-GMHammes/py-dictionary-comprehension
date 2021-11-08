carrinho = []
carrinho.append(('produto1', 30))
carrinho.append(('produto2', 20))
carrinho.append(('produto3', 50))
# ---------------------------------
print(f'\n {carrinho}')
carrinho = list(carrinho)
var1 = [(pro, pre) for pro, pre in carrinho]
print(f'\n {var1}')
# ---------------------------------
var2 = sum([float(val) for pro, val in carrinho])
print(f'\n var2 = [sum(float(val)) for pro, val in carrinho]: \n Valor: {var2}')
