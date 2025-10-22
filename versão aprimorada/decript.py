#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet


def listar_arquivos(excluir_excecoes=["lockware.py", "chave.key"]):
    # Lista todos os arquivos no diretório atual, excluindo exceções
    arquivos = [file for file in os.listdir() if os.path.isfile(file) and file not in excluir_excecoes]
    return arquivos

def carregar__chaves(nome_arquivo="chave.key"):

    with open(nome_arquivo, "rb") as arquivo_chave:
        chave = arquivo_chave.read()
    return chave

def descriptografar_arquivos(chave, excluir_excecoes=["lockware.py", "chave.key"]):
        fernet = Fernet(chave)
        arquivos = listar_arquivos(excluir_excecoes)

        for file in arquivos:
                with open(file, "rb") as arquivo:
                        conteudo = arquivo.read()
                conteudo_descriptografado = fernet.decrypt(conteudo)

                with open(file, "wb") as arquivo:
                        arquivo.write(conteudo_criptografado)
                print(f"Arquivo {file} descriptografado.")
           except Exception as e:
                print(f"Erro ao descriptografar o arquivo {file}: {e}")

chave = carregar_chaves()
descriptografar_arquivos(chave)
