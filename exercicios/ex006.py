# Condição

# > maior que
# < menor que
# >= maior ou igual
# <= menor opu igaul
# == igual
# != diferente

vendas=1500
meta=1300

if vendas >= meta:
    print("vendedor ganha bônus")
    print("Bateu a meta de vendas")
    bonus= 0.1 * vendas
    print("Bônus do vendedor: ", bonus)
else:
    print("Vendedor não ganha bônus")
    print("Não bateu a meta de vendas")


#2º cenario
vendas= 1600
meta1= 1300 # ganha 10%
meta2= 2000 # ganha 20%

if vendas >= 2000:
    bonus= 0.20 * vendas
else:
    if vendas >= 1300:
        bonus= 0.1 * vendas
    else:
        bonus= 0

print("bonus: ", bonus)

#ou
vendas= 1600
meta1= 1300 # ganha 10%
meta2= 2000 # ganha 20%

if vendas >= 2000:
    bonus= 0.20 * vendas
elif vendas >= 1300:
        bonus= 0.1 * vendas
else:
    bonus= 0

print("bonus: ", bonus)