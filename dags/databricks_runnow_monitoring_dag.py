from datetime import timedelta

from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from airflow.utils.dates import days_ago

# Exemplo de DAG que aciona jobs Databricks existentes e demonstra monitoramento
# de execução a partir do Airflow.

default_args = {
    'owner': 'portfolio',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=10),
}

with DAG(
    dag_id='databricks_runnow_monitoring',
    default_args=default_args,
    description='Dispara jobs Databricks existentes e monitora a execução no Airflow',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
    tags=['databricks', 'monitoring', 'portfolio'],
) as dag:

    run_databricks_job_1 = DatabricksRunNowOperator(
        task_id='run_databricks_job_1',
        databricks_conn_id='databricks_default',
        json={
            'job_id': 12345,  # Substitua pelo job_id do seu Databricks
            'notebook_params': {
                'env': 'dev',
                'step': 'bronze',
            },
        },
    )

    run_databricks_job_2 = DatabricksRunNowOperator(
        task_id='run_databricks_job_2',
        databricks_conn_id='databricks_default',
        json={
            'job_id': 67890,  # Substitua pelo job_id do seu Databricks
            'notebook_params': {
                'env': 'dev',
                'step': 'silver',
            },
        },
    )

    run_databricks_job_1 >> run_databricks_job_2
