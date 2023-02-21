import pandas as pd

# funzione che crea un dataframe passando il path (eventualmente assoluto) del file
def load_file(path):
    # estraiamo l'estensione del file, split prende l'ultimo elemento direttamente dopo il punto
    extension = path.split(".")[-1]

    if extension == "csv":
        # se l'estensione è csv, carichiamo il DataFrame dal file CSV
        df = pd.read_csv(path)
    elif extension == "parquet":
        # se l'estensione è parquet, carichiamo il DataFrame dal file PARQUET
        df = pd.read_parquet(path, engine='pyarrow')
    else:
        # se l'estensione non è supportata, solleviamo un'eccezione
        raise ValueError("Estensione del file non supportata. Sono supportati solo i file CSV e PARQUET.")

    return df

x = load_file('/Users/edoardocaliano/Desktop/PrgettoTaxi/Data/yellow_tripdata_2022-03.parquet')
print(x)

y = load_file('/Users/edoardocaliano/Desktop/PrgettoTaxi/Data/taxi+_zone_lookup.csv')
print(y)

#funzione per unire il file parquet con il file csv
def Merge(df1,df2):
    pass


#funzione per il filtraggio del dataframe totale
def filter(df):
    pass


#funzione per trasformare le series delle partenze e degli arrivi in secondi, per poi dopo calcolare la durata effettiva
def toTimestamp():
    pass


#funzione per trovare le durate effettive dei viaggi, il minimo e il massimo
def durate():
    pass

