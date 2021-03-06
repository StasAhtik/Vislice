STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA = '+', 'o', '-'
ZACETEK = "s"
ZMAGA, PORAZ = 'w', 'x'

class Vislice:
    def __init__(self):
        self.igre = {}
        self.max_id = 0

    def prost_id_igre(self):
        self.max_id += 1
        return self.max_id

    """ Druga možnost:
    def prost_id_igre_drugace(self):
        if not self.igre: return 0
        m = max(self.igre.keys())
        return m + 1 
    Če je self.igre prazen, to ne deluje,
    zato smo dodali prvo vrstico.
    """

    def nova_igra(self):
        nov_id = self.prost_id_igre()
        sveza_igra = nova_igra(bazen_besed)

        self.igre[nov_id] = (sveza_igra, ZACETEK)

        return nov_id

    def ugibaj(self, id_igre, crka):
        #Najdi
        #Trenutno stanje nas ne zanima
        igra, _ = self.igre[id_igre]
        #Posodobi z delegiranjem
        novo_stanje = igra.ugibaj(crka)
        #Popravi v slovarju
        self.igre[id_igre] = (igra, novo_stanje)

        return novo_stanje

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        self.crke = crke or list()

    def napacne_crke(self):
        return [c for c in self.crke if c.upper() not in self.geslo.upper()]

    def pravilne_crke(self):
        return [c for c in self.crke if c.upper() in self.geslo.upper()]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def zmaga(self):
        return not self.poraz() and len(set(self.pravilne_crke())) == len(set(self.geslo))

    def pravilni_del_gesla(self):
        pravilno = ' '
        for c in self.geslo.upper():
            if c in self.crke:
                pravilno += c
            else:
                pravilno += '_'
        return pravilno

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka in self.geslo.upper():
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            self.crke.append(crka)
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA

with open('vislice/besede.txt') as f:
    bazen_besed = f.read().split()

import random

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo)  

        