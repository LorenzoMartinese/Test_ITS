class Saluto:
    def __init__(self):
        self.testo = self.setTesto()
        self.destinatario = self.setDestinatario()

    def setTesto(self):
        testo = input("Inserisci qui il tuo saluto: ")
        return testo
    
    def setDestinatario(self):
        testo = input("Inserisci qui la persona o le persone che vuoi salutare: ")
        return testo # Added the missing return!

    def getSaluto(self):
        return self.testo + " a " + self.destinatario
    
if __name__ == "__main__":
    saluto1 = Saluto() 
    print(saluto1.getSaluto())