from extract import extract_data
from transform import transform_data
from load import load_to_postgres

df = extract_data()
df = transform_data(df)
load_to_postgres(df, "orders")

print("ETL completed successfully")
