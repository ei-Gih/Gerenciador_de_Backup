# Exercício que verifica se um produto procurado pelo usuário está disponível em uma lista de estoque.

lista_produtos=["airpod", "ipad", "iphone", "macbook"]
produto_procurado= input("Procure um produto: ")
produto_procurado= produto_procurado.lower()

if produto_procurado in lista_produtos:
    print("Produto no estoque")
else:
    print("Não temos este produto")