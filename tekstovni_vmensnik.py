from model import Miza
from model import preveriAliObstajaMiza
from model import preglejImenaIgralcev
from model import dodajMizo

prvaMiza = Miza(ime_mize='Kvartopirci', ime_1='Taroker', ime_2='Pagater', ime_3='Mondfanger', ime_4='Špilfarderber')

def dodaj_novo_mizo():
    print('Kako želite poimenovati svojo mizo?')
    ime_mize = input('> ')
    if preveriAliObstajaMiza(ime_mize) == True:
        print(f'Žal miza z imenom {ime_mize} že obstaja. Prosim, poskusite drugo ime. ')
    else:
        print(f'Ime mize je sprejemnljivo. Vaša miza se bo imenovala {ime_mize}.')
        print('Kako je ime igralcem? Prosim Vas, da se imena igralcev med seboj razlikujejo za vsaj en znak.')
        ime_igralca_1 = input('> Prvemu igralcu bo ime...')
        ime_igralca_2 = input('> Drugemu igralcu bo ime...')
        ime_igralca_3 = input('> Tretjemu igralcu bo ime...')
        ime_igralca_4 = input('> Četrtemu igralcu bo ime...')
        if preglejImenaIgralcev(ime_igralca_1, ime_igralca_2, ime_igralca_3, ime_igralca_4) == True:
            print(f'Imena so sprejemljiva. Vaša miza{ime_mize} ima igralce {ime_igralca_1}, {ime_igralca_2}, {ime_igralca_3}, {ime_igralca_4}.')
            dodajMizo(ime_mize, ime_igralca_1, ime_igralca_2, ime_igralca_3, ime_igralca_4)
            print('Uspešno ste dodali novo mizo')
        else:
            print('Imena se ponavljajo. Prosim izberite druga imena.')

def posodobi_podatke():
    print('Kako se imenuje vaša miza?')
    input('> ')
    
    pass

def poglej_dosedanje_rezultate():
    pass

def izhod():
    pass



def glavni_meni():
    print('Kaj želite storiti?')
    print('1) Dodaj novo mizo')
    print('2) Posodobi podatke')
    print('3) Poglej dosedanje rezultate ')
    print('4) Izhod')
    izbira = input('> ')
    if izbira == '1':
        dodaj_novo_mizo()
    elif izbira == '2':
        posodobi_podatke()
    elif izbira == '3':
        poglej_dosedanje_rezultate()
    elif izbira == '4':
        izhod()
    else:
        print ('Prosim izberite eno izmed podanih možnosti')






def main():
    print('Pozdravljeni v programu Tarok beležka.')

    while True:
        
        glavni_meni()
    




main()