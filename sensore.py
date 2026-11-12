class Sensore: 
    def __init__(self, codice: str, grandezza: str, unita: str, soglia: float) -> None:
        self.codice = codice.lower
        self.grandezza = grandezza.lower
        self.unita = unita.lower
        self.soglia = soglia

    
