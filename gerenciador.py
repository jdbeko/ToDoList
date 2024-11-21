import tkinter as tk
from tkinter import messagebox

# função para adicionar tarefa
def adicionar_tarefa(): # a função adicionar_tarefa captura o texto digitado no campo de entrada (entrada_tarefa) usando get().
    tarefa = entrada_tarefa.get()
    if tarefa != "":
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("aviso", "digite uma tarefa para adicionar!") #o messagebox é um módulo que exibe caixas de diálogo para mostrar mensagens ao usuário. Ele é usado para exibir informações, alertas, erros ou solicitar confirmações (como "Sim" ou "Não").

# função para remover a tarefa selecionada
def remover_tarefa(): # a função remover_tarefa tenta obter o índice da tarefa selecionada na lista usando curselection 
    try:
        indice_selecionado = lista_tarefas.curselection()[0]
        lista_tarefas.delete(indice_selecionado)
    except IndexError:
        messagebox.showwarning("aviso", "selecione uma tarefa para remover!")

# função para marcar tarefa como concluída
def concluir_tarefa(): # O índice da tarefa selecionada é obtido e, em seguida, o texto da tarefa é alterado para adicionar "(concluída)".
    try:
        indice_selecionado = lista_tarefas.curselection()[0]
        tarefa = lista_tarefas.get(indice_selecionado)
        lista_tarefas.delete(indice_selecionado)
        lista_tarefas.insert(indice_selecionado, f"{tarefa} (concluída)")
        lista_tarefas.itemconfig(indice_selecionado, {'fg': 'green'})
    except IndexError:
        messagebox.showwarning("aviso", "selecione uma tarefa para marcar como concluída!")

# configuração da janela principal 
janela = tk.Tk()
janela.title("Gerenciador de Tarefas")

# campo de entrada de tarefa # tk.Entry cria um campo de entrada de texto onde o usuário pode digitar as tarefas.
entrada_tarefa = tk.Entry(janela, width=40)
entrada_tarefa.grid(row=0, column=0, padx=10, pady=10)

# botão para adicionar tarefa # O parâmetro command=adicionar_tarefa associa a função adicionar_tarefa ao clique do botão.
btn_adicionar = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa)
btn_adicionar.grid(row=0, column=1, padx=10, pady=10)

# lista de tarefas #tk.Listbox cria uma lista de tarefas onde os itens podem ser selecionados. A opção selectmode=tk.SINGLE permite selecionar uma tarefa por vez.
lista_tarefas = tk.Listbox(janela, width=50, height=10, selectmode=tk.SINGLE)
lista_tarefas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# botão para remover tarefa 
btn_remover = tk.Button(janela, text="Remover Tarefa", command=remover_tarefa)
btn_remover.grid(row=2, column=0, padx=10, pady=10, sticky="e")

#botão para marcar tarefa como concluída
btn_concluir = tk.Button(janela, text="Concluir Tarefa", command=concluir_tarefa)
btn_concluir.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# inicia o loop da aplicação # mainloop() inicia o loop principal da aplicação, permitindo que a interface gráfica funcione e aguarde interações do usuário.
janela.mainloop()

