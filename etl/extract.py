import pandas as pd

def extract_data():
    return pd.read_csv(
        "data/Global_Superstore.csv",
        sep="\t" #seperate by tab not comma
    )
