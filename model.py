slovar_iger = {'tri': 10, 'dve': 20, 'ena': 30, 'solo tri': 40, 'solo dve': 50, 'solo ena': 60, 'pikolo berač': 60, 'berač': 70, 'solo brez': 80, 'klop': 0, 'bar.valat_tri': 100, 'bar.valat_dve': 110, 'bar.valat_ena': 120, 'bar.valat_solo-tri': 125, 'bar.valat_solo-dve': 150, 'bar.valat_solo-ena': 175, 'bar.valat_solo-brez': 250, 'valat_tri':200, 'valat_dve':220, 'valat_ena':240, 'valat_solo-tri':250, 'valat_solo-dve':300, 'valat_solo-ena':350, 'valat_solo_brez':500}
slovar_bonusov = {'kralji': 10, 'trula': 10, 'pagat ultimo': 25,'kralj ultimo': 10, 'valat': 50}
import json



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

    def podatkiOIgralcu(self):
        slovar_podatkov = {}
        slovar_podatkov['ime igralca'] = self.ime
        slovar_podatkov['točke igralca'] = self.tocke
        slovar_podatkov['radelci igralca'] = self.radelci
        return slovar_podatkov

    def posodobiIgralca(self, slovar):
        self.tocke = slovar['točke igralca']
        self.radelci = slovar['radelci igralca']
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


    def podatkiOMizi(self):
        slovar = {}
        slovar['ime mize'] = self.ime
        slovar['igralec 1'] = self.igralec_1.podatkiOIgralcu()
        slovar['igralec 2'] = self.igralec_2.podatkiOIgralcu()
        slovar['igralec 3'] = self.igralec_3.podatkiOIgralcu()
        slovar['igralec 4'] = self.igralec_4.podatkiOIgralcu()
        return slovar


    def posodobiTočkeRadelce(self, igralec_1, igralec_2, igralec_3, igralec_4):
        self.igralec_1.posodobiIgralca(igralec_1)
        self.igralec_2.posodobiIgralca(igralec_2)
        self.igralec_3.posodobiIgralca(igralec_3)
        self.igralec_4.posodobiIgralca(igralec_4)
        
    

class Belezka:

    def __init__(self, ime_mize, ime_1, ime_2, ime_3, ime_4):
        self.miza = Miza(ime_mize, ime_1, ime_2, ime_3, ime_4)
        self.ime = ime_mize

    def zapisiBelezko(self, ime_datoteke):
        slovar_mize = {}
        slovar_mize = self.miza.podatkiOMizi()
        print(slovar_mize)
        
        with open(ime_datoteke, 'w') as datoteka:
            json.dump(slovar_mize, datoteka, ensure_ascii=False, indent=4)

#    @classmethod
#    def nalozi_stanje(cls, ime_datoteke):
#        with open(ime_datoteke) as datoteka:
#            slovar_stanja = json.load(datoteka)
#        posodobljena_miza = ustvariMizo(slovar_stanja)
#        return Belezka()
            

def slovarIgralca(slovar):
    ime_igralca = slovar['ime igralca']
    tocke_igralca = slovar['točke igralca']
    radelci_igralca = slovar['radelci igralca']
    return Igralec(ime_igralca, tocke_igralca, radelci_igralca)


def vrniSteviloRadelcev(ime_mize, ime_igralca):
    miza = objekti_Miza[poisciMizo(ime_mize)]
    igralec = miza.poisciIgralca(ime_igralca)
    return igralec.radelci

def vrniSteviloTock(ime_mize, ime_igralca):
    miza = objekti_Miza[poisciMizo(ime_mize)]
    igralec = miza.poisciIgralca(ime_igralca)
    return igralec.tocke


def točkeOdIgre(igra, razlika):
    return slovar_iger[igra] + razlika

def bonusTočke(bonus):
    return slovar_bonusov[bonus]

def seznamImenMiz():
    mnozica = set()
    seznam = objekti_Miza
    for miza in seznam:
        mnozica.add(miza.ime_mize)
    return mnozica
    

def preveriAliObstajaMiza(ime_mize):
        mnozica = seznamImenMiz()
        return ime_mize in mnozica
    
        
def preveri_ali_obstaja_igralec(ime_mize, ime_igralca):
        if preveriAliObstajaMiza(ime_mize) == True:
            miza = poisciMizo(ime_mize)
            seznam_igralcev = seznamIgralcev(ime_mize)
            while len(seznam_igralcev) > 0:
                if seznam_igralcev[0] == ime_igralca:
                    return True
                else:
                    seznam_igralcev = seznam_igralcev[1:]
            return False
        else:
            print(f'Miza z imenom {ime_mize} še ne obstaja.')

def poisciMizo(ime_mize):
    if not ime_mize in seznamImenMiz:
        print('miza s tem imenon ne obstaja!!!')
    else:
        i = 0
        for miza in objekti_Miza:
            if miza[i].ime_mize == ime_mize:
                return i
            else:
                i += 1
        

def seznamIgralcev(ime_mize):
    if preveriAliObstajaMiza(ime_mize) == True:
        miza = objekti_Miza[ime_mize]
        ime_1 = miza.igralec_1.ime
        ime_2 = miza.igralec_2.ime
        ime_3 = miza.igralec_3.ime
        ime_4 = miza.igralec_4.ime
        return [ime_1, ime_2, ime_3, ime_4]
    else:
        print(f'Miza z imenom {ime_mize} še ne obstaja.' )

def preglejImenaIgralcev(ime_1, ime_2, ime_3, ime_4):
    seznam_igralcev = [ime_1, ime_2, ime_3, ime_4]
    množica_imen = set(seznam_igralcev)
    if len(množica_imen) < 4:
        return False
    else: 
        return True


def ustvariMizo(slovar):
    podatki = slovar
    ime_mize = podatki['ime mize']
    igralec_1 = podatki['igralec 1']
    igralec_2 = podatki['igralec 2']
    igralec_3 = podatki['igralec 3']
    igralec_4 = podatki['igralec 4']
    miza = Miza(ime_mize, igralec_1['ime igralca'], igralec_2['ime igralca'], igralec_3['ime igralca'], igralec_4['ime igralca'])
    miza.posodobiTočkeRadelce(igralec_1, igralec_2, igralec_3, igralec_4)
    objekti_Miza.append(miza)
     
def naloziMizo(ime_datoteke):
        with open(ime_datoteke) as datoteka:
            slovar_stanja = json.load(datoteka)
        posodobljena = ustvariMizo(slovar_stanja)
        return posodobljena

def nalozi_stanje(ime_datoteke):
        with open(ime_datoteke) as datoteka:
            slovar_stanja = json.load(datoteka)
        for miza in slovar_stanja:
            slovarMize = slovar_stanja[miza]
            ustvariMizo(slovarMize)
        

def zapisiMize(ime_datoteke):
        for mizica in objekti_Miza:
            slovar = mizica.podatkiOMizi()
            slovar_za_JSON[mizica.ime] = slovar
        
        with open(ime_datoteke, 'w') as datoteka:
            json.dump(slovar_za_JSON, datoteka, ensure_ascii=False, indent=4)        
  

objekti_Miza = []

slovar_za_JSON = {}

nalozi_stanje('belezka.json')

slovarJSON = {'ime mize': 'druga', 'igralec 1': {'ime igralca': 'tilen', 'točke igralca': 50, 'radelci igralca': 0}, 'igralec 2': {'ime igralca': 'klemen', 'točke igralca': 0, 'radelci igralca': 0}, 'igralec 3': {'ime igralca': 'jani', 'točke igralca': 0, 'radelci igralca': 0}, 'igralec 4': {'ime igralca': 'bojan', 'točke igralca': 0, 'radelci igralca': 0}}

NoviJohny = {'ime mize': 'deseta', 'igralec 1': {'ime igralca': 'miha', 'točke igralca': 50, 'radelci igralca': 0}, 'igralec 2': {'ime igralca': 'bugi', 'točke igralca': 0, 'radelci igralca': 0}, 'igralec 3': {'ime igralca': 'jurij', 'točke igralca': 0, 'radelci igralca': 0}, 'igralec 4': {'ime igralca': 'bomba', 'točke igralca': 0, 'radelci igralca': 0}}

seNovejsiJohny = {'ime mize': 'stota', 'igralec 1': {'ime igralca': 'bine', 'točke igralca': 50, 'radelci igralca': 0}, 'igralec 2': {'ime igralca': 'sara', 'točke igralca': 0, 'radelci igralca': 0}, 'igralec 3': {'ime igralca': 'tara', 'točke igralca': 0, 'radelci igralca': 0}, 'igralec 4': {'ime igralca': 'ema', 'točke igralca': 0, 'radelci igralca': 0}}


#ustvariMizo(NoviJohny)

#ustvariMizo(seNovejsiJohny)

#poskus = ustvariMizo(slovarJSON)

#poskus2 = ustvariMizo('tralala', 'brtbs', 'fsdgbvsd', 'edgs', 'sdgrsv')

#zapisiMize('belezka.json')

#print(slovar)

#Belezka('tretja', 'tine', 'matej', 'boštjan', 'andraž').zapisiBelezko('beležka.json')

#preveri_za_četrto = preveriAliObstajaMiza('četrta')

#preveriAliObstajaMiza('druga')
#
#igralci_za_drugo_mizo = seznamIgralcev('nova')
#
#
##preveri_ali_obstaja_igralec('druga', 'jani')
#haha = preveri_ali_obstaja_igralec('druga', 'štruci')
#
#t = vrniSteviloRadelcev('druga', 'bojan')
print('vse je šlo v redu')