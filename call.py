from validation import padronizar_nome, validar_datas, validar_valores, padronizar_tipo_acao, padronizar_motivo_acao, padronizar_resultado, padronizar_status, padronizar_vara
import pandas as pd

# Carregar o arquivo CSV para um DataFrame
df = pd.read_csv('Base de dados - Case DQA.csv')

# 1. Preenchimento: Calcular a porcentagem de preenchimento para cada coluna
preenchimento = df.notna().mean() * 100

# 2. Padronização: Aplicar as funções de padronização
df['Nome Autor'] = df['Nome Autor'].apply(padronizar_nome)
df['Nome Réu'] = df['Nome Réu'].apply(padronizar_nome)
df['Advogado Autor'] = df['Advogado Autor'].apply(padronizar_nome)
df['Advogado Réu'] = df['Advogado Réu'].apply(padronizar_nome)
df['Tipo de Ação'] = df['Tipo de Ação'].apply(padronizar_tipo_acao)
df['Motivo da Ação'] = df['Motivo da Ação'].apply(padronizar_motivo_acao)
df['Resultado do Processo'] = df['Resultado do Processo'].apply(padronizar_resultado)
df['Status'] = df['Status'].apply(padronizar_status)
df['Vara'] = df['Vara'].apply(padronizar_vara)

# 3. Consistência: Validar se as datas de ajuizamento são antes da data de sentença
df['Data Ajuizamento'] = pd.to_datetime(df['Data Ajuizamento'], errors='coerce')
df['Data da Sentença'] = pd.to_datetime(df['Data da Sentença'], errors='coerce')
df['Data Consistente'] = df.apply(validar_datas, axis=1)

# 4. Unicidade: Verificar duplicidade nos campos 'ID Processo' e 'Número do Processo'
df['Duplicado ID Processo'] = df.duplicated(subset='ID Processo', keep=False)
df['Duplicado Número Processo'] = df.duplicated(subset='Número do Processo', keep=False)

# 5. Abrangência: Para verificar a distribuição geográfica, preciso de uma coluna da Unidade Federativa (UF). 
# Não há uma coluna de UF, então assumi que a distribuição será feita com base na Vara
abrangencia_vara = df['Vara'].value_counts(normalize=True) * 100

# 6. Valor da Causa e Valor da Sentença: Verificar se são valores numéricos e com 2 casas decimais
df['Valor da Causa'] = df['Valor da Causa'].apply(validar_valores)
df['Valor da Sentença'] = df['Valor da Sentença'].apply(validar_valores)

# 7. Salvar o DataFrame tratado em um novo arquivo CSV
df.to_csv('CaseDQA_tratada.csv', index=False)

# Exibir resultados de qualidade de dados
print(f'Preenchimento por coluna: \n{preenchimento}')
print(f'Número de registros inconsistentes com datas: {df[~df["Data Consistente"]].shape[0]}')
print(f'Número de duplicatas encontradas no ID Processo: {df[df["Duplicado ID Processo"]].shape[0]}')
print(f'Número de duplicatas encontradas no Número do Processo: {df[df["Duplicado Número Processo"]].shape[0]}')

# Exibir a distribuição de abrangência por Vara
print(f'\nDistribuição de Abrangência por Vara: \n{abrangencia_vara}')
