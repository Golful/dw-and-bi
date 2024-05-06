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
