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
    pasta_origem = origem_entry.get().strip()
    pasta_destino = destino_entry.get().strip()

    if not pasta_origem:
        messagebox.showerror("Erro", "Informe a pasta de origem.")
        return
    if not os.path.isdir(pasta_origem):
        messagebox.showerror("Erro", "A pasta de origem não existe.")
        return

    if not pasta_destino:
        messagebox.showerror("Erro", "Informe a pasta de destino.")
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


def criar_interface():
    janela = tk.Tk()
    janela.title("PDF Copier")
    janela.resizable(False, False)
    janela.geometry("620x540")

    frame = tk.Frame(janela, padx=12, pady=12)
    frame.pack(fill=tk.BOTH, expand=True)

    tk.Label(frame, text="URL da pasta de origem:").grid(row=0, column=0, sticky="w")
    origem_entry = tk.Entry(frame, width=56)
    origem_entry.grid(row=1, column=0, padx=(0, 8), pady=(0, 8), sticky="w")
    tk.Button(frame, text="Selecionar origem", width=20, command=lambda: selecionar_pasta(origem_entry, "Selecione a pasta de origem")).grid(row=1, column=1, pady=(0, 8))

    tk.Label(frame, text="URL da pasta de destino:").grid(row=2, column=0, sticky="w")
    destino_entry = tk.Entry(frame, width=56)
    destino_entry.grid(row=3, column=0, padx=(0, 8), pady=(0, 8), sticky="w")
    tk.Button(frame, text="Selecionar destino", width=20, command=lambda: selecionar_pasta(destino_entry, "Selecione a pasta de destino")).grid(row=3, column=1, pady=(0, 8))

    tk.Label(frame, text="Nome dos colaboradores (nomes dos PDFs):").grid(row=4, column=0, sticky="w")
    colaborador_entry = tk.Entry(frame, width=40)
    colaborador_entry.grid(row=5, column=0, padx=(0, 8), pady=(0, 8), sticky="w")
    tk.Button(frame, text="Adicionar colaborador", width=20, command=lambda: adicionar_colaborador(colaborador_entry, colaboradores_listbox, colaboradores)).grid(row=5, column=1, pady=(0, 8))

    colaboradores = []
    colaboradores_listbox = tk.Listbox(frame, width=80, height=8)
    colaboradores_listbox.grid(row=6, column=0, columnspan=2, pady=(0, 8))

    tk.Button(frame, text="Iniciar cópia", width=20, command=lambda: iniciar_copia(origem_entry, destino_entry, colaboradores, log_text)).grid(row=7, column=0, columnspan=2, pady=(0, 12))

    tk.Label(frame, text="Status / logs:").grid(row=8, column=0, sticky="w")
    log_text = scrolledtext.ScrolledText(frame, width=72, height=12, state=tk.DISABLED)
    log_text.grid(row=9, column=0, columnspan=2, sticky="nsew")

    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=0)

    janela.mainloop()


if __name__ == "__main__":
    criar_interface()
