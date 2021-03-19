from tkinter import Tk
from kayttoliittyma2 import Kayttoliittyma
from sovelluslogiikka import Sovelluslogiikka
from summa import Summa


def main():
    sovellus = Sovelluslogiikka()

    window = Tk()
    window.title("Laskin")

    kayttoliittyma = Kayttoliittyma(sovellus, window)
    kayttoliittyma.kaynnista()

    window.mainloop()

if __name__ == "__main__":
    main()
