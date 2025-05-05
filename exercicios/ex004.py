# Exercício que calcula o lucro e a margem de lucro de uma empresa com base no faturamento, custo e imposto.
#forma de  fazer junçao/mescla de variaveis e textos

faturamento = 1200
custo = 700
imposto=faturamento * 0.1  #valores de % devem ser add em numeros decimais
lucro = faturamento - custo - imposto

Margem_lucro= lucro/faturamento

print("O Faturamento da empresa é: {}, Custo: {}, Lucro: {}" . format(faturamento, custo,lucro))
print("A margem de lucro foi de ", Margem_lucro)

#ou

print(f"O Faturamento da empresa é: {faturamento}, Custo: {custo}, Lucro: {lucro}")
print("A margem de lucro foi de ", Margem_lucro)
