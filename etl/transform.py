import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    # Drop rows without order ID
    df = df.dropna(subset=["Order ID"])

    # Convert dates
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    # Profit margin
    df["Profit Margin"] = df["Profit"] / df["Sales"]

    # Ingestion timestamp
    df["Ingested At"] = pd.Timestamp.now()

    # Rename columns (only ones we use)
    df = df.rename(columns={
        "Order ID": "order_id",
        "Order Date": "order_date",
        "Ship Date": "ship_date",
        "Ship Mode": "ship_mode",
        "Customer ID": "customer_id",
        "Customer Name": "customer_name",
        "Segment": "segment",
        "Country": "country",
        "Region": "region",
        "State": "state",
        "City": "city",
        "Product ID": "product_id",
        "Category": "category",
        "Sub-Category": "sub_category",
        "Sales": "sales",
        "Profit": "profit",
        "Quantity": "quantity",
        "Discount": "discount",
        "Shipping Cost": "shipping_cost",
        "Profit Margin": "profit_margin",
        "Ingested At": "ingested_at"
    })

    # Select final columns (match DB schema)
    df = df[
        [
            "order_id", "order_date", "ship_date", "ship_mode",
            "customer_id", "customer_name", "segment",
            "country", "region", "state", "city",
            "product_id", "category", "sub_category",
            "sales", "profit", "quantity", "discount",
            "shipping_cost", "profit_margin", "ingested_at"
        ]
    ]

    return df
