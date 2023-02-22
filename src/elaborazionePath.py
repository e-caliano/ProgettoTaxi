import os
import pandas as pd

# chiedi all'utente l'anno, i mesi e i nomi dei quartieri desiderati come input
anno = input("Inserisci l'anno desiderato (formato YYYY): ")
mesi = input("Inserisci i mesi desiderati (separati da virgola): ").split(',')
quartieri = input("Inserisci i nomi dei quartieri desiderati (separati da virgola): ").split(',')

# impostiamo il percorso della directory contenente i file PARQUET
percorso_directory = '/Users/edoardocaliano/Desktop/PrgettoTaxi/Data'

# otteniamo l'elenco di tutti i file nella directory specificata
elenco_file = os.listdir(percorso_directory)

# impostiamo il prefisso del nome del file PARQUET desiderato
prefisso_nome_file = 'yellow_tripdata_'

# elenco vuoto di dataframe per ogni file PARQUET
dfs = []

# otteniamo solo l'elenco dei file PARQUET e aventi il prefisso desiderato
elenco_file_parquet = [os.path.join(percorso_directory, file) for file in elenco_file if file.endswith('.parquet') and file.startswith(prefisso_nome_file)]


# iteriamo su ogni file PARQUET selezionato e carichiamo i dati in un dataframe pandas
for file_parquet in elenco_file_parquet:

    # lista che contiene gli elementi di elenco_file_parquet separati dal carattere '_'
    file_info = file_parquet.split('_')

    # selezione dell'ano dal file PARQUET selezionato
    anno_file = file_info[2][:4]

    # selezione del mese dal file PARQUET selezionato
    mese_file = file_info[-1][5:7]
    # print(anno_file)
    # print(mese_file)

    # controlliamo se il file corrente è stato selezionato dall'utente
    if anno_file == anno and mese_file in mesi:
        # carichiamo il dataframe dei dati delle corse dei taxi dal file CSV
        df = pd.read_parquet(file_parquet, engine="pyarrow")
        dfs.append(df)

df_concatenato = pd.concat(dfs)
print(df_concatenato)


