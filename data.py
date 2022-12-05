class Databaze:

    jmeno = []
    prijmeni = []
    tel_cislo = []
    vek = []

    def __int__(self, jmeno, prijmeni, tel_cislo, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.tel_cislo = tel_cislo
        self.vek = vek

    def __str__(self):
        return str("\n{0}\t{1}\t{2}\t\t{3}".format(self.jmeno,
                                                   self.prijmeni,
                                                   self.vek,
                                                   self.tel_cislo))

    def nacti_cislo(self, text_zadani, text_chyba):
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
        pokracovat = True
        while pokracovat:
            odpoved = input(text)
            if odpoved == "y":
                return True
            elif odpoved == "n":
                return False
            else:
                print("Chybná volba!")

    def volba(self):

        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec")

        volba = self.nacti_cislo("Vaše volba: ", "Chybná volba!")

        if volba == 1:
            print("Zadejte křestní jméno:")
            self.jmeno.append(input())
            print("Zadejte příjmení:")
            self.prijmeni.append(input())
            print("Zadejte telefonní číslo:")
            self.tel_cislo.append(input())
            print("Zadejte věk:")
            self.vek.append(input())
            print("Data byla uložena!")

        elif volba == 2:
            i = 0
            while i < len(self.jmeno):
                print("\n{0}\t{1}\t{2}\t\t{3}".format(self.jmeno[i].ljust(10),
                                                      self.prijmeni[i].ljust(15),
                                                      self.vek[i],
                                                      self.tel_cislo[i]), end="")
                i += 1
            else:
                print("")

        elif volba == 3:
            spatne = True
            while spatne:
                a = input("Zadejte jméno pojištěného:\n")
                b = input("Zadejte příjmení pojištěného:\n")
                if (a in self.jmeno) and (b in self.prijmeni):
                    position = self.prijmeni.index(b)
                    print("\n{0}\t{1}\t{2}\t\t{3}".format(self.jmeno[position].ljust(10),
                                                          self.prijmeni[position].ljust(15),
                                                          self.vek[position],
                                                          self.tel_cislo[position]))
                    return True
                else:
                    self.dalsi_pozadavek("Osoba není v databázi! Zkuste to znovu po stisknutí klávesy 'y'.\n")
            else:
                return False

        elif volba == 4:
            print("KONEC")

        elif volba > 4 or volba < 1:
            print("Chybná volba!")

    def main(self):
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
