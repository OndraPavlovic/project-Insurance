class Pojistenec:
    """
    třída reprezentující konkrétního pojištěnce, zadáváme jméno, příjmení, tel. číslo a věk
    """

    def __int__(self, jmeno, prijmeni, tel_cislo, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.tel_cislo = tel_cislo
        self.vek = vek

    def __str__(self):
        return str("{0}\t{1}\t{2}\t\t{3}".format(self.jmeno.ljust(10),
                                                 self.prijmeni.ljust(15),
                                                 self.vek,
                                                 self.tel_cislo))

