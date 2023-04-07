# IF
piesa_faina = True

print("pornim radio")
if piesa_faina==True:
    print('dau mai tare')
    print('fredonam')

print('oprim radio')


#if else
# daca numarul este par printam acest lucru
# altfel printam impar

nr = 3
# ce inseamna par? se imparte exact la 2
# ce inseamna ca se imparte la 2? ne da restul 0
if nr % 2  == 0:
    print('nr par')
else:
    print('impar')

# este un numar pozitiv?
if(nr >0):
    print('pozitiv')
else:
    print('nr nu este pozitiv')
# if, else if, else
# cum ne saluta robotelul in functie de ora?
#ne asiguram ca sunt  transformate din str in int
ora = int(input('introdu ora'))
if ora < 0:
    print('ora invalida.ora negativa')
elif ora <=11:
    print('buna dimineata')
elif ora <=18:
    print('buna ziua')
elif ora <=21:
    print ('buna seara')
elif ora <= 24:
    print('noapte buna')
else:
    print('ora invalida.ora mai mare decat 24')

#robotel telefonic
optiune= int(input('alege o optiune'))
if optiunea == 0:
    print('meniu anterior')
elif optiunea == 1:
    print('ati ales ro')
elif optiunea ==2:
    prrint('ati ales eng')
else:
    print('nu am identificat optiunea, mai incearca')

