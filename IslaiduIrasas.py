from datetime import datetime
from irasas import irasas
now=datetime.now()

islaidos="3"
papildomas_skaicius=1
id=""
indentifikavimo_numeris=[]
def indentifikavimas():
    global id
    global papildomas_skaicius
    id = int(islaidos + str(papildomas_skaicius))
    papildomas_skaicius += 1
    indentifikavimo_numeris.append(id)
    return id

class islaiduirasas:
    def __init__(self,suma, kategorija,atsiskaitymo_budas,isigyta_preke_palauga,data=now.strftime("%Y:%m:%d %H:%M:%S")):
        self.data= data
        self.suma= suma
        self.kategorija=kategorija
        self.atsiskaitymo_budas=atsiskaitymo_budas
        self.isigyta_preke_paslauga=isigyta_preke_palauga
        self.g = f"Tipas: Islaidos, Suma: {suma}, Kategorija: {kategorija}, Atsiskaitymo budas: {atsiskaitymo_budas}, Sumoketa uz: {isigyta_preke_palauga} Irasas padarytas: {data}, ID: {indentifikavimas()}"
# class islaiduirasas(irasas):
#     pass