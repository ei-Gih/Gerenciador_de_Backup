# Módulos e Bibliotecas

import os
import datetime

print(os.listdir('exercicios'))
print(datetime.date.today())

# Para instalar uma blibioteca que não tem no python 
# ir no terminal;
# selecionar o cammand Prompt
# pip install nome_da_bliblioteca

lista_arquivos = os.listdir("arquivos")
# os.rename("arquivos/abr22.txt", "arquivos/22/abr22.txt")

for arquivo in lista_arquivos:
    if ".txt" in arquivo:
        if "22" in arquivo:
            os.rename(f"arquivos/{arquivo}", f"arquivos/22/{arquivo}")
        elif "23" in arquivo:
            os.rename(f"arquivos/{arquivo}", f"arquivos/23/{arquivo}")