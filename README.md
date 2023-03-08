# ProgettoTaxi

# Questo file viene redatto al fine di guidare l'utente nell'utilizzo del programma. 

Per poter eseguire il programma si eseguano i seguenti passaggi:

 1) Fare riferimento alla directory "src" e ai suoi file con "_prova" (sono questi quelli da prendere in considerazione)
 2) Creare una cartella "Data" dove posizionare i file .PARQUET;
 3) Creare la directory "output" dove verrano caricati gli output (qualora la cartella non fosse scaricata o presente nel progetto);
 4) Salvare il Path della cartella "Data" (opzionale, ma strettamente consigliato);
 5) Lanciare il modulo "Main_prova.py" dove verranno chiesti i seguenti campi:
	- Inserisci l'anno desiderato (formato YYYY):
	- Inserisci i mesi desiderati (separati da virgola):
	- Inserisci i nomi dei quartieri separati da virgole, i quartieri sono: "Manhattan", "EWR", "Staten Island", "Bronx", "Queens", "Brooklyn", se si inserisce un quartiere 
	  non presente, esso non verrà preso in considerazione. Se non viene inserito nessun quartiere, l'output che riguarda i quartieri da visualizzare sarà un dataframe vuoto!
	- Digita il path della directory Data:

 Di seguito si propone un esempio dell'utilizzo del programma: 

inserisci anno: 2022
inserisci mese: 03,04
inserisci path assoluto: /Users/edoardocaliano/Desktop/PrgettoTaxi/Data
Inserisci i quartieri della quale vuoi conoscere le durate: EWR,Manhattan


In output verranno visualizzate i seguenti elementi:
	
I dati sono stati esportati nel file Durate_per_quartiere_cercato_ufficiale.csv
I dati sono stati esportati nel file Durate_minima_e_massima.csv
L'istogramma è stato salvato nel file Istogramma.png 

Durate_per_quartiere_cercato_ufficiale.csv rappresenta un dataframe contenente i quartieri scelti e una annessa serie aggiunta della durata delle corse. 
Durate_minima_e_massima.csv contiene un dataframe in cui sono rappresentati il viaggio più piccolo e il viaggio più grande tra tutti i dataframe. 
Istogramma.png rappresenta un istogramma che indica per ogni quartiere le corrispettive durate massime. 


