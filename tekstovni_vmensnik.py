from model import Miza

prvaMiza = Miza(ime_mize='Kvartopirci', ime_1='Taroker', ime_2='Pagater', ime_3='Mondfanger', ime_4='Špilfarderber')

def dodaj_novo_mizo():
    print('Uspešno ste dodali novo mizo')

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