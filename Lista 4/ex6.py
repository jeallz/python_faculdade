opcao = 0

while opcao != 3:
    print("\nMenu")
    print("1 - Olá")
    print("2 - Tchau")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Olá!")
    elif opcao == 2:
        print("Tchau!")
    elif opcao == 3:
        print("Saindo do programa...")
    else:
        print("Opção inválida!")