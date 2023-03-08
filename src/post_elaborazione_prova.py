import pandas as pd


def export_to_csv(lista_df1, filename):
    """
    :param lista_df1: lista di dataframes
    :param filename: stringa
    """
    # Concatena tutti i DataFrame nella lista in uno unico
    df = pd.concat(lista_df1, axis=0, ignore_index=True)
    # Ordina il DataFrame in ordine decrescente di durata
    df.sort_values(by='durata', ascending=False, inplace=True)
    # Scrive il file CSV nella cartella output
    df.to_csv("output/" + filename + '.csv', index=False)
    print(f"I dati sono stati esportati nel file {filename}.csv")

def export_min_max_durata_to_csv(durata_minima, durata_massima,filename):
    """
    :param durata_minima: dataframe
    :param durata_massima: dataframe
    :param filename: stringa
    """
    # Concatena i DataFrame di min_durata e max_durata in uno unico
    df = pd.concat([durata_minima, durata_massima], axis=0, ignore_index=True)
    # Scrive il file CSV nella cartella output
    df.to_csv("output/" + filename + '.csv', index=False)
    print(f"I dati sono stati esportati nel file {filename}.csv")

