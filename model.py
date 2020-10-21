import json
slovar_iger = {'tri': 10, 'dve': 20, 'ena': 30, 'solo tri': 40, 'solo dve': 50, 'solo ena': 60, 'solo brez': 80, 'pikolo berač': 60, 'berač': 70}
barvni_valati = {'barvni valat tri': 100, 'barvni valat dve': 110, 'barvni valat ena': 120, 'barvni valat solotri': 125, 'barvni valat solo dve': 150, 'barvni valat solo ena': 175, 'bar valat solo brez': 250}
valat = {'valat tri': 200, 'valat dve': 220, 'valat ena': 240, 'valat solo tri': 250, 'valat solo dve': 300, 'valat solo ena': 350, 'valat solo brez': 500}
slovar_bonusov = {'kralji': 10, 'trula': 10, 'pagat ultimo': 25, 'kralj ultimo': 10, 'valat': 50}


class Igralec:

    def __init__(self, ime, tocke=0, radelci=0):
        self.tocke = tocke
        self.radelci = radelci
        self.ime = ime

    def posodobi_tocke(self, tocke, mat):
        if self.porabi_radelc(mat):
            self.dodaj_tocke(tocke*2)
            print(f'Igralec {self.ime} je prejel {tocke*2} točk.')
        else:
            self.dodaj_tocke(tocke)
            print(f'Igralec {self.ime} je prejel {tocke} točk.')

    def dodaj_tocke(self, tocke):
        self.tocke += tocke

    def dodaj_radelc(self):
        self.radelci += 1

    def mondfang(self):
        self.tocke -= 21

    def preveri_radelc(self):
        if self.radelci == 0:
            return True
        else:
            return False

    def porabi_radelc(self, mat):
        if self.preveri_radelc() is False:
            if mat == 1:
                self.radelci -= 1
                print(f'Igralec {self.ime} je porabil en radelc')
            return True
        else:
            return False

    def podatki_o_igralcu(self):
        slovar_podatkov = {}
        slovar_podatkov['ime igralca'] = self.ime
        slovar_podatkov['točke igralca'] = self.tocke
        slovar_podatkov['radelci igralca'] = self.radelci
        return slovar_podatkov

    def posodobi_igralca(self, slovar):
        self.tocke = slovar['točke igralca']
        self.radelci = slovar['radelci igralca']


class Miza:

    def __init__(self, ime_mize, ime_1, ime_2, ime_3, ime_4):
        self.ime = ime_mize
        self.igralec_1 = Igralec(ime_1)
        self.igralec_2 = Igralec(ime_2)
        self.igralec_3 = Igralec(ime_3)
        self.igralec_4 = Igralec(ime_4)

    def poisci_igralca(self, ime):
        for igralec in [self.igralec_1, self.igralec_2, self.igralec_3, self.igralec_4]:
            if igralec.ime == ime:
                return igralec
        return None

    def podatki_o_mizi(self):
        slovar = {}
        slovar['ime mize'] = self.ime
        slovar['igralec 1'] = self.igralec_1.podatki_o_igralcu()
        slovar['igralec 2'] = self.igralec_2.podatki_o_igralcu()
        slovar['igralec 3'] = self.igralec_3.podatki_o_igralcu()
        slovar['igralec 4'] = self.igralec_4.podatki_o_igralcu()
        return slovar

    def posodobi_točke_radelce(self, igralec_1, igralec_2, igralec_3, igralec_4):
        self.igralec_1.posodobiIgralca(igralec_1)
        self.igralec_2.posodobiIgralca(igralec_2)
        self.igralec_3.posodobiIgralca(igralec_3)
        self.igralec_4.posodobiIgralca(igralec_4)


def dodaj_mizo(ime_mize, ime_1, ime_2, ime_3, ime_4):
    miza = Miza(ime_mize, ime_1, ime_2, ime_3, ime_4)
    objekti_Miza[miza.ime] = miza


def slovar_igralca(slovar):
    ime_igralca = slovar['ime igralca']
    tocke_igralca = slovar['točke igralca']
    radelci_igralca = slovar['radelci igralca']
    return Igralec(ime_igralca, tocke_igralca, radelci_igralca)


def vrni_stevilo_radelcev(ime_mize, ime_igralca):
    miza = poisci_mizo(ime_mize)
    igralec = miza.poisci_igralca(ime_igralca)
    return igralec.radelci


def vrni_stevilo_tock(ime_mize, ime_igralca):
    miza = poisci_mizo(ime_mize)
    igralec = miza.poisci_igralca(ime_igralca)
    return igralec.tocke


def točke_od_igre(igra, razlika):
    return slovar_iger[igra] + razlika


def bonus_točke(bonus):
    return slovar_bonusov[bonus]


def seznam_imen_miz():
    mnozica = set()
    slovar = objekti_Miza
    for miza in slovar:
        iskana = objekti_Miza.get(miza)
        mnozica.add(iskana.ime)
    return mnozica


def preveri_ali_obstaja_miza(ime_mize):
        mnozica = seznam_imen_miz()
        return ime_mize in mnozica


def vrzi_vkup(igra, slovar_iger, razlika, napovedi, realizacije, mat):
    seznam = seznam_tock(slovar_iger)
    točke_igra = seznam[igra - 1] * mat
    točke_igra = točke_igra + razlika
    bonusi = racunaj_bonuse(napovedi, realizacije)
    tocke = točke_igra + bonusi
    return tocke


def posodobi_radelc(ime_mize, ime_igralca, slovarIger, igra):
    if igra > 6 or slovarIger is not slovar_iger:
        miza = poisci_mizo(ime_mize)
        miza.igralec_1.radelci += 1
        miza.igralec_2.radelci += 1
        miza.igralec_3.radelci += 1
        miza.igralec_4.radelci += 1
        print(f'Vsi igralci mize {ime_mize} so prejeli radelc.')
    else:
        pass


def racunaj_bonuse(napovedi, realizacije):
    tocke = 0
    i = 0
    r = 1
    for napoved in napovedi:
        if napoved == 1 and realizacije[i] == 1:
            r = 2
        elif napoved == 1 and realizacije[i] == 0:
            r = -2
        elif napoved == 0 and realizacije[i] == 1:
            r = 1
        else:
            r = 0
        tocke += seznam_tock(slovar_bonusov)[i] * r
        i += 1
    return tocke


def dodaj_tocke_igri(ime_igralec, ime_soigralec, ime_miza, tocke, mat):
    miza = objekti_Miza[ime_miza]
    igralec = miza.poisci_igralca(ime_igralec)
    soigralc = miza.poisci_igralca(ime_soigralec)
    if soigralc is None:
        pass
    else:
        soigralc.dodaj_tocke(tocke)
        print(f'Soigralec {ime_soigralec} je prejel {tocke} točk.')
    igralec.posodobi_tocke(tocke, mat)


def preveri_ali_obstaja_igralec(ime_mize, ime_igralca):
        if preveri_ali_obstaja_miza(ime_mize):
            miza = poisci_mizo(ime_mize)
            seznam_igralcev = seznam_igralcev(ime_mize)
            while len(seznam_igralcev) > 0:
                if seznam_igralcev[0] == ime_igralca:
                    return True
                else:
                    seznam_igralcev = seznam_igralcev[1:]
            return False
        else:
            print(f'Miza z imenom {ime_mize} še ne obstaja.')


def poisci_mizo(ime_mize):
    return objekti_Miza.get(ime_mize)


def seznam_igralcev(ime_mize):
    if preveri_ali_obstaja_miza(ime_mize):
        miza = objekti_Miza.get(ime_mize)
        ime_1 = miza.igralec_1.ime
        ime_2 = miza.igralec_2.ime
        ime_3 = miza.igralec_3.ime
        ime_4 = miza.igralec_4.ime
        return [ime_1, ime_2, ime_3, ime_4]
    else:
        print(f'Miza z imenom {ime_mize} še ne obstaja.')


def preglej_imena_igralcev(ime_1, ime_2, ime_3, ime_4):
    # PReverimo, da so imena res različna
    # Če niso različna ne moremo vedeti kdo igra
    seznam_igralcev = [ime_1, ime_2, ime_3, ime_4]
    množica_imen = set(seznam_igralcev)
    if len(množica_imen) < 4:
        return False
    else:
        return True


def ustvari_mizo(slovar):
    podatki = slovar
    ime_mize = podatki['ime mize']
    igralec_1 = podatki['igralec 1']
    igralec_2 = podatki['igralec 2']
    igralec_3 = podatki['igralec 3']
    igralec_4 = podatki['igralec 4']
    miza = Miza(ime_mize, igralec_1['ime igralca'], igralec_2['ime igralca'], igralec_3['ime igralca'], igralec_4['ime igralca'])
    miza.posodobiTočkeRadelce(igralec_1, igralec_2, igralec_3, igralec_4)
    objekti_Miza[miza.ime] = miza


def nalozi_stanje(ime_datoteke):
        with open(ime_datoteke, encoding='UTF-8') as datoteka:
            slovar_stanja = json.load(datoteka)
        for miza in slovar_stanja:
            slovar_mize = slovar_stanja[miza]
            ustvari_mizo(slovar_mize)


def naredi_seznam(napoved):
    sez = list(napoved)
    nabor = [0, 0, 0, 0, 0]
    for st in sez:
        stevilo = int(st) - 1
        nabor[stevilo] = 1
    stevke = tuple(nabor)
    return stevke


def seznam_tock(slovar):
    return list(slovar.values())


def zapisi_mize(ime_datoteke):
        for mizica in objekti_Miza:
            slovar = objekti_Miza.get(mizica)
            zapisi = slovar.podatki_o_mizi()
            slovar_za_JSON[mizica] = zapisi

        with open(ime_datoteke, 'w', encoding='UTF-8') as datoteka:
            json.dump(slovar_za_JSON, datoteka, ensure_ascii=False, indent=4)


objekti_Miza = dict()


slovar_za_JSON = {}
