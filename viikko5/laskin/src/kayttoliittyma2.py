from enum import Enum
from tkinter import ttk, constants, StringVar
from laskut import Summa


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Kayttoliittyma:
    
<<<<<<< HEAD
=======

>>>>>>> 315908486f0da6004cd7ce0345406ca2f24b18dc
    def __init__(self, sovellus, root):
        
        self._sovellus = sovellus
        self._root = root
        
        self._komennot = {
            Komento.SUMMA: Summa(self._sovellus, Kayttoliittyma.resolvaa_komento())
        }

    @staticmethod
    def resolvaa_komento():
<<<<<<< HEAD
        return Kayttoliittyma.lue_syote()

    def kaynnista(self):
=======
        return self.lue_syote()

    def lue_syote(self):
        
        arvo = 0
        try:
            arvo = int(self._syote_kentta.get())
        except Exception:
            pass
        print(arvo)
        return arvo

    def kaynnista(self):
        self._syote_kentta = ttk.Entry(master=self._root)
>>>>>>> 315908486f0da6004cd7ce0345406ca2f24b18dc
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovellus.tulos)
        tulos_teksti = ttk.Label(textvariable=self._tulos_var)
        
        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
<<<<<<< HEAD
            command=lambda: self._suorita_komento(Komento.SUMMA) 
=======
            command=lambda: self._suorita_komento(Komento.SUMMA)
>>>>>>> 315908486f0da6004cd7ce0345406ca2f24b18dc
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)
    
<<<<<<< HEAD
    @staticmethod
    def lue_syote():
        arvo = 0
        try:
            arvo = int(self._syote_kentta.get())
        except Exception:
            pass
        print(arvo)
        return arvo
        
    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        komento_olio.suorita()
        
=======
    
        
    def _suorita_komento(self, komento):
        
        self.komento_olio = self._komennot[komento]
        self.komento_olio.suorita()
       
>>>>>>> 315908486f0da6004cd7ce0345406ca2f24b18dc
        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovellus.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovellus.tulos)
<<<<<<< HEAD
       
=======
        
>>>>>>> 315908486f0da6004cd7ce0345406ca2f24b18dc
    """ def _suorita_komento(self, komento):
        arvo = 0

        try:
            arvo = int(self._syote_kentta.get())
        except Exception:
            pass

        if komento == Komento.SUMMA:
            self._sovellus.plus(arvo)
        elif komento == Komento.EROTUS:
            self._sovellus.miinus(arvo)
        elif komento == Komento.NOLLAUS:
            self._sovellus.nollaa()
        elif komento == Komento.KUMOA:
            pass

        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovellus.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovellus.tulos) """
