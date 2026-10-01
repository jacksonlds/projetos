from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def extrair_dados(**kwargs):
    print("Iniciando a extração de dados brutos dos táxis...")
    dados = {"viagens": 1500, "origem": "BigQuery"}
    kwargs['ti'].xcom_push(key='dados_brutos', value=dados)
    print("Extração concluída com sucesso.")

def transformar_dados(**kwargs):
    print("Iniciando a transformação e limpeza dos dados...")
    ti = kwargs['ti']
    dados = ti.xcom_pull(key='dados_brutos', task_ids='extrair_dados')
    viagens_filtradas = dados['viagens'] * 0.95
    dados_transformados = {"viagens_limpas": int(viagens_filtradas), "status": "Limpo"}
    ti.xcom_push(key='dados_transformados', value=dados_transformados)
    print(f"Transformação concluída. Registos válidos: {int(viagens_filtradas)}")

def carregar_dados(**kwargs):
    print("Iniciando a carga dos dados transformados...")
    ti = kwargs['ti']
    dados = ti.xcom_pull(key='dados_transformados', task_ids='transformar_dados')
    print(f"Carga finalizada com sucesso! {dados['viagens_limpas']} registos carregados.")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'etl_taxis_pipeline_simples',
    default_args=default_args,
    description='DAG simples de ETL para o projeto de táxis',
    schedule=timedelta(days=1),  # Atualizado para o parâmetro correto 'schedule'
    start_date=datetime(2026, 1, 1),
    catchup=False,
) as dag:

    t1 = PythonOperator(task_id='extrair_dados', python_callable=extrair_dados)
    t2 = PythonOperator(task_id='transformar_dados', python_callable=transformar_dados)
    t3 = PythonOperator(task_id='carregar_dados', python_callable=carregar_dados)  # Sintaxe corrigida

    t1 >> t2 >> t3