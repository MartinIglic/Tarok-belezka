from model import Miza, preveriAliObstajaMiza, preglejImenaIgralcev, valat
from model import dodajMizo, objekti_Miza, slovar_za_JSON, seznamIgralcev
from model import slovar_bonusov, slovar_iger, barvni_valati, nalozi_stanje
from model import Igralec, vrziVkup, dodaj_tocke_igri, zapisiMize
from model import naredi_seznam, posodobi_radelc

navadne_igre = '''1)tri
2)dve
3)ena
4)solo tri
5)solo dve
6)solo ena
7)solo brez
8)pikolo berač
9)berač'''
seznam_bonusov = ['kralji', 'trula', 'pagat ultimo', 'kralj ultimo', 'valat']


def dodaj_novo_mizo():
    print('Kako želite poimenovati svojo mizo?')
    ime = input('> ')
    if preveriAliObstajaMiza(ime):
        print(f'Žal miza {ime} že obstaja. Prosim, poskusite drugo ime.')
    else:
        print(f'Ime mize je sprejemnljivo. Ime vaše mize je {ime}.')
        print('Kako je ime igralcem?')
        print('Imena igralcev naj se med seboj razlikujejo za vsaj en znak.')
        ime_1 = input('> Prvemu igralcu bo ime...')
        ime_2 = input('> Drugemu igralcu bo ime...')
        ime_3 = input('> Tretjemu igralcu bo ime...')
        ime_4 = input('> Četrtemu igralcu bo ime...')
        if preglejImenaIgralcev(ime_1, ime_2, ime_3, ime_4):
            print('Imena so sprejemljiva.')
            print(f'Za mizo {ime} so {ime_1}, {ime_2}, {ime_3}, {ime_4}.')
            dodajMizo(ime, ime_1, ime_2, ime_3, ime_4)
            print('Uspešno ste dodali novo mizo')
        else:
            print('Imena se ponavljajo. Prosim izberite druga imena.')


def posodobi_podatke():
    while True:
        print('Kako se imenuje vaša miza?')
        ime_mize = input('> ')
        if preveriAliObstajaMiza(ime_mize):
            print(f'Miza {ime_mize} sprejeta.')
            print('Ali ste igrali klopa?')
            print('1) Ja')
            print('2) Ne')
            odgovor = input('>')
            if odgovor == '1':
                zberiRezultateKlopa(ime_mize)
                break
            elif odgovor == '2':
                print('Kateri igralec je šel igrati?')
                seznam = ponudiIgralce(ime_mize)
                stevnik = input('> ')
                st = int(stevnik)
                ime_igralca = seznam[st - 1]
                igra = licitiranaIgra(ime_mize, ime_igralca)
                soigralc = soigralec(igra, ime_igralca, ime_mize)
                slovarIger = mordaValat(igra)
                raz = razlikaIgre(slovarIger, igra)
                mat = dobljena()
                napoved = seznamDodatkov(slovarIger, igra, 'napovedi')
                real = seznamDodatkov(slovarIger, igra, 'realizacije')
                tocke = vrziVkup(igra, slovarIger, raz, napoved, real, mat)
                dodaj_tocke_igri(ime_igralca, soigralc, ime_mize, tocke, mat)
                posodobi_radelc(ime_mize, ime_igralca, slovarIger, igra)
                print('Uspešno ste dodali točke.')
                break
            else:
                print('Prosim, pritisnite število 1 ali 2.')
        else:
            print('Miza s tem imenom ne obstaja. \nPoskusite drugo ime!')


def licitiranaIgra(ime, polnaRit):
    miza = objekti_Miza[ime]
    print(f'Kaj je šel {polnaRit} igrati?')
    return licitirajObično()


def licitirajObično():
    print(navadne_igre)
    indeks = input('> ')
    return int(indeks)


def soigralec(igra, ime, ime_mize):
    if igra < 4:
        print('Ali ste imeli soigralca?')
        print('1) Ja')
        print('2) Ne')
        odgovor = input('> ')
        if odgovor == '1':
            print('Koga ste klicali?')
            igralci = seznamIgralcev(ime_mize)
            ponudiIgralce(ime_mize)
            indeks = input('> ')
            ind = int(indeks)
            return igralci[ind - 1]
    else:
        return None


def mordaValat(igra):
    if igra <= 7:
        print('Ali ste igrali barvnega valata?')
        print('1) Ja')
        print('2) Ne')
        odgovor = input('> ')
        if odgovor == '1':
            return barvni_valati
        else:
            print('Ali ste igrali šli igrat navadnega valata?')
            print('1) Ja')
            print('2) Ne')
            morda = input('> ')
            if morda == '1':
                return valat
            else:
                return slovar_iger
    else:
        return slovar_iger


def razlikaIgre(slovarIger, igra):
    tocke = 0
    if slovarIger == slovar_iger and igra <= 6:
        while True:
            print('Koliko je bilo razlike?')
            razlika = input('> ')
            raz = int(razlika)
            if raz < 35:
                tocke += raz
                return tocke
            else:
                print('Vpisali ste preveliko razliko.')
                print('Razlika mora biti manjša od 35.')
    return tocke


def seznamDodatkov(slovarIger, igra, vrsta):
    seznam = []
    if slovarIger == slovar_iger and igra <= 6:
        print(f'Ali ste imeli {vrsta}?')
        print('1) Ja')
        print('2) Ne')
        morda = input('> ')
        if morda == '1':
            print(f'Napišite številke {vrsta}.')
            i = 1
            for napoved in seznam_bonusov:
                print(f'{i}){napoved}')
                i += 1
            napoved = input('> ')
            seznam = naredi_seznam(napoved)
            return seznam
        else:
            return (0, 0, 0, 0, 0)
    else:
        return (0, 0, 0, 0, 0)


def dobljena():
    print('Ali ste igro dobili ali izgubili?')
    print('1) Dobili.')
    print('2) Izgubili')
    while True:
        rez = input('> ')
        if rez == '1':
            return 1
        elif rez == '2':
            return -1
        else:
            print('Prosim vnesiti število ali 1 ali 2.')


def zberiRezultateKlopa(ime):
    miza = objekti_Miza[ime]
    seznam = seznamIgralcev(ime)
    for ime_igralec in seznam:
        igralec = miza.poisciIgralca(ime_igralec)
        print(f'Koliko točk je zbrala oseba {ime_igralec}?')
        tocke = input('> ')
        igralec.dodaj_tocke(-(int(tocke)))
        igralec.dodaj_radelc()
        print(f'Oseba {ime_igralec} je prejela {int(tocke)} točk.')
        print('Prejela je tudi en radelc.')
        print(f'{ime_igralec} ima {igralec.radelci} radelcev')
    print('Klop uspešno vnesen')


def ponudiIgralce(ime):
    miza = objekti_Miza[ime]
    igralci = seznamIgralcev(ime)
    i = 1
    for igralec in igralci:
        print(f'{i}) {igralec}')
        i += 1
    return igralci


def poglej_dosedanje_rezultate():
    print('Kako se imenuje vaša miza')
    while True:
        ime_mize = input('> ')
        if preveriAliObstajaMiza(ime_mize):
            miza = objekti_Miza[ime_mize]
            seznam = seznamIgralcev(ime_mize)
            for ime in seznam:
                igralec = miza.poisciIgralca(ime)
                rad = igralec.radelci
                toc = igralec.tocke
                print(f'Oseba {ime} ima {toc} točk')
                print(f'Oseba {ime} ima tudi {rad} neporabljenih radelcev.')
            print('Uspešno igro želim.')
            break
        else:
            print(f'Miza z imenom{ime_mize} še ne obstaja.')


def glavni_meni():
    while 1:
        zapisiMize('belezka.json')
        nalozi_stanje('belezka.json')
        printajGlavniMeni()
        izbira = input('>')
        if izbira == '1':
            dodaj_novo_mizo()
        elif izbira == '2':
            posodobi_podatke()
        elif izbira == '3':
            poglej_dosedanje_rezultate()
        elif izbira == '4':
            break
        else:
            print('Prosim izberite eno izmed podanih možnosti')


def printajGlavniMeni():
    print('Kaj želite storiti?')
    print('1) Dodaj novo mizo')
    print('2) Posodobi podatke')
    print('3) Poglej dosedanje rezultate ')
    print('4) Izhod')


def main():
    print('Pozdravljeni v programu Tarok beležka.')
    nalozi_stanje('belezka.json')
    while True:
        glavni_meni()
        zapisiMize('belezka.json')


main()
