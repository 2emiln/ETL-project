# Ett simpelt ETL-flöde


## Kom igång

Börja med att köra pip install requirements.txt:
> pip install -r requirements.txt

## Projektstruktur
```
etl-project/
│── data/
│   └── raw/
│       └── sales.csv         # Inputfil
│   └── sales_per_city.db     # Output (SQLite)
│
│── etl/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
│── logs/
│   └── etl.log               # Loggar
│
│── tests/
│   └── test_transform.py     # Pytest
│
│── main.py                   # Huvudskript
│── requirements.txt
│── README.md
```

## Flöde
```
1. Extract.py - Läser in rådata från data/raw/sales.csv
2. Transform.py - Transformerar datan till 2 kolumner och summerar försäljningen per stad
3. Load.py - Lägger in data i en SQL-databas

Alla steg loggas till etl/logs
```

