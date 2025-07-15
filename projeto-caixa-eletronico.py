print("=== Caixa Eletrônico ===")
print(" 1. Consultar saldo \n 2. Depositar \n 3. Sacar \n 4. Sair")

menu = "======================= \n    Caixa Eletrônico   \n======================= \n 1. Consultar saldo \n 2. Depositar \n 3. Sacar \n 4. Sair "
saldo = 0
opcao = input("Escolha uma opção: ")

while True:
    if opcao == "1":
        print(f"Saldo atual: R$ {saldo:.2f}")
        print(menu)
        opcao = input("Escolha outra opção: ")
    elif opcao == "2":
        deposito = float(input("Deseja depositar quanto: "))
        if deposito < 0:
                print("O valor do deposito tem que ser maior que 0 reais.")
        else:
                saldo = deposito + saldo
                print("Dinheiro depositado com sucesso!")
        print(menu)
        opcao = input("Escolha outra opção: ")
    elif opcao == "3":
        saque = float(input("Quanto deseja sacar: "))
        if saque > saldo:
                print("Valor maior que o saldo disponível!")
        else:
                saldo = saldo - saque
                print("Saque efetuado com sucesso!")
        print(menu)
        opcao = input("Escolha outra opção: ")
    elif opcao == "4":
        print("Saindo do sistema... até mais!")
        break
    elif opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida. Escolha 1, 2, 3 ou 4.")
        opcao = input("Escolha outra opção: ")