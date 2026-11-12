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

    def riepilogo(self) -> None:
        print("Riepilogo satallite")

        for lettura in self.letture:
            allarme = ""
            if lettura["allarme"]:
                allarme = "ALLARME"
            else:
                allarme = "OK"
            print(f"lettura -- sensore: {lettura["sensore"]}; grandezza: {lettura["grandezza"]}; valore: {lettura["valore"]}; unita: {lettura["unita"]}; allarme: {allarme}")



#Test allarmi
satellite = Satellite()

satellite.aggiungi_sensore(Sensore("AAA", "Temperatura", "Celsius", 100))


satellite.registra_lettura("AAA", 40)
satellite.registra_lettura("AAA", 100)
satellite.registra_lettura("AAA", 200)

satellite.riepilogo()

