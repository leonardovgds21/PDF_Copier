import os
import shutil


def copiar_pdfs(pasta_origem, pasta_destino, colaboradores):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    arquivos = os.listdir(pasta_origem)

    for arquivo in arquivos:

        # verifica se é PDF
        if arquivo.lower().endswith(".pdf"):
            
            # verifica se contém algum nome na lista
            for nome in colaboradores:

                if nome.lower() in arquivo.lower():
                    
                    caminho_origem = os.path.join(pasta_origem, arquivo)
                    caminho_destino = os.path.join(pasta_destino, arquivo)

                    shutil.copy2(caminho_origem, caminho_destino)

                    print(f"✅ Copiado: {arquivo}")
                    
                    break  # evita copiar duplicado