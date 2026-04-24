from datetime import timedelta

from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator
from airflow.utils.dates import days_ago

# Exemplo de DAG que orquestra três passos Databricks: Bronze, Silver e Gold.
# Ajuste os parâmetros de cluster e notebook_path conforme seu workspace.

default_args = {
    'owner': 'portfolio',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

new_cluster = {
    'spark_version': '13.0.x-scala2.12',
    'node_type_id': 'Standard_D3_v2',
    'num_workers': 2,
}

with DAG(
    dag_id='databricks_bronze_silver_gold',
    default_args=default_args,
    description='Orquestra três etapas de processamento Databricks em uma arquitetura medalhão',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
    tags=['databricks', 'portfolio', 'etl'],
) as dag:

    bronze_task = DatabricksSubmitRunOperator(
        task_id='bronze_layer_job',
        databricks_conn_id='databricks_default',
        json={
            'new_cluster': new_cluster,
            'notebook_task': {
                'notebook_path': '/Repos/portfolio/bronze_etl',
            },
        },
    )

    silver_task = DatabricksSubmitRunOperator(
        task_id='silver_layer_job',
        databricks_conn_id='databricks_default',
        json={
            'new_cluster': new_cluster,
            'notebook_task': {
                'notebook_path': '/Repos/portfolio/silver_etl',
            },
        },
    )

    gold_task = DatabricksSubmitRunOperator(
        task_id='gold_layer_job',
        databricks_conn_id='databricks_default',
        json={
            'new_cluster': new_cluster,
            'notebook_task': {
                'notebook_path': '/Repos/portfolio/gold_etl',
            },
        },
    )

    bronze_task >> silver_task >> gold_task
