import pandas as pd

# funzione che crea un dataframe passando il path (eventualmente assoluto) del file
def load_file(path):
    df = pd.read_parquet(path, engine='pyarrow')
    return df

x = load_file('/Users/edoardocaliano/Desktop/PrgettoTaxi/Data/yellow_tripdata_2022-03.parquet')
print(x)



