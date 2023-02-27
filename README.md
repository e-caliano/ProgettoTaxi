# ProgettoTaxi

# Questo file viene redatto al fine di guidare l'utente nell'utilizzo del programma. 

Per poter eseguire il programma si eseguano i seguenti passaggi:

 1) Creare una cartella "Data" dove posizionare i file .PARQUET;
 2) Salvare il Path della cartella "Data" (opzionale, ma strettamente consigliato);
 3) Lanciare il modulo "main.py" dove verranno chiesti i seguenti campi:
	- Inserisci l'anno desiderato (formato YYYY):
	- Inserisci i mesi desiderati (separati da virgola):
	- Inserisci i nomi dei quartieri separati da virgole (premere Invio per selezionare tutti i quartieri):
	- Digita il path della direcory Data:

 Di seguito si propone un esempio dell'utilizzo del programma: 

	Inserisci l'anno desiderato (formato YYYY): 2022

 	Inserisci i mesi desiderati (separati da virgola): 03,04

 	Inserisci i nomi dei quartieri separati da virgole (premere Invio per selezionare tutti i quartieri): 

 	Digita il path della direcory Data: /Users/edoardocaliano/Desktop/PrgettoTaxi/Data

In output verranno visualizzate i seguenti elementi:
	
	- dataframe dove per ogni quartiere, mese e anno scelti, sarà mostrato la durata dei viaggi (secondi);
	- quartiere dove è stato mostrato il viaggio con maggiore durata (nel caso in cui si volesse analizzare tutta NY);
	- dataframe dove vengono mostrati tutti i borough con i rispettivi viaggi di durata maggiore (secondi);
	- quartiere dove è stato mostrato il viaggio con minore durata (nel caso in cui si volesse analizzare tutta NY);
	- dataframe dove vengono mostrati tutti i borough con i rispettivi viaggi di durata minore (secondi);
	- lista in cui vengono mostrati, in ordine di mese tra quelli inseriti, la durata dei viaggi minimi e massimi;
	- un plot dei risultati della riga precedente.  


# Alla fine del programma dovrebbe essere visualizzato a schermo l'istogramma con le durate dei tragitti per i mesi dell'anno che sono stati selezionati
