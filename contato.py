contatos = {}

while True:
    print("\n1. Adicionar contato")
    print("2. Exibir contatos")
    print("3. Buscar contato")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do contato: ")
        telefone = input("Número do telefone: ")
        contatos[nome] = telefone

    elif opcao == "2":
        for nome, telefone in contatos.items():
            print(f"Nome: {nome}, Telefone: {telefone}")

    elif opcao == "3":
        nome = input("Nome do contato: ")
        if nome in contatos:
            print(f"Nome: {nome}, Telefone: {contatos[nome]}")
        else:
            print("Contato não encontrado.")

    elif opcao == "4":
        break

    else:
        print("Opção inválida.")
#por favor funciona não aguento mais