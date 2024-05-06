# Data Modeling 1

For Mac users:

```sh
brew install postgresql
```

## Running Postgres
```sh
docker-compose up
```
- open port 8080

To shutdown, press Ctrl+C and run:

```sh
docker-compose down
```

## Running ETL Scripts

```sh
python create_tables.py
python etl.py
```

## Steps
### 1) docker-compose up
### 2) python create_tables.py
### 3) python etl.py


## Tables

### Actors
|Attribute|Data Type|Note|
|:------------|:---------------:|:---------------:|
|id|int||
|login|text|username|
|url|text|link of the actor’s profile|

### Events
|Attribute|Data Type|Note|
|:------------|:---------------:|:---------------:|
|id|text||
|type|text|type of event|
|actor_id|int|(foreign key)|
|created_at|text|time event created|

### Repos
|Attribute|Data Type|Note|
|:------------|:---------------:|:---------------:|
|id|int||
|name|text||
|event_id|text|(foreign key)|
