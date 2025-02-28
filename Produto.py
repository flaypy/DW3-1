produtos = []

while True:
    print("\n1. Adicionar produto")
    print("2. Exibir produtos")
    print("3. Buscar produto")
    print("4. Calcular valor total do produto")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade em estoque: "))
        produtos.append([nome, preco, quantidade])

    elif opcao == "2":
        for p in produtos:
            print(f"Nome: {p[0]}, Preço: {p[1]}, Quantidade: {p[2]}")

    elif opcao == "3":
        nome = input("Nome do produto: ")
        for p in produtos:
            if p[0] == nome:
                print(f"Nome: {p[0]}, Preço: {p[1]}, Quantidade: {p[2]}")
                break
        else:
            print("Produto não encontrado.")

    elif opcao == "4":
        nome = input("Nome do produto: ")
        for p in produtos:
            if p[0] == nome:
                print(f"Valor total em estoque: {p[1] * p[2]}")
                break
        else:
            print("Produto não encontrado.")

    elif opcao == "5":
        break

    else:
        print("Opção inválida.")
