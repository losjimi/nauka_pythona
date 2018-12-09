samochody=['maluch','syrenka','porsze','polojnezo']
lody=['bakaliowe','pistacjowe','jagodowe','czekoladowe','miodowe']


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

s='-'
print(s.join(lody)) #laczenie wartosci z listy

#ostatni element listy
print(lody[-1])
#pierwszy i ostatni
print(lody[0:-1])
