# Analytics Engineering

use virtual environment and download requirements
```sh
python -m venv ENV
```
```sh
source ENV/bin/activate
```
```sh
pip install -r requirements.txt
```

SQL Pad
```sh
docker compose up
```
- open port 3000
-fill in email and password from docker-compose.yml

Test dbt connection
```sh
dbt debug
```
You should see "All checks passed!".

To create models
```sh
dbt run
```

To test models
```sh
dbt test
```
