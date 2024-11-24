import pandas as pd
import re
import numpy as np
from decimal import Decimal, InvalidOperation

# Função para validar e padronizar os nomes
def padronizar_nome(nome):
    if pd.isna(nome):
        return nome
    nome = nome.strip()
    nome = re.sub(r'[^A-Za-z\s]', '', nome)  # Remove caracteres não alfabéticos
    nome = nome.upper()  # Coloca em letras maiúsculas
    return nome

# Função para validar se a data de ajuizamento é menor que a data de sentença
def validar_datas(row):
    if pd.to_datetime(row['Data Ajuizamento'], errors='coerce') > pd.to_datetime(row['Data da Sentença'], errors='coerce'):
        return False
    return True

# Função para verificar se os valores são numéricos e corrigir para 2 casas decimais
def validar_valores(value):
    try:
        if pd.isna(value) or value == '':
            return Decimal('0.00')  # Retorna 0.00 caso o valor seja vazio ou inválido
        value = Decimal(value).quantize(Decimal('0.00'))  # Converte para Decimal com duas casas
        return value
    except InvalidOperation:
        return Decimal('0.00')  # Retorna 0.00 se o valor não for numérico

# Função para padronizar tipo de ação
def padronizar_tipo_acao(tipo_acao):
    tipo_acao = str(tipo_acao).strip().upper()
    tipos_validos = ['AÇÃO PENAL', 'AÇÃO CÍVEL', 'AÇÃO TRABALHISTA']
    return tipo_acao if tipo_acao in tipos_validos else np.nan

# Função para padronizar motivo da ação
def padronizar_motivo_acao(motivo_acao):
    motivo_acao = str(motivo_acao).strip().upper()
    motivos_validos = ['DIVÓRCIO', 'INDENIZAÇÃO', 'DÍVIDA']
    return motivo_acao if motivo_acao in motivos_validos else np.nan

# Função para padronizar resultado do processo
def padronizar_resultado(resultado):
    resultado = str(resultado).strip().upper()
    resultados_validos = ['ARQUIVADO', 'INDEFINIDO', 'IMPROCEDENTE', 'PROCEDENTE']
    return resultado if resultado in resultados_validos else np.nan

# Função para padronizar status
def padronizar_status(status):
    status = str(status).strip().upper()
    status_validos = ['JULGADO', 'EM ANDAMENTO']
    return status if status in status_validos else np.nan

# Função para padronizar vara
def padronizar_vara(vara):
    vara = str(vara).strip().upper()
    varas_validas = ['1ª VARA CÍVEL', '2ª VARA CÍVEL', '3ª VARA CRIMINAL', '4ª VARA CÍVEL', '5ª VARA CÍVEL']
    return vara if vara in varas_validas else np.nan

