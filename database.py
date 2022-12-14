from pojistenec import Pojistenec


class Databaze:
    """
    třída reprezentující všechy pojištěnce v databázi a operace s nimi
    """

    pojistenci = []

    def zalozit_pojistence(self):
        """
        metoda sloužící k založení nového pojištěnce do databáze
        """

        novy_pojistenec = Pojistenec()

        novy_pojistenec.jmeno = input("Zadejte jméno pojištěného:\n")
        novy_pojistenec.prijmeni = input("Zadejte příjmení pojištěného:\n")
        novy_pojistenec.tel_cislo = input("Zadejte telefonní číslo:\n")
        novy_pojistenec.vek = input("Zadejte věk:\n")

        self.pojistenci.append(novy_pojistenec)

    def vypsat_vsechny_pojistence(self):
        """
        metoda sloužící k vypsání všech pojištěnců uložených v databázi
        """

        for prvek in self.pojistenci:
            print(prvek)

    def vyhledat_pojistence(self):
        """
        metoda, která vyhledá na základě jména a příjmení konkrétního pojištěnce uloženého v databázi,
        ošetřena situace kdy se jméno a příjmení neshoduje s údaji v databázi
        """

        spatne = True
        while spatne:
            jmeno = input("Zadejte jméno pojištěného:\n")
            prijmeni = input("Zadejte příjmení pojištěného:\n")
            vyhledana_osoba = [osoba for osoba in self.pojistenci if (osoba.jmeno == jmeno)
                               and (osoba.prijmeni == prijmeni)]
            if vyhledana_osoba:
                for prvek in vyhledana_osoba:
                    print(prvek)
                return True
            else:
                self.dalsi_pozadavek("Osoba není v databázi! Zkuste to znovu po stisknutí klávesy 'y'.\n")
        else:
            return False

    def nacti_cislo(self, text_zadani, text_chyba):
        """
        metoda pro načtení čísla (použito při volbě operace), ošetřeno chybné zadání
        """

        global cislo
        spatne = True
        while spatne:
            try:
                cislo = int(input(text_zadani))
                spatne = False
            except ValueError:
                print(text_chyba)
        else:
            return cislo

    def dalsi_pozadavek(self, text):
        """
        metoda pro možnost zadat další požadavek či ukončit program, ošetřeno chybné zadání
        """

        pokracovat = True
        while pokracovat:
            odpoved = input(text)
            if odpoved == "y" or odpoved == "Y":
                return True
            elif odpoved == "n" or odpoved == "N":
                return False
            else:
                print("Chybná volba!")

    def volba(self):
        """
        metoda pro volbu požadované operace
        """

        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec")

        volba = self.nacti_cislo("Vaše volba:\n", "Chybná volba!")

        if volba == 1:
            self.zalozit_pojistence()

        if volba == 2:
            self.vypsat_vsechny_pojistence()

        if volba == 3:
            self.vyhledat_pojistence()

        if volba == 4:
            print("KONEC")

    def main(self):
        """
        motoda pro hlavní cyklus (volba operace, další požadavek) + zobrazení základní obrazovky
        """

        print("----------------------")
        print("Evidence pojištěných")
        print("----------------------")
        print("Vyberte si akci:")

        znovu = True
        while znovu:
            self.volba()
            if self.dalsi_pozadavek("\nPřejete si zadat další požadavek? y / n\n"):
                znovu = True
            else:
                znovu = False
        else:
            print("KONEC")
