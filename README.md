# ETL-project

Projektstruktur

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
│── main.py                   # Orkestrering
│── requirements.txt
│── README.md