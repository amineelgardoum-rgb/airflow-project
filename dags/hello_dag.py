from datetime import datetime 
from airflow.sdk import dag,task 

@dag(
    dag_id="hello_dag",
    start_date=datetime(2025,1,1),
    schedule="@daily",
    catchup=False
)
def hello():
    @task 
    def say_hello():
        print("Hello From Airflow")
        return "done"
    
    @task 
    def say_bye(msg):
        print(f"Message from {msg}")
        
    
    say_bye(say_hello())
    
hello()
