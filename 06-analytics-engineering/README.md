# Analytics Engineering

use virtual environment and download requirements
```sh
python -m venv ENV
source ENV/bin/activate
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
