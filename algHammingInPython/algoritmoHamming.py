while True:
    print("\n----Algoritmo de Hamming----")
    print("1. Codificar mensagem")
    print("2. Decodificar mensagem")
    print("0. Sair")
    
    opcao = input("Escolha uma opção e digite o número correspondente: ")
    
    if opcao == '1':
        print("\nInsira o conjunto de bits da mensagem original (máximo 8 bits): ")
        msgOriginal = input()
        if len(msgOriginal) > 8 or not all(bit in '01' for bit in msgOriginal):
            print("Erro! A mensagem deve ter no máximo 8 bits e conter apenas 0 e 1!\n")
            print("Retornando a tela inicial...\n")
            continue

        msgOriginal = msgOriginal.zfill(8)
        print("\nMensagem inserida padronizada para 8 bits: ", msgOriginal)

        hamming = [0] * 12 #vetor com 12 posições preenchidas com 0, que sera o tamanho da msgCodificada

        #disposicao da mensagem inserida nos campos de dados, lembrando que os bits de paridade
        #ficam nas posições de 2^M então sao as posicoes 1, 2, 4 e 8, agora ajustando os dados
        #para o indice que se inicia em 0 fica: 
        # 3->2, 5->4, 6->5 e assim por diante
        hamming[2] = int(msgOriginal[0]) # posicao 3
        hamming[4] = int(msgOriginal[1]) # posicao 5
        hamming[5] = int(msgOriginal[2]) # posicao 6
        hamming[6] = int(msgOriginal[3]) #....
        hamming[8] = int(msgOriginal[4])
        hamming[9] = int(msgOriginal[5])
        hamming[10] = int(msgOriginal[6])
        hamming[11] = int(msgOriginal[7])

        print("Mensagem inserida nas posições adequadas do conjunto a ser codificado: ", hamming)


        
    elif opcao == '2':
        print("\nInsira o conjunto de bits da mensagem codificada: ")
        msgCodificada = input()
        if len(msgCodificada) > 12 or not all(bit in '01' for bit in msgCodificada):
            print("Erro! A mensagem deve ter no máximo 12 bits e conter apenas 0 e 1!\n")
            print("Retornando a tela inicial...\n")
            continue
        msgCodificada = msgCodificada.zfill(12)
        
    elif opcao == '0':
        print("\nEncerrando o programa...\nObrigado, Deus abençoe")
        break  # O break quebra o laço while e finaliza o programa
        
    else:
        print("\nOpção inválida!")
        print("\nDigite: ")
        print("\n0 para fechar o programa;")
        print("\n1 para codificar o conjunto de bits;")
        print("\n2 para decodificar o conjunto de bits.\n")#