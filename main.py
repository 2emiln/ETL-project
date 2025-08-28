from etl.extract import extract
from etl.transform import transform
from etl.load import load_to_sql

def main():
    df = extract("data/raw/sales.csv")
    df_t = transform(df)
    load_to_sql(df_t)  # skriver till data/sales_per_city.db, tabell sales_per_city
    print("Klar.")

if __name__ == "__main__":
    main()
