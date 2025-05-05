from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Comandos Essenciais de Python - Lista Comentada", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.set_text_color(30, 30, 120)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Courier", "", 10)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 5, body)
        self.ln()

# Conteúdo
sections = [
    ("Variáveis e Tipos de Dados", """
x = 10          # Atribui o valor 10 à variável x
nome = "Ana"    # String (texto)
preco = 19.90   # Float (número com vírgula)
ativo = True    # Booleano (True ou False)
"""),
    ("Entrada e Saída", """
input("Digite seu nome: ")  # Lê uma entrada do usuário como string
print("Olá, mundo!")        # Imprime algo na tela
"""),
    ("Operadores Matemáticos", """
+   # Soma
-   # Subtração
*   # Multiplicação
/   # Divisão
//  # Divisão inteira (sem casas decimais)
%   # Módulo (resto da divisão)
**  # Potência (ex: 2 ** 3 = 8)
"""),
    ("Condicionais (if, elif, else)", """
if idade >= 18:
    print("Maior de idade")
elif idade == 17:
    print("Quase lá")
else:
    print("Menor de idade")
"""),
    ("Laços de Repetição", """
# For loop com range()
for i in range(5):
    print(i)

# While loop
x = 0
while x < 5:
    print(x)
    x += 1
"""),
    ("Funções", """
def saudacao(nome):              # Define uma função com parâmetro
    print(f"Olá, {nome}!")

saudacao("Lucas")                # Chama a função
"""),
    ("Listas", """
frutas = ["maçã", "banana", "uva"]
frutas.append("laranja")
frutas.remove("banana")
print(frutas[0])
"""),
    ("Strings", """
texto = "Python é legal"
print(len(texto))         
print(texto.upper())      
print(texto.lower())      
print(texto.replace("legal", "incrível"))
"""),
    ("Dicionários", """
aluno = {"nome": "João", "idade": 20}
print(aluno["nome"])
aluno["curso"] = "Python"
"""),
    ("Tuplas e Conjuntos", """
tupla = (1, 2, 3)               
conjunto = {1, 2, 3, 3}         
print(conjunto)
"""),
    ("Funções Embutidas Comuns", """
len()       # Tamanho de lista, string, etc.
sum()       # Soma dos itens de uma lista
type()      # Retorna o tipo de uma variável
range()     # Cria uma sequência de números
enumerate() # Itera lista com índice e valor
zip()       # Une duas listas elemento por elemento
"""),
    ("Trabalhando com Arquivos", """
# Escrevendo
with open("arquivo.txt", "w") as f:
    f.write("Olá, mundo!")

# Lendo
with open("arquivo.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)
"""),
    ("Tratamento de Erros", """
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Isso não é um número válido.")
"""),
    ("Módulos Comuns", """
import math
print(math.sqrt(25))

import random
print(random.randint(1, 10))
""")
]

# Criar PDF
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

for title, body in sections:
    pdf.chapter_title(title)
    pdf.chapter_body(body)

# Salvar
pdf_path = "/mnt/data/Comandos_Python_Comentados.pdf"
pdf.output(pdf_path)
pdf_path
