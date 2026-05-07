

# Desafio - Integre na solução anterior, da aula 2 (Refatorar) um fluxo de While que repita o fluxo até que o usuário insira as informações corretas

# 1) Inserir as váriaveis que farão com que o fluxo tenha controle do loop, ou seja, o nome, o salário e o bônus
nome = False
salario = False
bonus = False

# 2) Criar um loop while que verifique se as informações inseridas são válidas, vamos começar pelo nome
# 2.1) Loop para o nome, ou seja, enquanto o nome for vazio ou conter números, ele deve solicitar que o usuário insira um nome válido

while not nome:
    try:
        nome = input("Digite seu nome: ")
        if len(nome) == 0:
            raise ValueError("O nome não pode ser vazio.")
        elif any(char.isdigit() for char in nome):
            # verifica se o nome contém números e lança um erro caso seja verdade
            raise ValueError("O nome não pode conter números.")
        else:
            print(f"Olá, {nome}! Bem-vindo ao curso de Python para Dados!")
    except ValueError as e:
        print(f"Erro: {e}")
        nome = False  # Reinicia a variável para continuar o loop

# 2.2) Loop para o salário
while not salario:
    try:
        salario = float(input("Digite seu salário: "))
        if salario < 0:
            raise ValueError("O salário não pode ser negativo.")
    except ValueError:
        print("Erro: certifique-se de que o salário é um número válido e não negativo.")
        salario = False  # Reinicia a variável para continuar o loop

# 2.3) Loop para o bônus
while not bonus:
    try:
        bonus = float(input("Digite a porcentagem do bônus: "))
        if bonus < 0:
            raise ValueError("O bônus não pode ser negativo.")
            print("Erro: certifique-se de que o bônus é um número válido e não negativo.")
        else:
            bonus = True
    except ValueError:
        print("Erro: certifique-se de que o bônus é um número válido e não negativo.")


# 4) Calcule o valor do bônus final

valor_do_bonus = 1000 + salario * bonus
kpi = valor_do_bonus + salario / 1000

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"Olá {nome}, o seu salário é R${salario:.2f} e o seu bônus foi de {valor_do_bonus:.2f}")
print(f"Seu KPI é: {kpi:.2f}")
