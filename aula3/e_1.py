itens = [1, 2, 3, 4, 5, "para", 6, 7, 8, 9, 10]
i = 0
while i < len(itens):
    item = itens[i]
    if item == "para":
        print(f"Valor de parada encontrado: {item}")
        break
    print(f"Processando item: {item}")
    i += 1
