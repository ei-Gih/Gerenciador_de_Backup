# inputs
email= input("escreva seu e-mail: ")

fatoramento = float(input("Escreva o faturamento "))#transformar texto em numero
 

# Listas
vendas=[100,20,50,14,20,30,700]

# soma dos elementos
total_vendas=sum(vendas)
print(total_vendas)

# tamanho da lista
quantidade_vendas =len(vendas)
print(quantidade_vendas)

# max e min
print(max(vendas))
print(min(vendas))

# pegar possição
print(vendas[0])
print(vendas[-1])

print(11 in vendas)

# adicionar um item 
vendas.append(10)
print(vendas)

# remover um item
vendas.remove(700) #ou
vendas.pop(3) #remove pelo numero da posição
print(vendas) 

# editar um item
vendas[0]=1000
print (vendas)

# contar quantas vezes um item aparece na lista
print(vendas.count(20))

# ordenar uma lista
vendas.sort() # ordem crescente
print(vendas)

vendas.sort(reverse=True) #ordem decrescente
print(vendas)