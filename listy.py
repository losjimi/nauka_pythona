samochody=['maluch','syrenka','porsze','polojnezo']
lody=['bakaliowe','pistacjowe','jagodowe','czekoladowe','miodowe']
ilosc=[1, 3, 5, 7]
litry=[3, 2, 6, 8, 99]
galki=[300, 200, 600, 800, 999]


print(samochody[0])

#for s in samochody:
#   print(s)

#wycinanie czesci listy
sublista = samochody[1:3]
# np od drugiego do konca to [2:]
print(sublista)

for idx in range(len(samochody)):
    print('index: ' + str(idx) + ' : ' + samochody[idx])

#print(litry[1] + litry[3])
print(lody[3])
for kolejnosc in range(len(lody)):
    print('Kolejnosc tworzenia lodow:' + str(kolejnosc) + ' i ich smak: ' + lody[kolejnosc])
#ostatni element listy
print(lody[-1])
#pierwszy i ostatni
print(lody[0:-1])


s='-'
print(s.join(lody)) #laczenie wartosci z listy
#lub print('-'.join(lody))
arr='a,b,c,d,e'.split(',')
print(arr)

#kasowanie pozycji del samochody[0]
#nadpisanie samochody[1] = 'kia'

#zad 11 samochody i ilosc_osob
for idx  in range(len(samochody)):
    print('idx: ' + str(idx) + ' : ' + samochody[idx])
    print (samochody[idx] + ' ma ilosc drzwi = ' + str(ilosc[idx]))
# doda zmiane nazwy litry za pomoca if
for a in range(len(lody)):
    print(str(a) + ' : ' + lody[a] + ' mamy ich az ' + str(litry[a]) + ' litrow. Wyjdzie z nich az ' + str(galki[a]) + ' galek')

# nowe zadanie koszyk
co=['jajka','bulki','mleko']
cena=[8.99, 0.20, 3.99]
koszyk=[1, 10, 3]
wartosc_koszyka=0.00
#ponizej zastosowanie dwoch ifow
#
for k in range(len(cena)):
    wartosc_koszyka = wartosc_koszyka + cena[k]
if wartosc_koszyka > 20:
    wartosc_koszyka=wartosc_koszyka-(wartosc_koszyka*0.3)
    print('30% znizki')
elif wartosc_koszyka > 13:
    wartosc_koszyka=wartosc_koszyka-(wartosc_koszyka*0.2)
    print('20% znizki')
print(wartosc_koszyka)
#co drugi produkt 0.00 zrobi w domu
