import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from utils import copiar_pdfs


def selecionar_pasta(entry_field, title):
    caminho = filedialog.askdirectory(title=title)
    if caminho:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, caminho)


def adicionar_colaborador(entry_field, listbox, colaboradores):
    nome = entry_field.get().strip()
    if not nome:
        messagebox.showwarning("Atenção", "Digite o nome do colaborador antes de adicionar.")
        return

    if nome in colaboradores:
        messagebox.showinfo("Informação", f"O colaborador '{nome}' já foi adicionado.")
        entry_field.delete(0, tk.END)
        return

    colaboradores.append(nome)
    listbox.insert(tk.END, nome)
    entry_field.delete(0, tk.END)


def iniciar_copia(origem_entry, destino_entry, colaboradores, log_widget):
    origem_texto = origem_entry.get().strip()
    destino_texto = destino_entry.get().strip()

    if not origem_texto:
        messagebox.showerror("Erro", "Informe a pasta de origem.")
        return
    if not destino_texto:
        messagebox.showerror("Erro", "Informe a pasta de destino.")
        return

    pasta_origem = os.path.abspath(origem_texto)
    pasta_destino = os.path.abspath(destino_texto)

    if not os.path.isdir(pasta_origem):
        messagebox.showerror("Erro", "A pasta de origem não existe.")
        return
    if os.path.exists(pasta_destino) and not os.path.isdir(pasta_destino):
        messagebox.showerror("Erro", "O caminho de destino não é uma pasta válida.")
        return

    if pasta_origem == pasta_destino:
        messagebox.showerror("Erro", "A pasta de origem e a pasta de destino não podem ser iguais.")
        return

    if not colaboradores:
        messagebox.showerror("Erro", "Adicione pelo menos um nome de colaborador.")
        return

    try:
        copiados = copiar_pdfs(pasta_origem, pasta_destino, colaboradores)
        log_widget.config(state=tk.NORMAL)
        log_widget.delete("1.0", tk.END)

        if copiados:
            for arquivo in copiados:
                log_widget.insert(tk.END, f"✅ Copiado: {arquivo}\n")
            log_widget.insert(tk.END, "\n✅ Processo finalizado!\n")
            messagebox.showinfo("Sucesso", "Cópia de PDFs concluída com sucesso.")
        else:
            log_widget.insert(tk.END, "⚠️ Nenhum PDF correspondente foi encontrado.\n")
            messagebox.showinfo("Aviso", "Nenhum PDF correspondeu aos nomes informados.")

        log_widget.config(state=tk.DISABLED)
    except Exception as exc:
        messagebox.showerror("Erro", "Ocorreu um erro ao copiar os PDFs:\n" + str(exc))


def _create_dark_button(parent, text, command):
    button = tk.Button(
        parent,
        text=text,
        command=command,
        bg="#7c3aed",
        fg="#ffffff",
        activebackground="#6d28d9",
        activeforeground="#ffffff",
        bd=0,
        relief="flat",
        padx=15,
        pady=8,
        font=("Segoe UI", 10, "bold"),
        cursor="hand2",
    )
    button.bind("<Enter>", lambda event: button.config(bg="#6d28d9"))
    button.bind("<Leave>", lambda event: button.config(bg="#7c3aed"))
    return button


def _create_dark_entry(parent, width=56):
    entry = tk.Entry(
        parent,
        width=width,
        bg="#0f172a",
        fg="#ffffff",
        insertbackground="#ffffff",
        relief="flat",
        font=("Segoe UI", 10),
        highlightthickness=1,
        highlightbackground="#334155",
        highlightcolor="#7c3aed",
        bd=0,
    )
    return entry


def _create_card(parent):
    card = tk.Frame(
        parent,
        bg="#1e293b",
        bd=0,
        relief="flat",
        highlightbackground="#334155",
        highlightthickness=1,
    )
    return card


def criar_interface():
    janela = tk.Tk()
    janela.title("PDF Copier")
    janela.resizable(True, True)
    janela.geometry("760x820")
    janela.configure(bg="#0f172a")

    container = tk.Frame(janela, bg="#0f172a")
    container.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)

    header = tk.Frame(container, bg="#0f172a")
    header.pack(fill=tk.X, pady=(0, 20))

    tk.Label(header, text="PDF Copier", bg="#0f172a", fg="#ffffff", font=("Segoe UI", 20, "bold")).pack(anchor="w")
    tk.Label(header, text="Organize e copie PDF de colaboradores com elegância.", bg="#0f172a", fg="#94a3b8", font=("Segoe UI", 10)).pack(anchor="w", pady=(6, 0))

    origin_card = _create_card(container)
    origin_card.pack(fill=tk.X, pady=(0, 20), ipady=16)
    origin_card.grid_columnconfigure(0, weight=1)

    tk.Label(origin_card, text="URL da pasta de origem", bg="#1e293b", fg="#ffffff", font=("Segoe UI", 10, "bold")).grid(row=0, column=0, sticky="w", padx=16, pady=(14, 6))
    origem_entry = _create_dark_entry(origin_card, width=58)
    origem_entry.grid(row=1, column=0, padx=(16, 10), pady=(0, 16), sticky="ew")
    _create_dark_button(origin_card, "📁 Selecionar origem", lambda: selecionar_pasta(origem_entry, "Selecione a pasta de origem")).grid(row=1, column=1, padx=(0, 16), pady=(0, 16), sticky="e")

    destination_card = _create_card(container)
    destination_card.pack(fill=tk.X, pady=(0, 20), ipady=16)
    destination_card.grid_columnconfigure(0, weight=1)

    tk.Label(destination_card, text="URL da pasta de destino", bg="#1e293b", fg="#ffffff", font=("Segoe UI", 10, "bold")).grid(row=0, column=0, sticky="w", padx=16, pady=(14, 6))
    destino_entry = _create_dark_entry(destination_card, width=58)
    destino_entry.grid(row=1, column=0, padx=(16, 10), pady=(0, 16), sticky="ew")
    _create_dark_button(destination_card, "📁 Selecionar destino", lambda: selecionar_pasta(destino_entry, "Selecione a pasta de destino")).grid(row=1, column=1, padx=(0, 16), pady=(0, 16), sticky="e")

    collaborators_card = _create_card(container)
    collaborators_card.pack(fill=tk.X, pady=(0, 20), ipady=16)
    collaborators_card.grid_columnconfigure(0, weight=1)

    tk.Label(collaborators_card, text="Nome dos colaboradores (nomes dos PDFs)", bg="#1e293b", fg="#ffffff", font=("Segoe UI", 10, "bold")).grid(row=0, column=0, sticky="w", padx=16, pady=(14, 6))
    colaborador_entry = _create_dark_entry(collaborators_card, width=46)
    colaborador_entry.grid(row=1, column=0, padx=(16, 10), pady=(0, 16), sticky="ew")
    _create_dark_button(collaborators_card, "➕ Adicionar colaborador", lambda: adicionar_colaborador(colaborador_entry, colaboradores_listbox, colaboradores)).grid(row=1, column=1, padx=(0, 16), pady=(0, 16), sticky="e")

    colaboradores = []
    colaboradores_listbox = tk.Listbox(
        collaborators_card,
        width=79,
        height=8,
        bg="#0f172a",
        fg="#ffffff",
        bd=0,
        highlightthickness=1,
        highlightbackground="#334155",
        selectbackground="#4c1d95",
        selectforeground="#ffffff",
        font=("Segoe UI", 10),
    )
    colaboradores_listbox.grid(row=2, column=0, columnspan=2, padx=16, pady=(0, 16), sticky="nsew")
    collaborators_card.grid_rowconfigure(2, weight=1)

    action_frame = tk.Frame(container, bg="#0f172a")
    action_frame.pack(fill=tk.X, pady=(0, 20))
    action_button = _create_dark_button(action_frame, "Iniciar cópia", lambda: iniciar_copia(origem_entry, destino_entry, colaboradores, log_text))
    action_button.pack(fill=tk.X)

    logs_card = _create_card(container)
    logs_card.pack(fill=tk.BOTH, expand=True, pady=(0, 0), ipady=16)
    logs_card.grid_columnconfigure(0, weight=1)
    logs_card.grid_rowconfigure(1, weight=1)

    tk.Label(logs_card, text="Status / logs", bg="#1e293b", fg="#ffffff", font=("Segoe UI", 10, "bold")).grid(row=0, column=0, sticky="w", padx=16, pady=(16, 6))
    log_text = scrolledtext.ScrolledText(
        logs_card,
        width=80,
        height=8,
        state=tk.DISABLED,
        bg="#0f172a",
        fg="#e2e8f0",
        insertbackground="#ffffff",
        bd=0,
        highlightthickness=1,
        highlightbackground="#334155",
        font=("Segoe UI", 10),
    )
    log_text.grid(row=1, column=0, columnspan=2, padx=16, pady=(0, 16), sticky="nsew")

    container.grid_columnconfigure(0, weight=1)
    container.grid_rowconfigure(5, weight=1)

    janela.mainloop()


if __name__ == "__main__":
    criar_interface()
