rodzaj_wypoczynku='kino'
cena_normalna=25.00
cena_ulgowa=18.00
ilosc_osob=3
wiek_1=30
wiek_2=25
wiek_3=16
dzien='Sobota'

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


#if 18.00<cena_normalna<=25.00:
if dzien.startswith('So'):
    print('Promocja sobotnia 20%! ')
    cena_normalna= cena_normalna-cena_normalna*0.2
    print('Bilet w promocji: ' + str(cena_normalna))
elif dzien.startswith('N'):
    print('Promocja sobotnia 30%! ')
    cena_normalna= cena_normalna-cena_normalna*0.3
    print('Bilet w promocji: ' + str(cena_normalna))
else:
    print('Bilety w cenie standard - dzis nie Sobota ani Niedziela')
