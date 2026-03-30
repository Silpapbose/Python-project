
import pandas as pd

def load_data(path="data/weather.csv"):
    try:
        df = pd.read_csv(path)
        print(f" Loaded data from {path}")
        return df
    except FileNotFoundError:
        print(f" File not found: {path}")
    except Exception as e:
        print(f" Error loading data: {e}")

    return None
