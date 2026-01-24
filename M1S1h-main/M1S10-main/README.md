# 📦 Projeto ETL – Estoque e Saídas Logísticas

## 🧩 Visão Geral
O **Projeto ETL – Estoque e Saídas Logísticas** tem como objetivo analisar a movimentação de estoque (entradas e saídas) em Centros de Distribuição (CDs), permitindo identificar padrões de consumo, produtos com maior demanda, centros mais movimentados e a relação entre capacidade de armazenagem e estoque utilizado.

Este projeto foi desenvolvido com foco acadêmico e também como **portfólio prático**, demonstrando a aplicação de conceitos de **ETL, SQL, Python, Data Warehouse e Análise de Dados**.

---

## 🎯 Problema que o projeto resolve
Em operações logísticas, é comum haver dificuldades para responder perguntas como:

- Qual Centro de Distribuição tem maior movimentação?
- Quais produtos possuem maior saída?
- Existe estoque parado?
- Algum CD está operando acima ou abaixo da sua capacidade?
- Como comparar entradas e saídas por produto e por centro?

Este sistema resolve essas questões ao **consolidar, tratar e analisar dados de estoque**, gerando consultas analíticas e visualizações gráficas.

---

## 🏗️ Arquitetura da Solução
O projeto segue uma arquitetura **ETL + Data Warehouse**:

1. **Extração**  
   Leitura de dados de movimentação de estoque (entradas e saídas).

2. **Transformação**  
   - Cálculo de movimentação líquida
   - Cálculo de saldo final por produto e por CD
   - Normalização de dados

3. **Carga (Load)**  
   - Dimensão de Centros de Distribuição
   - Fato de Movimentação de Estoque

4. **Análise**  
   - Consultas SQL analíticas
   - Exportação para CSV/XLSX
   - Visualização em Jupyter Notebook

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Pandas & NumPy** – Tratamento e análise de dados
- **PostgreSQL** – Banco de dados relacional
- **SQL (DDL e DML)** – Criação e validação do Data Warehouse
- **Matplotlib & Seaborn** – Visualização de dados
- **Jupyter Notebook** – Análises gráficas
- **Git & GitHub** – Controle de versão

---

## 📂 Estrutura do Projeto

```
M1S10-main/
│
├── main.py                 # Orquestrador do projeto
├── src/
│   ├── database.py         # Conexão com o banco
│   ├── analysis.py         # Consultas analíticas com Pandas
│   └── etl/
│       ├── pipeline.py     # Pipeline ETL
│       ├── extract.py
│       ├── transform.py
│       └── load.py
│
├── sql/
│   ├── create_tables.sql   # Criação das tabelas
│   ├── clean_tables.sql    # Limpeza das tabelas
│   └── validation_queries.sql
│
├── notebooks/
│   ├── graficos.ipynb      # Visualizações e análises
│
├── data/
│   ├── consulta.csv        # Dados exportados
│   └── consulta.xlsx
│
└── README.md
```

---

## ▶️ Como Executar o Projeto

### 🔹 Pré-requisitos
- Python 3 instalado
- PostgreSQL instalado e em execução
- Ambiente virtual configurado

### 🔹 Passos para execução

1. Clone o repositório:
```bash
git clone https://github.com/Konradmusialowski/projeto_etl_logistica_estoque.git
```

2. Acesse o diretório do projeto:
```bash
cd M1S10-main
```

3. Ative o ambiente virtual:
```bash
venv\Scripts\activate
```

4. Execute o pipeline completo:
```bash
python main.py
```

5. Para visualizar gráficos:
```bash
jupyter notebook
```
Abra o arquivo `notebooks/graficos.ipynb`.
rode direto da pasta no botao executar cell
---

## 📊 Exemplos de Análises Geradas

- Ranking de CDs com maior saída
- Produtos com maior movimentação
- Média mensal de movimentação por centro
- Comparação entre capacidade de armazenagem e estoque final
- Identificação de CDs com espaço disponível ou sobrecarregados

---

## 🔍 Validação e Integridade dos Dados
O projeto executa consultas SQL para:

- Verificar volume de registros carregados
- Identificar chaves primárias nulas
- Detectar movimentações sem centro correspondente

Garantindo **qualidade e consistência dos dados**.

---

## 🚀 Melhorias Futuras

- Inclusão de dimensão de tempo
- Dashboards 
- executar o graficos.ipynb junto com o main.py
- Alertas automáticos de estoque crítico
- Análise de estoque parado
- Previsão de demanda com Machine Learning

---


**Konrad Musialowski**  
Estudante de Sistemas de Informação  
Projeto desenvolvido para fins acadêmicos

---


