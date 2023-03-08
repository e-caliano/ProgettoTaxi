import pandas as pd
import os
import matplotlib.pyplot as plt


def plot_durata_massima_per_quartiere(lista_df2, filename):
    """
    :param lista_df2: lista di dataframes
    :param filename: stringa
    """
    # Calcolo la durata massima per ogni quartiere
    durate_massime = []
    quartieri = []
    for df in lista_df2:
        #Per ogni dataframe nella lista creo un dataframe che raggruppa i viaggi in base al quartiere di partenza
        quartiere_durata_massima = df.groupby(['borough'])['durata'].max()
        #aggiungo elementi presenti nella lista quartieri estratta dalla serie
        quartieri.extend(quartiere_durata_massima.index.tolist())
        #aggiungo le durate massime
        durate_massime.extend(quartiere_durata_massima.tolist())

    # Creo il DataFrame con i dati da plottare
    data_to_plot = pd.DataFrame({'quartiere': quartieri, 'durata_massima': durate_massime})
    # Plottaggio dell'istogramma. Do una dimensione scelta
    plt.figure(figsize=(12, 6))
    plt.bar(data_to_plot['quartiere'], data_to_plot['durata_massima'])
    #Titolo
    plt.title('DURATE MASSIME DEI QUARTIERI DI NEW YORK')
    #asse x
    plt.xlabel('Quartiere')
    #asse y
    plt.ylabel('Durata massima (s)')
    # Salvo l'istogramma come file png nella cartella output
    plt.savefig("output/" + filename + '.png')
    print(f"L'istogramma è stato salvato nel file {filename}.png")
