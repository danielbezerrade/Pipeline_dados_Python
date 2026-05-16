# 📊 Pipeline de Dados com Python

Projeto simples de engenharia de dados utilizando Python, Pandas e Jupyter Notebook para realizar:

- 🔍 Análise exploratória de dados
- 🧹 Limpeza e tratamento
- 📁 Padronização
- ⚙️ Automação de pipeline

---

# 🚀 Tecnologias utilizadas

- 🐍 Python
- 🐼 Pandas
- 📓 Jupyter Notebook
- 🌐 Git e GitHub
- 📊 OpenPyXL

---

# 📂 Estrutura do Projeto

```text
PIPELINE_DADOS_PYTHON/

│
├── exploracao.ipynb
├── dados.py
├── executando_pipeline.py
├── criando_pastas.py
├── base_vendas_tecnologia_pipeline.xlsx
│
├── pipeline/
│   └── dados_tratados_pipeline.xlsx
│
├── dados_tratados_analise_exploratoria/
│   └── dados_tratados_exploração.xlsx
│
├── pipeline.log
├── .gitignore
└── README.md
🎯 Objetivo do Projeto

O objetivo deste projeto é simular um pequeno pipeline de engenharia de dados utilizando Python.

O pipeline realiza:

📥 Leitura de arquivos Excel
🔎 Análise exploratória
⚠️ Identificação de valores nulos
♻️ Remoção de duplicidades
🛠️ Tratamento e padronização de dados
📤 Exportação dos dados tratados
⚙️ Etapas do Pipeline
1️⃣ Análise Exploratória

Nesta etapa foram analisados:

📌 Tipos de dados
📌 Valores nulos
📌 Duplicidades
📌 Estrutura do dataset

Utilizando funções como:

df.info()
df.describe()
df.isnull().sum()
df.duplicated().sum()
2️⃣ Tratamento de Dados

Foram realizados tratamentos como:

🧹 Remoção de duplicatas
🔧 Preenchimento de valores nulos
📝 Padronização de colunas
📊 Organização dos dados
3️⃣ Pipeline Automatizada

O projeto utiliza funções e classes para automatizar o fluxo de tratamento dos dados.

Exemplo:

if __name__ == '__main__':
    execute_pipeline()

