import pandas as pd

# parquetFile = '/Users/edoardocaliano/Desktop/PrgettoTaxi/Data/yellow_tripdata_2022-03.parquet'
df = pd.read_parquet('/Users/edoardocaliano/Desktop/PrgettoTaxi/Data/yellow_tripdata_2022-03.parquet', engine='pyarrow')
print(df.columns)
pickUp = df['tpep_pickup_datetime']
print(pickUp)