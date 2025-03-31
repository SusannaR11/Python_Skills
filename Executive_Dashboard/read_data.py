import pandas as pd
from pathlib import Path


def load_data(filepath):
    data_path = Path(__file__).parents[1]/filepath
    df= pd.read_csv("data/supahcoolsoft.csv")
    return df

if __name__ == "__main__":
    df = load_data()
    print(df.columns)
    


    