from datetime import datetime
from PajamuIrasas import pajamuirasas
from IslaiduIrasas import islaiduirasas
import pickle


class biudzetas:
    def __init__(self,vardas):
        self.vardas=vardas
        self.pajamu_zurnalas=[]
        self.islaidu_zurnalas=[]
        self.zurnalas=[]
        self.stringai=[]



    def ivesti_pajamas(self,suma, kategorija,siuntejas,papildoma_informacija):
        pajamos=pajamuirasas(suma,kategorija,siuntejas,papildoma_informacija)
        self.pajamu_zurnalas.append(suma)
        self.zurnalas.append(pajamos)
        self.stringai.append(pajamos.g)
        with open("pajamos.pkl","wb") as pickle_out:
            pickle.dump(pajamos,pickle_out)

    with open("pajamos.pckl", "rb") as pickle_in:
        naujas_pajamos = pickle.load(pickle_in)
    print(naujas_pajamos)


    def ivesti_islaidas(self,suma,kategorija,atsiskaitymo_budas,isigyta_preke_paslauga):
        islaidos=islaiduirasas(suma,kategorija,atsiskaitymo_budas,isigyta_preke_paslauga)
        self.zurnalas.append(islaidos)
        self.islaidu_zurnalas.append(suma)
        self.stringai.append(islaidos.g)
        with open("islaidos.pkl","wb") as pickle_out:
            pickle.dump(islaidos,pickle_out)

    def gauti_balansa(self):
        print(f"{self.vardas}.Jusu balansas yra: {sum(self.pajamu_zurnalas) - sum(self.islaidu_zurnalas)}")

    def gauti_ataskaita(self):
        print(self.stringai)

    def zurnalas(self):
        print(self.zurnalas)


with open("pajamos.pckl", "rb") as pickle_in:
    naujas_pajamos=pickle.load(pickle_in)