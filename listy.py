samochody=['maluch','syrenka','porsze','polojnezo']
lody=['bakaliowe','pistacjowe','jagodowe','czekoladowe','miodowe']
ilosc=[1, 3, 5, 7]
litry=[3, 2, 6, 8, 99]


print(samochody[0])

#for s in samochody:
#   print(s)

#wycinanie czesci listy
sublista = samochody[1:3]
# np od drugiego do konca to [2:]
print(sublista)

for idx in range(len(samochody)):
    print('index: ' + str(idx) + ' : ' + samochody[idx])


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

for a in range(len(lody)):
    print(str(a) + ' : ' + lody[a] + ' mamy ich az ' + str(litry[a]) + ' litrow.')
