from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="edip_pipeline",
    start_date=datetime(
        2026,
        1,
        1
    ),
    schedule="@daily",
    catchup=False
) as dag:

    generate = BashOperator(
        task_id="generate_data",
        bash_command=(
            "cd /opt/edip && "
            "python generate_data.py"
        )
    )

    etl = BashOperator(
        task_id="run_etl",
        bash_command=(
            "cd /opt/edip && "
            "python run_etl.py"
        )
    )

    generate >> etl
