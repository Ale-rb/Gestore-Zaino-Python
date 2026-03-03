import os

class Zaino:

    def __init__(self):
        self.cartella_corrente = os.path.dirname(__file__)
        self.percorso_file = os.path.join(self.cartella_corrente, "Zaino.txt")
        self.Lista_Zaino=[]
        
        
        try:
            with open(self.percorso_file, "r") as file:
                for riga in file:
                    self.Lista_Zaino.append(riga.strip()) # .strip() toglie il "\n" (invio) alla fine della riga
        except FileNotFoundError:
            print("File non trovato, ne verrà creato uno nuovo alla prima aggiunta.")
            
    def salva_su_disco(self):
        # Creiamo un metodo dedicato solo al salvataggio totale
        with open(self.percorso_file, "w") as file:
            for x in self.Lista_Zaino:
                file.write(x + "\n")
        print("Dati salvati correttamente nel file.")
        
    def aggiungi_materia(self,Materia):
        self.Lista_Zaino.append(Materia)
        with open("Zaino.txt", "a") as file:
            file.write(Materia +"\n")
    
    def rimuovi_materia(self,Materia):
        if Materia in self.Lista_Zaino:
            self.Lista_Zaino.remove(Materia)
            with open("Zaino.txt","w") as file:
                for x in self.Lista_Zaino:
                    file.write(x+"\n")
                print("Materia: ", Materia, "rimossa")
                print("Lista aggiornata: ")
                self.mostra_zaino()
            
        else:
            print("Materia non trovata.")
            
        
        
    def mostra_zaino(self):
        for x in self.Lista_Zaino:
            print(x)

def main():
    mio_zaino=Zaino()
    while True:
        print("-----menu-----")
        print("1.Aggiungi")
        print("2.Mostra Zaino")
        print("3.Rimuovi materia")
        print("4.Esci")
        
        scelta=input("Segli una voce dal menu: ")
        
        if scelta=="1":
            Materia=input("Inserisci la materia da aggiungere: ")
            mio_zaino.aggiungi_materia(Materia)
            print("Materia aggiunta: ",Materia)
            mio_zaino.mostra_zaino()
            
        elif scelta=="2":
            print("Lista Materie: ")
            mio_zaino.mostra_zaino()
            
        elif scelta=="3":
            Materia=input("Quale materia vuoi eliminare?: ")
            mio_zaino.rimuovi_materia(Materia)
            
        elif scelta=="4":
            mio_zaino.salva_su_disco()
            print("Chiusura programma...")
            break
        else:
            print("Voce menu non valida")
            
main()