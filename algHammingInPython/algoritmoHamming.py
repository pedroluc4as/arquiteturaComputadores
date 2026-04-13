while True:
    print("\n----Algoritmo de Hamming----")
    print("1. Codificar mensagem")
    print("2. Decodificar mensagem")
    print("0. Sair")
    
    opcao = input("Escolha uma opção e digite o número correspondente: ")
    
    if opcao == '1':
        print("\nInsira o conjunto de bits da mensagem original (máximo 8 bits): ")
        msgOriginal = input()
        print("\nCodificando o conjunto de bits da mensagem orignal...\n")
        # A lógica para ler e validar os 8 bits entra aqui
        
    elif opcao == '2':
        print("\nInsira o conjunto de bits da mensagem codificada (máximo 8 bits): ")
        msgCodificada = input()
        print("\nDecodificando o conjunto de bits da mensagem codificada...\n")
        # A lógica de decodificação entra aqui
        
    elif opcao == '0':
        print("\nEncerrando o programa...\nObrigado, Deus abençoe")
        break  # O break quebra o laço while e finaliza o programa
        
    else:
        print("\nOpção inválida!")
        print("\nDigite: ")
        print("\n0 para fechar o programa;")
        print("\n1 para codificar o conjunto de bits;")
        print("\n2 para decodificar o conjunto de bits.\n")