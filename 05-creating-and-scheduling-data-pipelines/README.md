# Creating and Scheduling Data Pipelines

use this code to check for running containers 
```sh
docker ps
```
if using Linux, run the code below

```sh
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

1. Run Docker Compose

```sh
docker-compose up
```
2. open Airflow UI from port 8080

3. login Airflow

4. run etl from DAGs

**หมายเหตุ:** จริง ๆ แล้วเราสามารถเอาโฟลเดอร์ `data` ไว้ที่ไหนก็ได้ที่ Airflow ที่เรารันเข้าถึงได้ แต่เพื่อความง่ายสำหรับโปรเจคนี้ เราจะนำเอาโฟลเดอร์ `data` ไว้ในโฟลเดอร์ `dags` เลย