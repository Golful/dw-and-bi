# import logging

# from airflow import DAG
# from airflow.operators.empty import EmptyOperator
# from airflow.operators.bash import BashOperator
# from airflow.operators.python import PythonOperator
# from airflow.utils import timezone

# import requests

# def _get_dog_api():
#     response = requests.get("https://dog.ceo/api/breeds/image/random")
#     data = response.json()
#     logging.info(data)
#     with open


# def _say_hello():
#     logging.debug("This is DEBUG log")
#     logging.info("hello")


# with DAG(
#     "hello",
#     start_date=timezone.datetime(2024, 3, 23),
#     schedule=None,
#     tags=["DS525"],
# ):
#     start = EmptyOperator(task_id="start")
    
#     get_dog_api = PythonOperator(
#         task_id="get_dog_api",
#         python_callable=_get_dog_api
#     )


#     end = EmptyOperator(task_id="end")

#     start >> echo_hello >> end
#     start >> say_hello >> end