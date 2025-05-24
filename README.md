# Análise de Churn - Telecom Índia 🚀

## 📋 Descrição
Projeto de análise preditiva para identificar clientes com propensão a cancelar serviços de telecomunicações na Índia.

## 🗂️ Estrutura do Projeto

```
india-churn-analysis/
│
├── data/                      
│   ├── raw/                  # Dados originais
│   │   └── customer_data.csv 
│   └── output/               # Dados processados
│       ├── prod_customer_data_churn.csv
│       ├── prod_customer_data_new_customers.csv
│       └── predictions.csv
│
├── notebooks/                # Análises e modelos
│   ├── 01_model_training.ipynb    
│   └── 02_new_data_predict.ipynb  
│
├── models/                   # Modelos salvos
│   ├── logistic_regression_model.pkl
│   ├── random_forest_model.pkl
│   ├── xgboost_model.pkl
│   └── lightgbm_model.pkl
│
├── sql/                      # Scripts SQL
│   └── create_tables.sql
│
├── docker-compose.yml        # Configuração Docker
├── requirements.txt          # Dependências Python
├── README.md                # Documentação
└── .env                     # Variáveis de ambiente
```

### 🔧 Pré-requisitos

- Python 3.8+
- Docker Desktop
- Git
- VS Code (recomendado)

### ⚙️ Configuração do Ambiente

#### 1. Clone o repositório

```
git clone https://github.com/seu-usuario/india-churn-analysis.git
cd india-churn-analysis
```

#### 2. Ambiente Virtual Python

Crie um arquivo `.env` na raiz:

```
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente (Windows)
.\venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

#### 3. Configurar Docker

Crie um arquivo `.env` na raiz:


```
SA_PASSWORD=SuaSenhaForte123
ACCEPT_EULA=Y
MSSQL_PID=Developer
```

Inicie o container:

```
docker-compose up -d
```

### 📊 Executando o Projeto

#### 1. Preparação dos Dados

- Coloque seus dados em `customer_data.csv`


#### 2. Treinamento do Modelo

Execute o notebook `01_model_training.ipynb`:

- Pré-processamento dos dados
- Treinamento de múltiplos modelos
- Avaliação de performance
- Salvamento do melhor modelo

#### 3. Fazendo Predições

Execute o notebook `02_new_data_predict.ipynb`:

- Carregamento do modelo treinado
- Predições em novos dados
- Análise dos resultados
- Geração do arquivo de predições

#### 4. Visualização do Dashboard

- Summary

![Summary](/public/Dashboard/summary.png)

- Predictions

![Predictions](/public/Dashboard/predictions.png)

### 📦 Dependências Principais

```
pandas==1.5.3
numpy==1.24.3
scikit-learn==1.2.2
xgboost==1.7.5
lightgbm==3.3.5
matplotlib==3.7.1
seaborn==0.12.2
jupyter==1.0.0
```

### 🗄️ Banco de Dados

- Conexão SQL Server

```
Host: localhost
Port: 1433
User: sa
Password: [definida no .env]
```

- Verificar Status

```
docker ps
docker logs sqlserver_container
```

### 🔍 Monitoramento

- Logs do Container

```
docker logs -f sqlserver_container
```

- Acessar o Container

```
docker exec -it sqlserver_container bash
```

### 🚨 Solução de Problemas

- Erro no Docker

```
# Reiniciar container
docker-compose down
docker-compose up -d

# Verificar logs
docker logs sqlserver_container
```

- Erro nos Notebooks
    1. Verifique se o ambiente virtual está ativo
    2. Confirme as dependências:

    ```
    pip list
    ```

    3. Reinicie o kernel do Jupyter

### 📄 Licença

Este projeto está sob a licença MIT.

### 📧 Contato

- LinkedIn: [Pedro Sancho Rodrigues](https://www.linkedin.com/in/pedrosanchorodrigues/)

- GitHub: @sanchopedro

- Site: [sancho dev](https://sanchodev.vercel.app/)