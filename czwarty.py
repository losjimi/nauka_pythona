rodzaj_wypoczynku='kino'
cena_normalna=25.00
cena_ulgowa=18.00
ilosc_osob=3
wiek_1=30
wiek_2=25
wiek_3=16

print('Dzisiaj bedziemy odpoczywac. Wybralismy rodzaj zabawy '
+ rodzaj_wypoczynku + '. Idziemy w ' + str(ilosc_osob) + ' osob.')

if (wiek_1 >= 18 and wiek_2 >= 18 and wiek_3 >= 18):
    print('Za bilety zaplacimy ' + str(cena_normalna*3))
elif ((wiek_1 >= 18 and wiek_2 >= 18 and wiek_3 < 18) or (wiek_1 >= 18 and wiek_2 < 18 and wiek_3 >= 18) or (wiek_1 < 18 and wiek_2 >= 18 and wiek_3 >= 18)):
    print('Za bilety zaplacimy ' + str(cena_normalna*2+cena_ulgowa))
elif ((wiek_1 >= 18 and wiek_2 < 18 and wiek_3 < 18) or (wiek_1 < 18 and wiek_2 < 18 and wiek_3 >= 18) or (wiek_1 < 18 and wiek_2 >= 18 and wiek_3 < 18)):
    print('Za bilety zaplacimy ' + str(cena_normalna+cena_ulgowa*2))
elif (wiek_1 < 18 and wiek_2 < 18 and wiek_3 < 18):
    print('Za bilety zaplacimy ' + str(cena_ulgowa*3))
