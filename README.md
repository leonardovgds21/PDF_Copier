# 📄 PDF Copier

Automatize a cópia de arquivos PDF de forma rápida, simples e eficiente.

## 🚀 Sobre o projeto

O **PDF Copier** é uma Aplicação desktop desenvolvida em Python para automatizar a movimentação de arquivos PDF entre diretórios com base no nome dos colaboradores.

O projeto nasceu para eliminar uma atividade manual recorrente realizada mensalmente, reduzindo tempo gasto na execução da tarefa, minimizando erros operacionais e aumentando a produtividade do processo.

---

## 🎯 Objetivo

O principal objetivo do projeto é:

- ✅ Reduzir o tempo gasto na cópia manual de centenas de arquivos PDF  
- ✅ Minimizar erros humanos  
- ✅ Facilitar o uso por usuários não técnicos  
- ✅ Padronizar o processo de organização de arquivos  

---

## ⚙️ Funcionalidades

- Seleção de pasta de origem e destino via interface
- Filtro de arquivos PDF por nome de colaborador
- Cópia automática (sem remover arquivos da origem)
- Interface gráfica simples e intuitiva
- Exibição de logs em tempo real

---

## 🧠 Como funciona

O sistema:

1. Percorre todos os arquivos da pasta de origem  
2. Identifica arquivos PDF  
3. Verifica se o nome do colaborador está presente no nome do arquivo  
4. Copia os arquivos correspondentes para a pasta de destino  

---

## 🖥️ Interface

O programa conta com uma interface gráfica moderna que permite:

- Selecionar diretórios com poucos cliques  
- Inserir nomes de colaboradores facilmente  
- Visualizar o status da execução em tempo real  

---

## 🛠️ Tecnologias utilizadas

- Python 3
- Tkinter (interface gráfica)
- Microsoft Copilot

---

## 🤖 Desenvolvimento com IA

Este projeto foi desenvolvido com apoio de Inteligência Artificial, utilizando o conceito de **Vibe Coding**, onde a IA auxilia no processo de desenvolvimento, design e melhoria contínua do sistema.

---

## Imagem do programa
<img width="762" height="852" alt="print" src="https://github.com/user-attachments/assets/5fb82488-88be-4a40-8885-2403f4e8b800" />

## 📦 Como usar

1. Execute o programa:

```bash
python main.py
```

---

## 🏗️ Como gerar o executável (.exe)

O executável não fica no repositório (a pasta `dist/` está no `.gitignore`), então é preciso gerá-lo em cada máquina ou copiá-lo de uma máquina onde já foi gerado.

1. Instale o PyInstaller (apenas na primeira vez):

```bash
python -m pip install pyinstaller
```

2. Na pasta do projeto, gere o executável (arquivo único, sem janela de console):

```bash
python -m PyInstaller --noconfirm --onefile --windowed --name "PDF Copier" main.py
```

3. O executável fica em `dist\PDF Copier.exe`. Ele funciona sem Python instalado e pode ser copiado para qualquer pasta.

Sempre que o código for alterado, gere o executável novamente para que ele inclua as mudanças.
