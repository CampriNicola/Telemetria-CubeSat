from sensore import Sensore
from satellite import Satellite

CubeSatAurora = Satellite()

sensore1 = Sensore("1", "Metri", "Km", 1000)
sensore2 = Sensore("2", "Temperatura", "Celsius", 40)
sensore3 = Sensore("3", "Velocità", "m/s", 10)

CubeSatAurora.aggiungi_sensore(sensore1)
CubeSatAurora.aggiungi_sensore(sensore2)
CubeSatAurora.aggiungi_sensore(sensore3)

CubeSatAurora.registra_lettura("1", 500)
CubeSatAurora.registra_lettura("1", 5000.5)
CubeSatAurora.registra_lettura("2", 30)
CubeSatAurora.registra_lettura("2", 40)
CubeSatAurora.registra_lettura("3", 90)
CubeSatAurora.registra_lettura("1", 10)

allarmi = CubeSatAurora.letture_in_allarme()

CubeSatAurora.riepilogo()