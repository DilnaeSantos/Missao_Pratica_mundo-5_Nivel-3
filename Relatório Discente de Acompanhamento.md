# 📝 Relatório Discente de Acompanhamento

## Informações do Curso

- **Projeto:** Manipulação e Tratamento de Dados com Pandas
- **Curso:** Full Stack
- **Universidade:** Estácio de Sá - Campus São José dos Pinhais
- **Período:** 5º Período
- **Turma:** 9001
- **Tecnologia:** Python e Pandas
- **Tutor:** Altamira Queiroz
- **Matéria:** Tratando a Imensidao Dos Dados (RPG0033)

## Informações do Aluno

- **Nome:** Dilnae Rennan Souza dos Santos
- **Matrícula:** 202302631631

## Descrição do Projeto

O projeto teve como objetivo a prática de manipulação e tratamento de dados utilizando a biblioteca **Pandas** em Python. Através de microatividades práticas, foram abordadas tarefas fundamentais como criação de subconjuntos de dados, configuração de exibição, visualização de trechos do conjunto e, por fim, o tratamento completo de um dataset com dados inconsistentes e valores ausentes.

---

## 📌 Microatividade 1

**Objetivo:** Ler um arquivo CSV com Pandas e exibir seu conteúdo.

- Foi utilizado o método `pd.read_csv()` para ler o arquivo.
- Os dados foram atribuídos a uma variável chamada `dados`.
- Foi utilizada a função `print(dados)` para exibir seu conteúdo.

---

## 📌 Microatividade 2

**Objetivo:** Criar um subconjunto de dados com apenas 3 colunas.

- Criada uma nova variável `subconjunto` contendo as colunas `['Date', 'Pulse', 'Calories']`.
- O subconjunto foi exibido com `print(subconjunto)`.

---

## 📌 Microatividade 3

**Objetivo:** Configurar a exibição de até 9999 linhas no Pandas.

- Configurado com `pd.set_option('display.max_rows', 9999)`.
- Os dados foram exibidos com `print(dados.to_string())`.

---

## 📌 Microatividade 4

**Objetivo:** Exibir as 10 primeiras e 10 últimas linhas do dataset.

- Utilizado `dados.head(10)` para as primeiras 10.
- Utilizado `dados.tail(10)` para as últimas 10.

---

## 📌 Microatividade 5

**Objetivo:** Obter informações gerais sobre o dataset.

- Utilizado o método `dados.info()`.
- Foi possível observar:
  - Quantidade de linhas e colunas.
  - Tipo de dados em cada coluna.
  - Dados nulos.
  - Uso de memória do DataFrame.

---

## 🧹 Missão Prática: Tratamento Completo de Dados

**Objetivo:** Corrigir e padronizar dados em um DataFrame para uso analítico.

### Passos Realizados:

1. Leitura do CSV original com separador `;`.
2. Exibição de informações e pré-visualização com `.info()`, `.head()` e `.tail()`.
3. Cópia do DataFrame original.
4. Substituição de valores nulos na coluna `Calories` por `0`.
5. Substituição de valores nulos em `Date` por `'1900/01/01'`.
6. Conversão da coluna `Date` para o tipo `datetime`, com tratamento de erros.
7. Correção manual da string `'20201226'` e conversão completa com `pd.to_datetime()`.
8. Exclusão da linha com valor nulo restante usando `.dropna()`.

### Resultado:

O DataFrame foi tratado com sucesso, tornando-se adequado para análises futuras. As inconsistências e valores ausentes foram resolvidos de forma programática com os recursos oferecidos pelo Pandas.

---

## Conclusão

As microatividades e a missão prática possibilitaram o domínio de técnicas essenciais de manipulação e tratamento de dados com a biblioteca Pandas. O projeto demonstra a capacidade de trabalhar com dados reais, identificar inconsistências e preparar datasets para visualizações e análises mais avançadas.
