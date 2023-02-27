import pandas as pd
import main
import os
import sys
import matplotlib.pyplot as plt


# chiedi all'utente l'anno, i mesi e i nomi dei quartieri desiderati come input
anno = input("Inserisci l'anno desiderato (formato YYYY): ")
mesi = input("Inserisci i mesi desiderati (separati da virgola): ").split(',')
quartieri_input = input("Inserisci i nomi dei quartieri separati da virgole (premere Invio per selezionare tutti i quartieri): ")



if quartieri_input == "":
    quartieri = None
else:
    quartieri = [q.lower() for q in quartieri_input.split(",")]

# def imposta_directory():
#     path = input("Digita il path della directory Data: ")
#     return path

# impostiamo il percorso della directory contenente i file PARQUET
percorso_directory = input("Digita il path della direcory Data: ")

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
        # carichiamo il dataframe dei dati delle corse dei taxi dal file CSV tramite l'apposita function del modulo prova
        df = main.load_file(file_parquet)
        # facciamo il merge con il df_lookup tramite l'apposita function del modulo prova
        df = main.merge(df)

        if quartieri is not None:

            df = df[df['borough'].str.lower().isin(quartieri)]


            if len(df) == 0:
                print(f"Errore: Nessuna corsa trovata per tutti quartieri inseriti {quartieri}, runnare nuovamente il programma digitando il nome corretto per i quartieri desiderati")
                exit()


            # azione di filtraggio del df tramite apposita function del modulo prova
            df = main.filter(df)

            # calcolo e aggiunta delle durate dei tragitti tramite apposita function del modulo prova
            df = main.durata(df)

        else:

            df = main.filter(df)
            df = main.durata(df)

        dfs.append(df)
#print(main.viaggio_più_breve(dfs))
#print(main.viaggio_più_lungo(dfs))
#df_concatenato = pd.concat(dfs)
#print(df_concatenato)

def dizionario_per_plot(mesi):
    """
    :param mesi:lista
    :return:
    """
    min_durata_corsa= main.viaggio_più_breve(dfs)[1]
    max_durata_corsa=main.viaggio_più_lungo(dfs)[1]

    dizionario = {}
    for i in range(len(mesi)):
        dizionario[mesi[i]] = [min_durata_corsa[i], max_durata_corsa[i]]
    dizionario_ordinato = dict(sorted(dizionario.items(), key=lambda x: x[0]))
    return dizionario_ordinato
dizionario= dizionario_per_plot(mesi)
durate_minime = [dizionario[month][0] for month in mesi]
durate_massime = [dizionario[month][1] for month in mesi]


def crea_istogramma_durata_viaggi(dizionario):
    """
    Crea un istogramma della durata dei viaggi, suddivisi per mese.

    :param dizionario: dizionario contenente le durate dei viaggi per ogni mese
    :return: None
    """

    # Creazione dell'istogramma
    fig, ax = plt.subplots()
    valori = [valore[1] - valore[0] for valore in dizionario.values()]
    bottom = [valore[0] for valore in dizionario.values()]
    colori = ['red', 'blue', 'green', 'orange', 'purple', 'pink', 'brown', 'gray', 'olive', 'teal', 'navy',
              'maroon']  # Lista di colori per le colonne

    ax.bar(dizionario.keys(), valori, bottom=bottom, width=0.5, color=colori)

    # Impostazione dei valori sull'asse y
    valori_y = [i * 50000 for i in range(15)]  # Crea una lista di valori da 0 a 700000 con un intervallo di 100000
    plt.yticks(valori_y)
    plt.title("DURATA VIAGGI")

    # Etichettatura degli assi
    plt.xlabel('Mesi')
    plt.ylabel('Secondi')

    # Visualizzazione dell'istogramma
    plt.show()