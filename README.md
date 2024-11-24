# Análise de Qualidade de Dados 

Este repositório contém o script e os relatórios gerados como parte do desafio de análise de dados proposto pela Neoway. O objetivo principal deste desafio é avaliar e rastrear a qualidade de uma base de dados, utilizando diversas dimensões de qualidade, a fim de identificar problemas recorrentes e apresentar melhorias.

O processo de análise inclui a verificação de cinco dimensões de qualidade de dados, seguidas pela criação de um relatório de qualidade utilizando ferramentas como PowerBI ou Data Studio.

## Objetivo do Projeto

Realizar uma avaliação de qualidade de dados baseada em cinco dimensões:

1. **Preenchimento:** Cálculo da porcentagem de preenchimento de cada campo, desconsiderando valores nulos ou vazios.
2. **Padronização:** Verificação da conformidade dos dados com a formatação esperada.
3. **Consistência:** Identificação de dados contraditórios, de acordo com regras de negócios.
4. **Unicidade:** Detecção de duplicidades nos registros da base de dados.
5. **Abrangência:** Verificação da distribuição geográfica dos dados em Unidades Federativas do Brasil.

## Requisitos do Desafio

### Parte 1 - Avaliação de Qualidade de Dados

- **Desenvolvimento de Script:** O script foi desenvolvido utilizando **SQL** e **Python** para analisar e transformar os dados da base fornecida, gerando as métricas de qualidade para cada uma das cinco dimensões mencionadas.
  
- **Criação de Relatório de Qualidade:** Um relatório foi gerado utilizando **PowerBI** ou **Data Studio**, apresentando visualmente as métricas de qualidade para cada dimensão e destacando áreas que precisam de melhoria.

### Dimensões de Qualidade de Dados

1. **Preenchimento:** 
   - Cálculo da porcentagem de preenchimento dos campos da base.
  
2. **Padronização:**
   - Verificação da conformidade dos campos como `NomeAutor`, `NomeRéu`, `Advogado Autor`, `Advogado Réu`, `Tipo de Ação`, `Motivo da Ação`, `Resultado do Processo` e `Status`, com as regras de formatação predefinidas.

3. **Consistência:**
   - Verificação de inconsistências de dados, como valores de data inválidos ou campos com registros que não seguem as regras de negócio (por exemplo, `Data da Sentença` deve ser maior que `Data Ajuizamento`).

4. **Unicidade:**
   - Identificação de registros duplicados nos campos `ID Processo` e `Número do Processo`, que devem ser únicos na base de dados.

5. **Abrangência:**
   - Análise da distribuição dos registros conforme as varas cíveis, representando a porcentagem de registros por vara.

## Regras de Negócio e Formatação

- **ID Processo:** Não pode haver duplicidades e não deve ser alterado.
- **Número do Processo:** Não pode haver duplicidades e não deve ser alterado.
- **Campos de Nome (Autor, Réu, Advogado):** Devem ser formatados em letras maiúsculas, sem números, caracteres especiais ou acentuação.
- **Data de Ajuizamento e Sentença:** Devem seguir o formato `AAAA-MM-DD` e a `Data da Sentença` deve ser posterior à `Data Ajuizamento`.
- **Valores Numéricos:** Os campos `Valor da Causa` e `Valor da Sentença` devem conter apenas números, com duas casas decimais.
- **Tipo de Ação e Motivo da Ação:** Devem ser formatados em letras maiúsculas, com as categorias pré-definidas e sem caracteres especiais ou números.
- **Resultado do Processo e Status:** Devem ser formatados conforme as categorias definidas, em letras maiúsculas e sem caracteres especiais.
- **Vara:** Deve ser formatado em letras maiúsculas, sem acentuação e com as categorias específicas.

## Tecnologias Utilizadas

- **SQL:** Para manipulação e análise de dados na base.
- **Python:** Para análise, transformação de dados e cálculos de métricas de qualidade.
- **PowerBI:** Para criação de visualizações e relatórios interativos.

