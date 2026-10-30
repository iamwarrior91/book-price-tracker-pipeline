FROM apache/airflow:3.3.2

COPY requirements.txt /requirements.txt

# Reinstall the matching Airflow version while adding the pipeline dependencies.
RUN pip install --no-cache-dir "apache-airflow==3.3.2" -r /requirements.txt
