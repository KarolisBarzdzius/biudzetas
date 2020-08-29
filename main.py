from Biudzetas import *

adresatai=[]

vardas = str(input("Iveskite varda: "))
e = biudzetas(vardas)
adresatai.append(e)
while True:
        print("1 - Ataskaita")
        print("2 - Pajamu ivedimas")
        print("3 - Islaidu ivedimas")
        print("4 - Balansas")
        print("5 - Iseiti")
        try:
            q=int(input("Pasirinkite: "))
            if q == 1:
                print(e.gauti_ataskaita())
            elif q==2:
                print(e.ivesti_pajamas(suma=int(input("Iveskite pajamas: ")),kategorija=str(input("Iveskite kategorija:")),siuntejas=str(input("Iveskite siunteja: ")),papildoma_informacija=str(input("Iveskite papildoma informacija: "))))
            elif q==3:
                print(e.ivesti_islaidas(suma=int(input("Iveskite islaidas: ")),kategorija=str(input("Iveskite kategorija: ")),atsiskaitymo_budas=str(input("Atsiskaitymo budas: ")),isigyta_preke_paslauga=str(input("Mokketa uz: "))))
            elif q==4:
                print(e.gauti_balansa())
            elif q==5:
                break
            elif q==6:
                print(vardas)
            elif q==7:
                pass
            elif q==8:
                pass
            else:
                print("Nerasta")
        except ValueError:
            pass