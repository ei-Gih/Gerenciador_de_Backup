# Dicionario

# dic_produtos={"chave":valor,"chave2":valor2, "chave3":valor}
dic_produtos={"airpod":[2000, 100],"ipad":[9000,260], "iphone":6000, "macbook":[11000, 500]}

# pegar um elemento
print(dic_produtos["iphone"])

# editar um elemento
dic_produtos["iphone"]= dic_produtos["iphone"] * 1.3
print(dic_produtos)

# quantidade de itens
print(len(dic_produtos))

# retirar um item do dicionario
dic_produtos.pop("airpod")
print(dic_produtos)

# adicionar um item no dicionario
dic_produtos["appli watch"]= 2500
print(dic_produtos)

# verificar se um item existe no dicionário
#verificar se uma chave existe
if "iphone" in dic_produtos:
    print("existe Produto")
else: print("Não existe")

#verificar se um valor existe nos valores do dicionário
if 9000 in dic_produtos.values():
    print("existe Produto")
else: print("Não existe")
