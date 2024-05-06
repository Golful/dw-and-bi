# Building a Data Warehouse


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

Run etl_bigquery.py
```sh
python etl_bigquery.py
```

Open Bigquery and try using query
```sh
SELECT actor, count(1) as c 
FROM `ascendant-voice-413911.github.events` 
group by actor
order by c desc
```