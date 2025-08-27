from etl.extract import extract
from etl.transform import transform

df = extract()
print(df.head())