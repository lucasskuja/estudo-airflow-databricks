# Estudo Airflow + Databricks

Este repositório é um portfólio para demonstrar a integração entre Apache Airflow e Databricks. O foco está em orquestração de jobs Databricks, monitoramento de execuções e boas práticas de pipeline.

## Objetivo do projeto
- Mostrar DAGs que orquestram jobs Databricks.
- Demonstrar monitoramento de execução via Airflow.
- Apresentar exemplos de execução de jobs e uso de `DatabricksSubmitRunOperator` / `DatabricksRunNowOperator`.

## Estrutura do repositório
- `dags/` - DAGs de exemplo com orquestração Databricks.
- `docs/` - Documentação de configuração e conexão.
- `requirements.txt` - Dependências do projeto.
- `.gitignore` - Configurações para ignorar arquivos locais.

## DAGs disponíveis
- `dags/databricks_bronze_silver_gold_dag.py` - Orquestra três tarefas que representam uma arquitetura Bronze/Silver/Gold no Databricks.
- `dags/databricks_runnow_monitoring_dag.py` - Aciona jobs existentes no Databricks e demonstra monitoramento de execução a partir do Airflow.

## Requisitos
- Python 3.10
- Virtualenv
- Apache Airflow 2.6.1
- `apache-airflow-providers-databricks`

## Instalação
1. Crie e ative o ambiente virtual:
    ```bash
    python3.10 -m venv .venv
    source .venv/bin/activate
    ```
2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Configuração do Airflow
1. Configure o Airflow para usar o diretório local:
    ```bash
    export AIRFLOW_HOME=$(pwd)/airflow
    ```
2. Inicialize o banco de dados do Airflow:
    ```bash
    airflow db init
    ```
3. Crie a conexão Databricks conforme descrito em `docs/databricks_connection.md`.
4. Garanta que o `dags_folder` aponte para `./dags` ou copie os arquivos de DAG para o diretório de DAGs do Airflow.

## Execução
1. Inicie o Airflow:
    ```bash
    airflow standalone
    ```
2. Acesse o Airflow Web UI em `http://localhost:8080`.
3. Ative os DAGs e execute as tarefas manualmente ou agende-as.

## Ajustes necessários antes da execução
- Substitua `notebook_path` nos DAGs pelos caminhos corretos do seu workspace Databricks.
- Substitua `job_id` no DAG `databricks_runnow_monitoring_dag.py` pelos IDs de job reais.
- Configure a conexão `databricks_default` com host e token.

## Referências
- Curso Alura: [construindo pipelines de dados com Airflow e Azure Databricks](https://cursos.alura.com.br/course/databricks-pipelines-dados-airflow-azure-databricks)
- https://airflow.apache.org/docs/apache-airflow/stable/start
- https://docs.databricks.com/dev-tools/airflow/index.html
