# ETL-flöde för summering av resturanger i olika städer


## Kom igång

### För Python
```
python -m venv venv
venv\Scripts\activate (Windows)
source venv/bin/activate (Mac/Linux)

Installera requirements
> pip install -r requirements.txt
```

### För Anaconda
```
conda create -n etl python=3.11 -y
conda activate etl

Installera requirements
> pip install -r requirements.txt
```

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
1. Extract.py   - Läser in rådata från data/raw/sales.csv
2. Transform.py - Transformerar datan till 2 kolumner och summerar försäljningen per stad
3. Load.py      - Lägger in data i en SQL-databas

Alla steg loggas till etl/logs
```

## Exempel

### Input (Från CSV)
```
order_id,date,restaurant,city,total,payment_method
1,2025-01-01,Bistro Aurora,Stockholm,1200,Card
2,2025-01-02,Cafe Nord,Göteborg,800,Cash
```

### Output (Till Databasen)
```
city         total_sales
Göteborg     800
Stockholm    1200
```