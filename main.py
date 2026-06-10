from config import PASTA_ORIGEM, PASTA_DESTINO
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


def main():
    print("🚀 Iniciando cópia de PDFs...\n")

    colaboradores = solicitar_colaboradores()
    copiar_pdfs(PASTA_ORIGEM, PASTA_DESTINO, colaboradores)

    print("\n✅ Processo finalizado!")


if __name__ == "__main__":
    main()