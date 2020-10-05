slovar_iger = {'tri': 10, 'dve': 20, 'ena': 30, 'solo tri': 40, 'solo dve': 50, 'solo ena': 60, 'pikolo berač': 60, 'berač': 70, 'solo brez': 80, 'klop': 0, 'bar.valat_tri': 100, 'bar.valat_dve': 110, 'bar.valat_ena': 120, 'bar.valat_solo-tri': 125, 'bar.valat_solo-dve': 150, 'bar.valat_solo-ena': 175, 'bar.valat_solo-brez': 250, 'valat_tri':200, 'valat_dve':220, 'valat_ena':240, 'valat_solo-tri':250, 'valat_solo-dve':300, 'valat_solo-ena':350, 'valat_solo_brez':500}
slovar_bonusov = {'kralji': 10, 'trula': 10, 'pagat ultimo': 25,'kralj ultimo': 10, 'valat': 50}


class Igralec:

    def __init__(self, ime, tocke=0, radelci=0):
        self.tocke = tocke
        self.radelci = radelci
        self.ime = ime


    def dodaj_tocke(self, tocke):
        self.tocke += tocke

    def dodaj_radelc(self):
        self.radelci += 1

    def mondfang(self):
        self.tocke -= 21

    def preveriRadelc(self):
        if self.radelci == 0:
            return True
        else: 
            return False

    def porabiRadelc(self):
        if preveriRadelc() is False:
            self.radelci -= 1
        else:
            pass
class Miza:


    def __init__(self, ime_mize, ime_1, ime_2, ime_3, ime_4): 
        self.ime = ime_mize
        self.igralec_1 = Igralec(ime_1)
        self.igralec_2 = Igralec(ime_2)
        self.igralec_3 = Igralec(ime_3)
        self.igralec_4 = Igralec(ime_4)
        
    

    def poisciIgralca(self, ime):
        for igralec in [self.igralec_1, self.igralec_2, self.igralec_3, self.igralec_4]:
            if igralec.ime == ime:
                return igralec
        return None

    #def dodaj_mizo(self, ime_mize, ime_igralca_1, ime_igralca_2, ime_igralca_3, ime_igralca_4):
    #    seznam_vseh_miz[ime_mize] = Miza(ime_mize, ime_igralca_1, ime_igralca_2, ime_igralca_3, ime_igralca_4)



def vrniSteviloRadelcev(ime_mize, ime_igralca):
    return mize[ime_mize].poisciIgralca(ime_igralca).radelci


def vrniSteviloTock(ime_mize, ime_igralca):
    return mize[ime_mize].poisciIgralca(ime_igralca).tocke




def dodajMizo(ime_mize, ime_1, ime_2, ime_3, ime_4):
        mize[ime_mize] = Miza(ime_mize, ime_1, ime_2, ime_3, ime_4)


def točkeOdIgre(igra, razlika):
    return slovar_iger[igra] + razlika


def bonusTočke(bonus):
    return slovar_bonusov[bonus]


def preveriAliObstajaMiza(ime_mize):
        if ime_mize in mize:
            return True
        else:
            return False


def preveri_ali_obstaja_igralec(ime_mize, ime_igralca):
        if preveriAliObstajaMiza(ime_mize) == True:
            miza = mize[ime_mize]
            seznam_igralcev = seznamIgralcev(ime_mize)
            while len(seznam_igralcev) > 0:
                if seznam_igralcev[0] == ime_igralca:
                    return True
                else:
                    seznam_igralcev = seznam_igralcev[1:]
            return False
        else:
            print(f'Miza z imenom {ime_mize} še ne obstaja.')


def seznamIgralcev(ime_mize):
    if preveriAliObstajaMiza(ime_mize) == True:
        miza = mize[ime_mize]
        ime_1 = miza.igralec_1.ime
        ime_2 = miza.igralec_2.ime
        ime_3 = miza.igralec_3.ime
        ime_4 = miza.igralec_4.ime
        return [ime_1, ime_2, ime_3,ime_4 ]
    else:
        print(f'Miza z imenom {miza.ime_mize} še ne obstaja.' )



def preglejImenaIgralcev(ime_1, ime_2, ime_3, ime_4):
    seznam_igralcev = [ime_1, ime_2, ime_3, ime_4]
    množica_imen = set(seznam_igralcev)
    if len(množica_imen) < 4:
        return False
    else: 
        return True



def izpisiSeznamIgralcev(ime_mize, seznam_igralcev):
    print (f'Za mizo {ime_mize} sedijo {ime_1}, {ime_2}, {ime_3} in {ime_4}. ' )

mize = {}

#nova = dodajMizo('nova', 'anže', 'jurij', 'matic', 'gal')

#druga = dodajMizo('druga', 'tilen', 'klemen', 'jani', 'bojan')
#
#tretja = Miza('tretja_miza', 'gašper', 'tim', 'nik', 'leon')
#
#preveri_za_četrto = preveriAliObstajaMiza('četrta')
#
#
#
#preveriAliObstajaMiza('druga')
#
#igralci_za_drugo_mizo = seznamIgralcev('nova')
#
#
##preveri_ali_obstaja_igralec('druga', 'jani')
#haha = preveri_ali_obstaja_igralec('druga', 'štruci')
#
#t = vrniSteviloRadelcev('druga', 'bojan')
#print('vse je šlo v redu')