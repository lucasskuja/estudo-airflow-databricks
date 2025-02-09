## Requisitos:
- Python >= 3.7 <= 3.10
- Virtualenv
- Airflow 3.6.1

## Passo a passo

1. Indico criar um ambiente virtual para que os pacotes locais não se misturem com os pacotes necessários no projeto:
    ```shell
    python3.10 -m venv myenv
    source myenv/bin/activate
    ````
1. Instalação do Airflow:
    ````shell
    export AIRFLOW_HOME=./airflow

    AIRFLOW_VERSION=2.6.1

    PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"

    CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

    pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
    ````
1. instalando o provider do databricks:

    ````shell
    pip install apache-airflow-providers-databricks
    ````
1. Iniciando o Airflow:
    ````shell
    airflow standalone
    ````

## Referências:
- Curso Alura: [construindo pipelines de dados com Airflow e Azure Databricks](https://cursos.alura.com.br/course/databricks-pipelines-dados-airflow-azure-databricks)
- https://airflow.apache.org/docs/apache-airflow/stable/start.
- https://apilayer.com/marketplace/exchangerates_data-api

