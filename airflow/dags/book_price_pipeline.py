"""Manual Airflow workflow for the local Book Price Tracker pipeline."""

from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator


pipeline_environment = {
    # Docker Desktop routes this hostname from the worker to the host machine.
    "DB_HOST": "host.docker.internal",
    "DB_PORT": "5433",
}


with DAG(
    dag_id="book_price_pipeline",
    description="Scrape books, load PostgreSQL, build dbt models, and run dbt tests.",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["portfolio", "books", "data-engineering"],
) as dag:
    scrape_books = BashOperator(
        task_id="scrape_books",
        bash_command="""
        set -e
        cd /opt/project
        scrapy crawl books -O data/raw/books.csv
        """,
        env=pipeline_environment,
        append_env=True,
    )

    load_books = BashOperator(
        task_id="load_books",
        bash_command="""
        set -e
        cd /opt/project
        python load_books.py
        """,
        env=pipeline_environment,
        append_env=True,
    )

    build_dbt_models = BashOperator(
        task_id="build_dbt_models",
        bash_command="""
        set -e
        export DB_PASSWORD="$(grep '^DB_PASSWORD=' /opt/project/.env | cut -d= -f2- | tr -d '\\r')"
        dbt run --project-dir /opt/project/price_tracker_dbt \\
          --profiles-dir /opt/project/airflow/dbt --target docker
        """,
    )

    test_dbt_models = BashOperator(
        task_id="test_dbt_models",
        bash_command="""
        set -e
        export DB_PASSWORD="$(grep '^DB_PASSWORD=' /opt/project/.env | cut -d= -f2- | tr -d '\\r')"
        dbt test --project-dir /opt/project/price_tracker_dbt \\
          --profiles-dir /opt/project/airflow/dbt --target docker
        """,
    )

    scrape_books >> load_books >> build_dbt_models >> test_dbt_models
