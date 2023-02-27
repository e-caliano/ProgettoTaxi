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

           id        borough  ... tpep_dropoff_datetime durata_corsa
 0        163      Manhattan  ...   2022-04-01 00:58:33       2240.0
 1        163      Manhattan  ...   2022-04-01 00:21:41       1251.0
 2        163      Manhattan  ...   2022-04-01 00:49:57        199.0
 3        163      Manhattan  ...   2022-04-01 01:10:44        788.0
 4        163      Manhattan  ...   2022-04-01 00:25:31        428.0
 ...      ...            ...  ...                   ...          ...
 3599915  204  Staten Island  ...   2022-04-28 23:40:47          5.0
 3599916  204  Staten Island  ...   2022-04-28 23:45:01         15.0
 3599917  204  Staten Island  ...   2022-04-28 23:46:59         13.0
 3599918  204  Staten Island  ...   2022-04-28 23:50:57         11.0
 3599919   59          Bronx  ...   2022-04-01 12:30:00       1980.0



 Il quartiere dove è stato effettuato il viaggio maggiore è: Manhattan
 borough
 Bronx             86086.0
 Brooklyn          87090.0
 EWR               21074.0
 Manhattan        482262.0
 Queens           345206.0
 Staten Island     15005.0


 I quartieri dove è stato effettuato il viaggio minore sono: Bronx, Brooklyn, EWR, Manhattan, Queens, Staten Island
 borough
 Bronx            1.0
 Brooklyn         1.0
 EWR              1.0
 Manhattan        1.0
 Queens           1.0
 Staten Island    1.0

 'I minimi per ogni mese, in ordine, sono, in secondi:' [1.0, 1.0]

 'I massimi per ogni mese, in ordine, sono, in secondi:' [482262.0, 209739.0]

 'I minimi per ogni mese, in ordine, sono, in secondi:' [1.0, 1.0]

 'I massimi per ogni mese, in ordine, sono, in secondi:' [482262.0, 209739.0] 

# Alla fine del programma dovrebbe essere visualizzato a schermo l'istogramma con le durate dei tragitti per i mesi dell'anno che sono stati selezionati
