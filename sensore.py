class Sensore: 
    def __init__(self, codice: str, grandezza: str, unita: str, soglia: float) -> None:
        self.codice = codice
        self.grandezza = grandezza.lower()
        self.unita = unita.lower()
        self.soglia = soglia

    def __str__(self):
        return f"{self.codice}"

    
sensore1 = Sensore("A", "Temperatura", "Celsius", 100)