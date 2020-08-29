from datetime import datetime

class irasas:
    def __init__(self,suma, kategorija,data=datetime.now()):
        self.suma=suma
        self.kategorija=kategorija
        self.data=data
        self.g = f" Tipas: Pajamos, Suma: {suma}, Laikas: {data},Kategorija: {kategorija}"