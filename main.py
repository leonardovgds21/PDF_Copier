import os
from utils import copiar_pdfs


def solicitar_colaboradores():
    colaboradores = []

    while True:
        nome = input("Digite o nome do colaborador: ").strip()
        if not nome:
            print("Nome não pode ficar vazio. Tente novamente.")
            continue

        colaboradores.append(nome)

        while True:
            resposta = input("Deseja digitar outro nome? [s/n]: ").strip().lower()
            if resposta in ("s", "sim"):
                break
            if resposta in ("n", "nao", "não"):
                return colaboradores
            print("Por favor, responda com 's' ou 'n'.")


def solicitar_caminho(prompt_text, deve_existir=False):
    while True:
        caminho = input(prompt_text).strip()
        if not caminho:
            print("O caminho não pode ficar vazio. Tente novamente.")
            continue

        if deve_existir and not os.path.isdir(caminho):
            print("O caminho informado não existe ou não é uma pasta. Tente novamente.")
            continue

        return caminho


def main():
    print("🚀 Iniciando cópia de PDFs...\n")

    pasta_origem = solicitar_caminho("Digite o caminho da pasta de origem: ", deve_existir=True)
    pasta_destino = solicitar_caminho("Digite o caminho da pasta de destino: ")

    colaboradores = solicitar_colaboradores()
    copiar_pdfs(pasta_origem, pasta_destino, colaboradores)

    print("\n✅ Processo finalizado!")


if __name__ == "__main__":
    main()