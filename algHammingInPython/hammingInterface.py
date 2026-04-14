import tkinter as tk
from tkinter import messagebox

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
    lbl_resultado_cod.config(text=f"Mensagem codificada:\n{msgFinal}\n\nPosições de paridade: {posicoes_paridade}", fg="blue")

def decodificar_mensagem():
    # Pega os bits inseridos na opção de decodificar
    msgCodificada = entry_dec_msg.get()
    n = len(msgCodificada)
    
    if n == 0 or not all(bit in '01' for bit in msgCodificada):
        messagebox.showerror("Erro!", "A mensagem deve conter apenas 0 e 1!")
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
    lbl_resultado_dec.config(text=f"{info_erro}Mensagem original decodificada:\n{msgOriginal}", fg="green")

def fechar_programa():
    messagebox.showinfo("Sair", "Encerrando o programa...\nObrigado, Deus abençoe!")
    janela.destroy()

# ==================== INTERFACE GRÁFICA (Tkinter) ====================
# Criação e configuração da janela principal do sistema
janela = tk.Tk()
janela.title("Algoritmo de Hamming")
janela.geometry("450x550")
janela.configure(padx=20, pady=20)

# Título Principal
lbl_titulo = tk.Label(janela, text="---- Algoritmo de Hamming ----", font=("Arial", 14, "bold"))
lbl_titulo.pack(pady=(0, 20))

# ----- SEÇÃO 1: CODIFICAR -----
# Agrupa os elementos de codificação dentro de um quadro visual
frame_codificar = tk.LabelFrame(janela, text="1. Codificar Mensagem", padx=10, pady=10)
frame_codificar.pack(fill="both", expand=True, pady=(0, 10))

tk.Label(frame_codificar, text="Insira a mensagem original (máximo 8 bits):").pack(anchor="w")
entry_cod_msg = tk.Entry(frame_codificar, width=30)
entry_cod_msg.pack(pady=5)

btn_cod = tk.Button(frame_codificar, text="Codificar", command=codificar_mensagem, bg="#e0e0e0")
btn_cod.pack(pady=5)

lbl_resultado_cod = tk.Label(frame_codificar, text="", justify="left", font=("Arial", 10, "bold"))
lbl_resultado_cod.pack(pady=5)

# ----- SEÇÃO 2: DECODIFICAR -----
# Agrupa os elementos de decodificação dentro de um quadro visual
frame_decodificar = tk.LabelFrame(janela, text="2. Decodificar Mensagem", padx=10, pady=10)
frame_decodificar.pack(fill="both", expand=True, pady=(0, 10))

tk.Label(frame_decodificar, text="Insira a mensagem codificada:").pack(anchor="w")
entry_dec_msg = tk.Entry(frame_decodificar, width=30)
entry_dec_msg.pack(pady=5)

btn_dec = tk.Button(frame_decodificar, text="Decodificar", command=decodificar_mensagem, bg="#e0e0e0")
btn_dec.pack(pady=5)

lbl_resultado_dec = tk.Label(frame_decodificar, text="", justify="left", font=("Arial", 10, "bold"))
lbl_resultado_dec.pack(pady=5)

# ----- BOTÃO SAIR -----
btn_sair = tk.Button(janela, text="0. Sair", command=fechar_programa, bg="#ffcccc", width=15)
btn_sair.pack(pady=10)

# Mantém a interface gráfica aberta rodando em loop
janela.mainloop()