import tkinter as tk
from tkinter import messagebox

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

# Criando e posicionando os widgets
label_pessoa = tk.Label(root, text="Nome da Pessoa:")
label_pessoa.grid(row=0, column=0, padx=10, pady=5)

entry_pessoa = tk.Entry(root)
entry_pessoa.grid(row=0, column=1, padx=10, pady=5)

label_paes = tk.Label(root, text="Quantidade de Pães Consumidos:")
label_paes.grid(row=1, column=0, padx=10, pady=5)

entry_paes = tk.Entry(root)
entry_paes.grid(row=1, column=1, padx=10, pady=5)

btn_adicionar = tk.Button(root, text="Adicionar Consumo", command=adicionar_consumo)
btn_adicionar.grid(row=2, columnspan=2, padx=10, pady=10)

label_valor_total_paes = tk.Label(root, text="Valor Total dos Pães (R$):")
label_valor_total_paes.grid(row=3, column=0, padx=10, pady=5)

entry_valor_total_paes = tk.Entry(root)
entry_valor_total_paes.grid(row=3, column=1, padx=10, pady=5)

label_valor_total_refrigerantes = tk.Label(root, text="Valor Total dos Refrigerantes (R$):")
label_valor_total_refrigerantes.grid(row=4, column=0, padx=10, pady=5)

entry_valor_total_refrigerantes = tk.Entry(root)
entry_valor_total_refrigerantes.grid(row=4, column=1, padx=10, pady=5)

btn_calcular = tk.Button(root, text="Calcular Valor Total", command=calcular_valor_total)
btn_calcular.grid(row=5, columnspan=2, padx=10, pady=10)

# Iniciando o loop principal da janela
root.mainloop()