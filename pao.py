import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk # type: ignore

# Lista para armazenar as quantidades de pães consumidos por pessoa
consumo_paes = []

def adicionar_consumo():
    try:
        # Obtendo os valores dos widgets de entrada
        pessoa = entry_pessoa.get()
        paes_consumidos = int(entry_paes.get())

        # Adicionando o consumo à lista
        consumo_paes.append((pessoa, paes_consumidos))

        # Limpar os campos de entrada
        entry_pessoa.delete(0, tk.END)
        entry_paes.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

def calcular_valor_total():
    try:
        # Obtendo o valor total dos pães e dos refrigerantes
        valor_total_paes = float(entry_valor_total_paes.get())
        valor_total_refrigerantes = float(entry_valor_total_refrigerantes.get())

        # Calculando o valor total consumido de pães
        total_paes_consumidos = sum(qtd_paes for pessoa, qtd_paes in consumo_paes)
        valor_total_consumido_paes = total_paes_consumidos * valor_total_paes

        # Calculando o valor total consumido de refrigerantes
        valor_total_consumido_refrigerantes = valor_total_refrigerantes

        # Calculando o valor a pagar por pessoa (considerando pães e refrigerantes)
        valor_a_pagar = {}
        for pessoa, qtd_paes in consumo_paes:
            valor_por_pessoa_paes = qtd_paes * valor_total_paes / total_paes_consumidos
            valor_total_por_pessoa = valor_por_pessoa_paes + (valor_total_refrigerantes / len(consumo_paes))
            valor_a_pagar[pessoa] = valor_total_por_pessoa

        # Exibindo o resultado
        resultado = "Valor a pagar por pessoa:\n"
        for pessoa, valor in valor_a_pagar.items():
            resultado += f"{pessoa}: R${valor:.2f}\n"

        messagebox.showinfo("Resultados", resultado)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora de Lanche da Noite")

# Carregando a primeira imagem e convertendo para um formato tkinter
imagem1 = Image.open("./img/pao.jpeg")
imagem1.thumbnail((150, 150))  # Redimensionando a imagem
imagem1 = ImageTk.PhotoImage(imagem1)

# Carregando a segunda imagem e convertendo para um formato tkinter
imagem2 = Image.open("./img/coca.png")
imagem2.thumbnail((150, 150))  # Redimensionando a imagem
imagem2 = ImageTk.PhotoImage(imagem2)

# Criando e posicionando os widgets
label_imagem1 = tk.Label(root, image=imagem1)
label_imagem1.grid(row=0, column=0, padx=5, pady=5)

label_imagem2 = tk.Label(root, image=imagem2)
label_imagem2.grid(row=0, column=1, padx=5, pady=5)

label_pessoa = tk.Label(root, text="Nome da Pessoa:")
label_pessoa.grid(row=1, column=0, padx=10, pady=5)

entry_pessoa = tk.Entry(root)
entry_pessoa.grid(row=1, column=1, padx=10, pady=5)

label_paes = tk.Label(root, text="Quantidade de Pães Consumidos:")
label_paes.grid(row=2, column=0, padx=10, pady=5)

entry_paes = tk.Entry(root)
entry_paes.grid(row=2, column=1, padx=10, pady=5)

btn_adicionar = tk.Button(root, text="Adicionar Consumo", command=adicionar_consumo)
btn_adicionar.grid(row=3, columnspan=2, padx=10, pady=10)

label_valor_total_paes = tk.Label(root, text="Valor Total dos Pães (R$):")
label_valor_total_paes.grid(row=4, column=0, padx=10, pady=5)

entry_valor_total_paes = tk.Entry(root)
entry_valor_total_paes.grid(row=4, column=1, padx=10, pady=5)

label_valor_total_refrigerantes = tk.Label(root, text="Valor Total dos Refrigerantes (R$):")
label_valor_total_refrigerantes.grid(row=5, column=0, padx=10, pady=5)

entry_valor_total_refrigerantes = tk.Entry(root)
entry_valor_total_refrigerantes.grid(row=5, column=1, padx=10, pady=5)

btn_calcular = tk.Button(root, text="Calcular Valor Total", command=calcular_valor_total)
btn_calcular.grid(row=6, columnspan=2, padx=10, pady=10)

def exibir_lista_pessoas():
    # Verificar se a janela já está aberta
    if hasattr(exibir_lista_pessoas, 'janela_pessoas') and exibir_lista_pessoas.janela_pessoas.winfo_exists():
        janela_pessoas = exibir_lista_pessoas.janela_pessoas
        # Limpar a janela antes de atualizar
        for widget in janela_pessoas.winfo_children():
            widget.destroy()
    else:
        # Criar uma nova janela se não estiver aberta
        janela_pessoas = tk.Toplevel(root)
        janela_pessoas.title("Lista de Pessoas")
        exibir_lista_pessoas.janela_pessoas = janela_pessoas

    # Adicionar botões para alterar e excluir pessoas e alterar quantidade de pães
    for i, (pessoa, paes_consumidos) in enumerate(consumo_paes):
        label_pessoa = tk.Label(janela_pessoas, text=f"Pessoa {i+1}: {pessoa} - Pães Consumidos: {paes_consumidos}")
        label_pessoa.grid(row=i, column=0, padx=10, pady=5)

        # Botão para alterar quantidade de pães
        btn_alterar_paes = tk.Button(janela_pessoas, text="Alterar Pães", command=lambda pessoa=pessoa: alterar_paes(pessoa))
        btn_alterar_paes.grid(row=i, column=1, padx=5, pady=5)

        # Botão para excluir pessoa
        btn_excluir_pessoa = tk.Button(janela_pessoas, text="Excluir Pessoa", command=lambda pessoa=pessoa: excluir_pessoa(pessoa))
        btn_excluir_pessoa.grid(row=i, column=2, padx=5, pady=5)

def alterar_paes(pessoa):
    # Encontrar o índice da pessoa na lista de consumo_paes
    index = next((i for i, (p, _) in enumerate(consumo_paes) if p == pessoa), None)
    if index is not None:
        novo_valor = tk.simpledialog.askinteger("Alterar Pães", f"Novo valor de pães consumidos para {pessoa}:",
                                                initialvalue=consumo_paes[index][1])
        if novo_valor is not None:
            consumo_paes[index] = (pessoa, novo_valor)
            # Atualizar a exibição da lista de pessoas
            exibir_lista_pessoas()

def excluir_pessoa(pessoa):
    # Remover a pessoa da lista de consumo_paes
    consumo_paes[:] = [p for p in consumo_paes if p[0] != pessoa]
    # Atualizar a exibição da lista de pessoas
    exibir_lista_pessoas()

# Adicionar um botão para exibir a lista de pessoas
btn_exibir_lista_pessoas = tk.Button(root, text="Exibir Lista de Pessoas", command=exibir_lista_pessoas)
btn_exibir_lista_pessoas.grid(row=7, columnspan=2, padx=10, pady=10)


# Iniciando o loop principal da janela
root.mainloop()
