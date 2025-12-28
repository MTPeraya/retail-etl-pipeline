from sqlalchemy import create_engine
import pandas as pd

def load_to_postgres(df: pd.DataFrame, table_name: str):
    engine = create_engine(
        "postgresql://postgres:postgres@postgres:5432/postgres"
    )

    df.to_sql(table_name, engine, if_exists="append", index=False)
