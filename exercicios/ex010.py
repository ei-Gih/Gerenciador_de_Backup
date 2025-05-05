#cadastrar o novo produto (se o produto não existir)
#caso o produto exista ele vai edittar o produto
#além disso: o programa tem que no final atualizar o preço de todos os produtos para o novos valores
#são 10% a mais que o preço original

dic_produtos={"airpod":2000 ,"ipad":9000, "iphone":6000, "macbook":11000}

nome_produto = input("Nome do produto")
preco_produto= input("valor do produto")

nome_produto=nome_produto.lower()
preco_produto=float(preco_produto)


dic_produtos[nome_produto]= [preco_produto]
print(dic_produtos)


for produto in dic_produtos:
    novo_preco=dic_produtos[produto] * 1.1
    dic_produtos[produto]=novo_preco

print(dic_produtos)