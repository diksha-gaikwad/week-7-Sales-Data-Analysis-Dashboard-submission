import pandas as pd

def load_sales_data(path):
    try:
        df = pd.read_csv(path)
        df['order_date'] = pd.to_datetime(df['order_date'])
        print("Data Loaded Successfully")
        print(df.head())
        return df
    except Exception as e:
        print("Error:", e)