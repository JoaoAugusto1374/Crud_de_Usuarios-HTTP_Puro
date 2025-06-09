import os
from urllib.parse import parse_qs

CAMINHO_ARQUIVO = "usuarios.txt"

def carregar_usuarios():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return []
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
        linhas = f.readlines()
    usuarios = []
    for linha in linhas:
        if linha.strip():
            partes = linha.strip().split("|")
            usuarios.append({
                "id": int(partes[0]),
                "nome": partes[1],
                "email": partes[2],
                "telefone": partes[3],
            })
    return usuarios

def salvar_usuarios(usuarios):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
        for u in usuarios:
            linha = f"{u['id']}|{u['nome']}|{u['email']}|{u['telefone']}\n"
            f.write(linha)
