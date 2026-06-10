import os
import shutil
import unicodedata


def _normalizar_texto(texto):
    texto = unicodedata.normalize("NFKD", texto.casefold())
    texto = "".join(ch for ch in texto if not unicodedata.combining(ch))
    return " ".join(texto.split())


def _is_subpath(child_path, parent_path):
    child_path = os.path.abspath(child_path)
    parent_path = os.path.abspath(parent_path)
    try:
        return os.path.commonpath([child_path, parent_path]) == parent_path
    except ValueError:
        return False


def copiar_pdfs(pasta_origem, pasta_destino, colaboradores):
    pasta_origem = os.path.abspath(pasta_origem)
    pasta_destino = os.path.abspath(pasta_destino)

    if _is_subpath(pasta_destino, pasta_origem):
        raise ValueError("A pasta de destino não pode estar dentro da pasta de origem.")

    os.makedirs(pasta_destino, exist_ok=True)

    colaboradores_normalizados = [_normalizar_texto(nome) for nome in colaboradores]
    copiados = []

    for raiz, _, arquivos in os.walk(pasta_origem):
        for arquivo in arquivos:
            if not arquivo.lower().endswith(".pdf"):
                continue

            arquivo_normalizado = _normalizar_texto(arquivo)

            for nome_normalizado in colaboradores_normalizados:
                if nome_normalizado in arquivo_normalizado:
                    caminho_origem = os.path.join(raiz, arquivo)
                    caminho_destino = os.path.join(pasta_destino, arquivo)
                    shutil.copy2(caminho_origem, caminho_destino)
                    copiados.append(caminho_destino)
                    break

    return copiados
