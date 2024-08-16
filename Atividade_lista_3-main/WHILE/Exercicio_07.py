def mostrar_menu():
    print("Escolha uma das opções:")
    print("1 - Eu programo em Python")
    print("2 - Eu programo em PHP")
    print("3 - Eu programo em Java")

def main():
    while True:
        mostrar_menu()
        
        # Solicita a escolha do usuário
        opcao = input("Digite a opção desejada (1, 2 ou 3): ")
        
        # Verifica a opção escolhida e exibe a mensagem correspondente
        if opcao == '1':
            print("Eu estou estudando Python!")
            break
        elif opcao == '2':
            print("Eu estou estudando PHP!")
            break
        elif opcao == '3':
            print("Eu estou estudando Java!")
            break
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")
            
if __name__ == "__main__":
    main()