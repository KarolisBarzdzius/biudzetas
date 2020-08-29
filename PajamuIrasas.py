from datetime import datetime
from irasas import irasas

now=datetime.now()
pajamos="2"
papildomas_skaicius=1
id=""
indentifikavimo_numeris=[]
def indentifikavimas():
    global id
    global papildomas_skaicius
    id = int(pajamos + str(papildomas_skaicius))
    papildomas_skaicius += 1
    indentifikavimo_numeris.append(id)
    return id

class pajamuirasas:
    def __init__(self, suma, kategorija,papildoma_informacija,siuntejas,data=now.strftime("%Y:%m:%d %H:%M:%S")):
        self.data = data
        self.papildoma_informacija=papildoma_informacija
        self.siuntejas=siuntejas
        self.suma = suma
        self.kategorija = kategorija
        self.g= f" Tipas: Pajamos, Suma: {suma}, Kategorija: {kategorija}, Papildoma informacija: {papildoma_informacija}, Siuntejas: {siuntejas}, Irasas padarytas: {data}, ID: {indentifikavimas()}"
# class pajamuirasas(irasas):
#     def __init__(self,papildoma_informacija="",siuntejas=""):
#         self.papildoma_informacija=papildoma_informacija
#         self.siuntejas=siuntejas