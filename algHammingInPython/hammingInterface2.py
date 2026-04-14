import tkinter as tk
from tkinter import messagebox

#importação da biblioteca tkinter para a interface grafica e as mensagens de quando se fecha o programa

def calcular_r(m):
    """Calcula a quantidade de bits de paridade necessários."""
    r = 0
    while (2**r < m + r + 1):
        r += 1
    return r

def codificar_mensagem():
    # Pega o valor inserido na interface gráfica
    msgOriginal = entry_cod_msg.get()
    m = len(msgOriginal)
    
    # Valida para aceitar qualquer tamanho entre 1 e 8 bits
    if m > 8 or m == 0 or not all(bit in '01' for bit in msgOriginal):
        messagebox.showerror("Erro!", "A mensagem deve ter no máximo 8 bits e conter apenas 0 e 1!")
        return

    # Descobre a quantidade de bits de paridade (r) necessários dinamicamente
    r = calcular_r(m)
    tamanho_total = m + r
    
    # vetor preenchido com 0, que sera o tamanho da msgCodificada
    hamming = [0] * tamanho_total

    # disposicao da mensagem inserida nos campos de dados, lembrando que os bits de paridade
    # ficam nas posições de 2^M então sao as posicoes 1, 2, 4 e 8.
    # ajustando os dados para o indice que se inicia em 0
    j = 0
    for i in range(1, tamanho_total + 1):
        # Se a posição 'i' não for uma potência de 2, é posição de dado
        if (i & (i - 1)) != 0:
            hamming[i - 1] = int(msgOriginal[j])
            j += 1

    # cálculo dos bits de paridade usando XOR que é (^), com cada bit e armazenando
    # nas posicoes reservadas anteriormente para o bit de paridade
    for i in range(r):
        posicao_paridade = 2**i
        valor_paridade = 0
        for k in range(1, tamanho_total + 1):
            if k & posicao_paridade:
                valor_paridade ^= hamming[k - 1]
        hamming[posicao_paridade - 1] = valor_paridade

    # aqui pega e armazena na msgFinal e exibe de forma corrida como texto usando o .join
    msgFinal = ''.join(map(str, hamming)) 
    
    # Identifica as posições de paridade para mostrar ao usuário conforme o trabalho exige
    posicoes_paridade = ", ".join([str(2**i) for i in range(r)])
    
    # Atualiza o texto do resultado na interface exibindo a mensagem codificada formatada
    # A fonte aqui é um pouco maior (12) conforme solicitado e a cor igual ao botão
    lbl_resultado_cod.config(text=f"Mensagem codificada:\n{msgFinal}\n\nPosições de paridade: {posicoes_paridade}", fg=COR_TEXTO_CODIFICAR, font=("TkFixedFont", 12, "bold"))

def decodificar_mensagem():
    # Pega os bits inseridos na opção de decodificar
    msgCodificada = entry_dec_msg.get()
    n = len(msgCodificada)
    
    # Validação para no máximo 12 bits, conforme o limite de 8 bits originais codificados
    if n == 0 or n > 12 or not all(bit in '01' for bit in msgCodificada):
        messagebox.showerror("Erro!", "A mensagem codificada deve ter no máximo 12 bits e conter apenas 0 e 1!")
        return
        
    # Transforma o texto inserido em um vetor de inteiros
    hamming = [int(bit) for bit in msgCodificada]
    
    # Descobre quantos bits de paridade tem na mensagem recebida
    r = 0
    while (2**r <= n):
        r += 1
        
    # Recalcula a paridade usando XOR para achar a Síndrome (onde está o erro)
    sindrome = 0
    for i in range(r):
        posicao_paridade = 2**i
        valor_paridade = 0
        for k in range(1, n + 1):
            if k & posicao_paridade:
                valor_paridade ^= hamming[k - 1]
        # Se o XOR não der 0, soma a posição na síndrome
        if valor_paridade != 0:
            sindrome += posicao_paridade
            
    info_erro = ""
    # Se a sindrome for maior que 0, significa que um erro foi detectado
    if sindrome > 0:
        if sindrome <= n:
            info_erro = f"Aviso: Erro detectado na posição {sindrome}. Corrigindo...\n"
            # Inverte o bit errado para corrigir a mensagem (XOR com 1 faz a inversão)
            hamming[sindrome - 1] ^= 1
        else:
            info_erro = "Erro múltiplo não corrigível detectado.\n"

    # Extrai a mensagem original pulando os bits de paridade (que são potências de 2)
    msgOriginal = ""
    for i in range(1, n + 1):
        if (i & (i - 1)) != 0:
            msgOriginal += str(hamming[i - 1])
            
    # Exibe o resultado da decodificação na tela
    # A fonte aqui é um pouco maior (12) e a cor igual ao botão
    lbl_resultado_dec.config(text=f"{info_erro}Mensagem original decodificada:\n{msgOriginal}", fg=COR_TEXTO_DECODIFICAR, font=("TkFixedFont", 12, "bold"))

#mensagem quando fecha o programa usando a lib do tk, so exibe uma mensagem para o usario que o programa fechou, só pra nao sumir do nada da tela...
def fechar_programa():
    messagebox.showinfo("Sair", "Encerrando o programa...\nObrigado, Deus abençoe!")
    janela.destroy()

#INTERFACE GRÁFICA (Tkinter)
#Cores da interface
#Aqui se define as cores de todo a interface, dai ao inves de digitar a cor de cada coisa na
#mao eu so coloco o nome da que eu quero, seria tipo o define em C
COR_FUNDO = "#E6F2FF"       
COR_TEXTO = "#003366"       
COR_BOTAO_CODIFICAR = "#0037FF"
COR_TEXTO_CODIFICAR = "#0037FF"
COR_BOTAO_DECODIFICAR = "#09FF00"  
COR_TEXTO_DECODIFICAR = "#09FF00"
COR_BOTAO_HOVER = "#000000" 
COR_SAIR = "#FF0000"  

#versao DOS - ficou ruim '-'
#COR_FUNDO = "#000000"
#COR_TEXTO = "#00FF00"       
#COR_BOTAO_CODIFICAR = "#004400" 
#COR_TEXTO_CODIFICAR = "#00FF00" 
#COR_BOTAO_DECODIFICAR = "#004400"
#COR_TEXTO_DECODIFICAR = "#00FF00"
#COR_BOTAO_HOVER = "#006600"
#COR_SAIR = "#330000"    
    
# Criação e configuração da janela principal do sistema
janela = tk.Tk()
janela.title("Algoritmo de Hamming")
janela.geometry("700x700")
#coloquei este tamanho por conta do tamanho da fonte que é maior do que o usual
#a fonte puxa a fonte de onde o programa está sendo executado, é a TkFixedFont propria do Tk
janela.configure(padx=20, pady=20, bg=COR_FUNDO)

# ----- SEÇÃO 1: CODIFICAR -----
# Define o quadro (frame) visual que vai agrupar os elementos da parte de codificação
frame_codificar = tk.LabelFrame(janela, text="1. Codificar Mensagem", padx=10, pady=10, bg=COR_FUNDO, fg=COR_TEXTO, font=("TkFixedFont", 14, "bold"))
frame_codificar.pack(fill="both", expand=True, pady=(0, 10))

# Label: Texto de instrução para o usuário inserir os bits
tk.Label(frame_codificar, text="Insira a mensagem original (máximo 8 bits):", bg=COR_FUNDO, fg=COR_TEXTO, font=("TkFixedFont", 14, "bold")).pack(anchor="w")

# Entry: Caixa de texto onde o usuário vai digitar a mensagem
entry_cod_msg = tk.Entry(frame_codificar, width=35, font=("TkFixedFont", 14, "bold"))
entry_cod_msg.pack(pady=5)

# Button: Botão que executa a função de codificar mensagem ao ser clicado
btn_cod = tk.Button(frame_codificar, text="Codificar", command=codificar_mensagem, bg=COR_BOTAO_CODIFICAR, fg="white", activebackground=COR_BOTAO_HOVER, activeforeground="white", font=("TkFixedFont", 14, "bold"), relief="flat", cursor="spraycan") 
#cursor de pintado o codigo inserido (quer dizer que esta codificado!kkkkkk)
btn_cod.pack(pady=5)

# Label: Espaço reservado e invisível inicialmente, usado para mostrar o resultado depois
lbl_resultado_cod = tk.Label(frame_codificar, text="", justify="center", font=("TkFixedFont", 14, "bold"), bg=COR_FUNDO)
lbl_resultado_cod.pack(pady=5)

# ----- SEÇÃO 2: DECODIFICAR -----
# Define o quadro (frame) visual que vai agrupar os elementos da parte de decodificação
frame_decodificar = tk.LabelFrame(janela, text="2. Decodificar Mensagem", padx=10, pady=10, bg=COR_FUNDO, fg=COR_TEXTO, font=("TkFixedFont", 14, "bold"))
frame_decodificar.pack(fill="both", expand=True, pady=(0, 10))

# Label: Texto de instrução para o usuário inserir a mensagem codificada
tk.Label(frame_decodificar, text="Insira a mensagem codificada (máximo 12 bits):", bg=COR_FUNDO, fg=COR_TEXTO, font=("TkFixedFont", 14, "bold")).pack(anchor="w")

# Entry: Caixa de texto para digitar os bits a serem decodificados
entry_dec_msg = tk.Entry(frame_decodificar, width=35, font=("TkFixedFont", 14, "bold"))
entry_dec_msg.pack(pady=5)

# Button: Botão que executa a função de decodificar mensagem
btn_dec = tk.Button(frame_decodificar, text="Decodificar", command=decodificar_mensagem, bg=COR_BOTAO_DECODIFICAR, fg="white", activebackground=COR_BOTAO_HOVER, activeforeground="white", font=("TkFixedFont", 14, "bold"), relief="flat", cursor="coffee_mug")
#cursor voltando ao que era antes depois de muito café (decodificando)
btn_dec.pack(pady=5)

#Label: Espaço para exibir o resultado da decodificação ou os avisos de erro encontrados
lbl_resultado_dec = tk.Label(frame_decodificar, text="", justify="center", font=("TkFixedFont", 14, "bold"), bg=COR_FUNDO)
lbl_resultado_dec.pack(pady=5)

#mensagem do programador(Pedro Sperandio)
lbl_titulo = tk.Label(janela, text="Trabalho de Arquitetura de Computadores\npor: Pedro Sperandio\npara: Vladimir Piccolo Barcelos\nObrigado!", justify="center", font=("Consolas", 10, "bold"), bg=COR_FUNDO, fg=COR_TEXTO)
lbl_titulo.pack(side="right", pady=(0, 15))

#BOTÃO SAIR
# Button: Botão de encerramento geral do programa
btn_sair = tk.Button(janela, text="Sair", command=fechar_programa, bg=COR_SAIR, fg="white", activebackground="#000000", activeforeground="white", font=("TkFixedFont", 14, "bold"), width=15, relief="flat", cursor="X_cursor") #kkkkkkk botaozinho fera X(CLOSE), amei python
btn_sair.pack(pady=10)

# Mantém a interface gráfica aberta rodando em loop infinito até que seja fechada
janela.mainloop()