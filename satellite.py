from sensore import Sensore

class Satellite:
    def __init__(self) -> None:
        self.sensori = {}
        self.letture = []

    def aggiungi_sensore(self, sensore: Sensore) -> None:
        if sensore.codice in self.sensori:
            raise ValueError("Senore già contenuto")
    
        self.sensori[sensore.codice] = sensore

    def registra_lettura(self, codice_sensore: str, valore: float) -> None:
        if codice_sensore not in self.sensori:
            raise KeyError("Codice non contenuto")

        sensore = self.sensori[codice_sensore]

        self.letture.append(
                {
                    "sensore": sensore,
                    "grandezza": sensore.grandezza,
                    "valore": valore,
                    "unita": sensore.unita,
                    "allarme": valore > sensore.soglia
                }   
        )

    def letture_in_allarme(self) -> list[dict]:
        result = []
        for lettura in self.letture:
            if lettura["allarme"]:
                result.append(lettura)

        return result
    