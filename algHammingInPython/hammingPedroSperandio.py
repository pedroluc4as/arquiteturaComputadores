while True:
    print("\n----Algoritmo de Hamming----")
    print("1. Codificar mensagem")
    print("2. Decodificar mensagem")
    print("0. Sair")
    
    opcao = input("Escolha uma opção e digite o número correspondente: ")
    
    if opcao == '1':
        print("\nInsira o conjunto de bits da mensagem original (máximo 8 bits): ")
        msgOriginal = input()
        m = len(msgOriginal)
        
        # Valida para aceitar qualquer tamanho entre 1 e 8 bits
        if m > 8 or m == 0 or not all(bit in '01' for bit in msgOriginal):
            print("Erro! A mensagem deve ter entre 1 e 8 bits e conter apenas 0 e 1!\n")
            print("Retornando a tela inicial...\n")
            continue

        msgEspacada = " ".join(msgOriginal) 
        print(f"\nMensagem inserida:\n{msgEspacada}")

        # Descobre a quantidade de bits de paridade (r) necessários dinamicamente
        r = 0
        while (2**r < m + r + 1):
            r += 1

        tamanho_total = m + r
        hamming = [0] * tamanho_total

        # Disposição da mensagem inserida nos campos de dados
        # Usamos um laço para funcionar com qualquer tamanho
        j = 0
        for i in range(1, tamanho_total + 1):
            # Se a posição 'i' não for uma potência de 2, é posição de dado (D)
            if (i & (i - 1)) != 0:
                hamming[i - 1] = int(msgOriginal[j])
                j += 1

        print("\nCodificando...")

        # Cálculo dos bits de paridade usando XOR (^) dinamicamente
        for i in range(r):
            posicao_paridade = 2**i
            valor_paridade = 0
            for k in range(1, tamanho_total + 1):
                # Se o bit k faz parte do grupo da paridade atual, faz o XOR
                if k & posicao_paridade:
                    valor_paridade ^= hamming[k - 1]
            hamming[posicao_paridade - 1] = valor_paridade

        msgFinal = ' '.join(map(str, hamming)) 
        print(f"\nMensagem final codificada ({tamanho_total} bits):\n{msgFinal}")

        # --- EXIBIÇÃO VISUAL ALINHADA E DINÂMICA ---
        print("\n--- Mapa de Construção da Mensagem ---")
        
        # Formata as posições numéricas (ex: 01 02 03...)
        posicoes = " ".join([f"{i:02d}" for i in range(1, tamanho_total + 1)])
        print(f"Posições:  {posicoes}")
        
        # Formata a legenda (ex: P1 P2 D  P4 D ...)
        funcoes = []
        for i in range(1, tamanho_total + 1):
            if (i & (i - 1)) == 0:
                funcoes.append(f"P{i:<2}")
            else:
                funcoes.append("D ")
        print(f"Função:    {' '.join(funcoes)}")
        
        # Formata os bits alinhados
        linha_bits = "  ".join(map(str, hamming))
        print(f"Bits:       {linha_bits}")
        print("\nLegenda: \nP = Bit de Paridade | D = Bit de Dado original")
        
    elif opcao == '2':
        print("\nInsira o conjunto de bits da mensagem codificada: ")
        msgCodificada = input()
        if len(msgCodificada) > 12 or not all(bit in '01' for bit in msgCodificada):
            print("Erro! A mensagem deve ter no máximo 12 bits e conter apenas 0 e 1!\n")
            print("Retornando a tela inicial...\n")
            continue
        # A lógica de decodificação entra aqui
        
    elif opcao == '0':
        print("\nEncerrando o programa...\nObrigado, Deus abençoe")
        break          
    else:
        print("\nOpção inválida!")
        print("\nDigite: ")
        print("\n0 para fechar o programa;")
        print("\n1 para codificar o conjunto de bits;")
        print("\n2 para decodificar o conjunto de bits.\n")