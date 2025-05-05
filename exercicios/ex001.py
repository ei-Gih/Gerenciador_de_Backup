# Formatação em textos

email_cliente = "qualqueremail@gmail.com"

# MAIUSCULA
email_cliente=email_cliente.upper()
print(email_cliente)

# minuscula
email_cliente=email_cliente.lower()
print(email_cliente)

# Localizar o "@"
print(email_cliente.find("@")) # -1 quando não encontrar

# Tamanho do texto
print(len(email_cliente))

# Pegar um caracter
print(email_cliente[4]) # se colocar numero negativo ele contara de tras para frente
print(email_cliente[:4]) # pegaum pedaço,ou seja,vai do 0 até o index escolhido

# Trocar um pedaço do texto
novo_email =email_cliente.replace("gmail.com", "hotmail.com") #substituir
print(novo_email)

nome = "joao lira"
# Editar nomes
print(nome.capitalize())
print(nome.title())

#exercicio
##pegar o servidor do email
posicao_arroba= email_cliente.find("@") + 1
servidor =email_cliente[posicao_arroba:]
print(servidor)

##pegar o nome
posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco]
print(primeiro_nome)

##pegar o sobrenome
sobrenome= nome[posicao_espaco+1:]
print(sobrenome)


# Casos Especiais - formatação numéricas em texto
margem_lucro= 1900*0.01
margem_lucro=round(margem_lucro,2)
print(f"Margem de Lucro: {margem_lucro:.0%}")
