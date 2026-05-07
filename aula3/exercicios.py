# Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir
# que todos os registros tenham valores positivos para `quantidade` e `preço`.
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos
# forem positivos ou "Dados inválidos" caso contrário.

# Para começar a resolver o exercício, podemos criar um dicionário representando um registro de venda e, em seguida, usar uma estrutura condicional para verificar os valores de `quantidade` e `preço`. Aqui está um exemplo de como isso pode ser feito:
quantidade = 40
preco = 20

if quantidade > 0 and preco > 0:
    print("Dados válidos")
else:
    print("Dados inválidos")


# Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT.
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

temperatura = 25
if temperatura < 18:
    print("Baixa")
elif 18 <= temperatura <= 26:
    print("Normal")
else:
    print("Alta")


# Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`,
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

log = {'timestamp': '2021-06-23 10:00:00',
       'level': 'ERROR', 'message': 'Falha na conexão'}
if log['level'] == 'ERROR':
    print(log['message'])


# Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação,
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha
# fornecido um email válido. Escreva um programa que valide essas condições
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

idade = 10  # ex de valor, vai substituindo com input do usuario
email = "fulano@exemplo.com"  # ex de valor, vai substituindo com input do usuario

if not 18 <= idade <= 65:
    print("Idade inválida")
elif "@" not in email or "." not in email:
    print("Email invalido")
else:
    print("Dados de usuário válidos")
# OR

if 18 <= idade <= 65:
    if "@" in email and "." in email:
        print("Dados de usuário válidos")
    else:
        print("Dados de usuário inválidos")

# Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h).
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

transacao = {'valor': 12000, 'hora': 20}
if transacao['valor'] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
    print("Transação suspeita")
else:
    print("Transação normal")


# Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

# vamos montar um dicionario, exemplos praticos monte a nuvem de palavras, ou verificar quais produtos fazem parte de um e-commerce, ou quais são os produtos mais vendidos, ou quais são os produtos mais buscados, ou quais são os produtos mais comentados,
 # tipo um WEBSCRAPING, ou seja, a partir de um site, ou de um texto, ou de um comentário, ou de uma avaliação, ou de uma descrição,
 # vamos montar um dicionário, onde a chave é a palavra, e o valor é a quantidade de vezes que ela aparece no texto, ou seja, a frequência de cada palavra.

texto = "dados são importantes para a tomada de decisões, dados são a base para a análise de dados, dados são o combustível para a inteligência artificial"

# contagem_de_palavras = {}

# dados = 1 #for contado 1 vez
# e = 1 #for contado 1 vez
# decisão = 2 #for contado 2 vezes
# análise = 1 #for contado 1 vez

# Aqui é temos uma estrutura complexa, pq temos uma estrutura de INT dentro de outra estrutura
palavras = texto.split()
contagem_de_palavras = {}

for palavra in palavras:
    if palavra in contagem_de_palavras:
        contagem_de_palavras[palavra] += 1
    else:
        contagem_de_palavras[palavra] = 1

print(contagem_de_palavras)


# Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

lista_de_numeros = [10, 20, 30, 40, 50]
minimo = min(lista_de_numeros)
maximo = max(lista_de_numeros)

# Normalização para escala de 0 a 1
lista_normalizada = [(x - minimo) / (maximo - minimo)
                     for x in lista_de_numeros]

print(lista_normalizada)


# Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

lista_de_usuarios = [
    {'nome': 'Alice', 'email': 'alice@exemplo.com'},
    {'nome': 'Bob', 'email': 'bob@exemplo.com'},
    {'nome': 'Charlie', 'email': None},
    {'nome': 'David', 'email': ""}
]
usuarios_validos = [
    usuario for usuario in lista_de_usuarios if usuario['email']]
print(usuarios_validos)

# Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

numeros = range(1, 101)  # ou seja, de 1 a 100
# outra forma [num for num in lista_de_numeros if num % 2 == 0]
numeros_pares = [x for x in numeros if x % 2 == 0]
# pq x nesse caso é o elemento da lista, ou seja, o número, e a condição é que o número seja par, ou seja, o resto da divisão por 2 seja igual a 0
# mas se em vez de x colocasse n daria também certo, pq o nome da variável é irrelevante, o importante é a estrutura da compreensão de lista, ou seja, a parte antes do for é o valor que vai ser adicionado na nova lista, a parte depois do for é a iteração sobre a lista original, e a parte depois do if é a condição para incluir o elemento na nova lista.
print(numeros_pares)

# Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {'categoria': 'Eletrônicos', 'valor': 1000},
    {'categoria': 'Roupas', 'valor': 500},
    {'categoria': 'Eletrônicos', 'valor': 1500},
    {'categoria': 'Roupas', 'valor': 800},
    {'categoria': 'Alimentos', 'valor': 300}
]
total_vendas_categoria = {}

for venda in vendas:
    categoria = venda['categoria']
    valor = venda['valor']
    if categoria in total_vendas_categoria:
        total_vendas_categoria[categoria] += valor
    else:
        total_vendas_categoria[categoria] = valor
print(total_vendas_categoria)

# Exercícios com WHILE

# Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
dados = []
entrada = ""
while True:
    entrada = input("Digite um dado (ou 'sair' para encerrar): ")
    if entrada.lower() == "sair":
        break
    dados.append(entrada)
# OR

dados = []
entrada = ""
while entrada.lower() != "sair":
    entrada = input("Digite um dado (ou 'sair' para encerrar): ")
    if entrada.lower() == "sair":
        break
    dados.append(entrada)
print(dados)

# Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
numero = int(input("Digite um número entre 1 e 10: "))
while numero < 1 or numero > 10:
    print("Número inválido. Tente novamente.")
    numero = int(input("Digite um número entre 1 e 10: "))
print(f"Número válido: {numero}")


# Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

url_atual = "https://api.exemplo.com/dados?page=1"
urls_totais = ["https://api.exemplo.com/dados?page=1",
               "https://api.exemplo.com/dados?page=2", "https://api.exemplo.com/dados?page=3"]

while url_atual in urls_totais:
    print(f"Processando dados da {url_atual}")
    # Simular a obtenção da próxima URL (página) - aqui estamos apenas incrementando o número da página
    pagina_atual = int(url_atual.split("page=")[-1])
    pagina_proxima = pagina_atual + 1
    url_atual = f"https://api.exemplo.com/dados?page={pagina_proxima}"
print("Todas as páginas foram processadas.")

# Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

tentativas_maximas = 5
tentativa = 1

while tentativa <= tentativas_maximas:
    print(f"Tentativa {tentativa} de {tentativas_maximas}...")
    # Simular uma tentativa de conexão (aqui você pode adicionar lógica para simular sucesso ou falha)
    sucesso = False  # Simulando falha
    if sucesso:
        print("Conexão bem-sucedida!")
        break
    else:
        print("Falha na conexão. Tentando novamente...")
        tentativa += 1

# Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

itens = [1, 2, 3, 4, 5, "para", 6, 7, 8, 9, 10]
i = 0
while i < len(itens):
    item = itens[i]
    if item == "para":
        print(f"Valor de parada encontrado: {item}")
        break
    print(f"Processando item: {item}")
    i += 1
