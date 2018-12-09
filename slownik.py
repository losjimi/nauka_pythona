samolot ={  'nazwa': ' boing',
            'przebieg': '200',
            'typ': 'pasazerski'}
#dla klucza zwraca wartosc
print(samolot['nazwa'])
print(samolot['typ'])
print('')
# dla pythona 3
for key, value in samolot.iteritems():
    print('{0}:{1}'.format(key, value))
# dla starszych pythonow
for key in samolot:
    print('{0}:{1}'.format(key, samolot[key]))

# wyrzuci blad - print(samolot['aaa'])
print('')
print('')
# lista ktorej elementami jest slownik

koszyk = [  {'nazwa': 'mleko','cena': '5.20'},
            {'nazwa': 'bulka', 'cena': '0.20'},
            {'nazwa': 'ziemniaki', 'cena': '1.60'}]
suma=0
for a in range(len(koszyk)):
    print(koszyk[a]['cena'])
    suma = suma + float(koszyk[a]['cena'])

print(str(suma))
