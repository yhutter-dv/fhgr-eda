import numpy as np

"""
Berechnen Sie die numerischen Werte der folgenden Ausdrücke auf der Konsole:
12.45 - 4.33 + 1/7 – 11/65
(1 - 5.6/3) / 22.89 - 31.1
(7 - 11/3 + 2)**0.5
2**(-1.45) + 1
"""
result = 12.45 - 4.33 + 1/7 - 11/65
print(f"12.45 - 4.33 + 1/7 – 11/65 = {result}")

result = (1 - 5.6/3) / 22.89 - 31.1
print(f"(1 - 5.6/3) / 22.89 - 31.1 = {result}")

result = (7 - 11/3 + 2)**0.5
print(f"(7 - 11/3 + 2)**0.5 = {result}")

result = 2**(-1.45) + 1
print(f"2**(-1.45) + 1 = {result}")

"""
Es sei a = -1; b = 11/3 und c = -4. Berechnen Sie auf der Konsole
2a - b
(5a-1)/(7c-3a+5)
(b-a/3)/(2c-34)
(a-11/3c)**b
(a + 2)-1.45 + b/(c+1)
"""
a = -1
b = 11/3
c = -4

result = 2*a - b
print(f"2a - b = {result}")

result =(a-11/3*c)**b
print(f"(a-11/3c)**b = {result}")

result =(a + 2)-1.45 + b/(c+1)
print(f"(a + 2)-1.45 + b/(c+1) = {result}")

"""
Erzeugen Sie eine Liste a mit dem Inhalt 1, 4, 'also', 0.
- Schreiben Sie mittels Slicing das 1. und 2. element in eine Liste b.
- Schreiben Sie mittels Slicing das letzte element in eine Liste c.
- Erzeugen Sie eine Liste d in der hintereinander 2-mal der Inhalt von a und dann 2-mal
der Inhalt von b steht.
"""

a = [1, 4, 'also', 0]
b = a[:2]
c = a[-1]
d = a + a + b + b
print("List a: ", a)
print("List b: ", b)
print("List c: ", c)
print("List d: ", d)


"""
Erzeugen Sie eine Liste cubic in der die 3.Potenz der natürlichen Zahlen von 1 bis 20
steht.
(a) mit einer for-Schleife
(b) mit einer List Comprehension
"""
cubic_for = []
for i in range(1, 21):
    cubic_for.append(i * i)
print("Cubic For Loop: ", cubic_for)

cubic_list_comprehension = [i * i for i in range(1, 21)]
print("Cubic List Comprehension: ", cubic_list_comprehension)

"""
Erzeugen Sie den String ‘0123456789’ mit einer for-Schleife
"""
numbers = ""
for i in range(10):
    numbers += str(i)
print(numbers)


"""
Schreiben Sie eine Funktion DIVISION(x,y) in einem Python-Skript, die den Wert von x/y
berechnet und ausgibt. Beachten Sie, dass diese Division für y=0 nicht definiert ist.
Erzeugen Sie entsprechend eine Fehlermeldung.
"""
def division(x, y):
    if y == 0:
        print("Oh boy do I have the division by zero exception for you...")
        print("Jokes aside please do not divide by zero")
        return None
    return x / y

result = division(1,3)
print(f"1 / 3 = ", result)

division(1, 0)

"""
Schreiben Sie eine Funktion SCHALTJAHR(n), die eine 0 ausgibt, wenn n kein Schaltjahr
ist und eine 1 ausgibt, wenn n ein Schaltjahr ist. Hierbei gilt: Die Jahreszahl eines
Schaltjahres n lässt sich durch 4 teilen. Dies gilt aber nicht wenn n auch durch 100
teilbar ist. Allerdings ist es doch wieder ein Schaltjahr, wenn n sich durch 400 teilen
lässt.
"""

def schaltjahr(n):
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return True
            return False
        return True
    return False

years = [1992, 1996, 1998, 2000]
for year in years:
    leap_year = schaltjahr(year)
    if leap_year:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")


"""
Erzeuge Sie ein Array a mit 10 beliebigen Zahlen. Erzeugen Sie jetzt jeweils Arrays deren
Element jeweils:
- jeweils das doppelte der Elemente von a sind
- die Hälfte der Elemente von a sind
- um 10 grösser sind als die Elemente von a
"""
a = np.random.rand(10)
print("a: ", a)
b = a * 2
print("b: ", b)
c = a + 10
print("c: ", c)

"""
Erzeuge Sie ein Array b mit 10 beliebigen Zahlen.
Addieren Sie a und b elementweise und schreiben das Ergebnis in ein Array c
"""
b = np.random.rand(10)
print("b: ", b)
c = a + b
print("c: ", c)


"""
Die Preise von 3 Artikeln seien: 9.99 SFr, 21.90 SFr und 2.20 SFr. Schreiben Sie die Preise
in ein Array Preise_SFr. Führen Sie diese und alle folgenden Berechnungen in einem
Skript aus.
- Sie wollen die Preise in EUR berechnen bei einem Kurs von 1.0000 SFr = 1.0129 EUR.
Schreiben Sie die Preise in das Array Preise_EUR.
- Sie wollen alle Preise (in SFr und EUR) um 20% reduzieren. Schreiben Sie die
reduzierten Preise in die Arrays Preise_EUR_red, Preise_SFr_red.
- Am Ende des Jahres sind die Anzahl der Verkäufe wie folgt:

        in SFr (regulär)    in Eur (regulär)    in SFr (mit Rabatt) in EUR (mit Rabatt)
Art 1   210                 14                  89                  7
Art 2   401                 110                 45                  10
Art 3   356                 821                 690                 518

Berechnen Sie den Gesamtumsatz in SFr
"""

exchange_rate_sfr_eur = 1.0129
preise_sfr = np.array([9.99, 21.90, 2.20])
preise_eur = preise_sfr * exchange_rate_sfr_eur
preise_sfr_red = preise_sfr * 0.8
preise_eur_red = preise_eur * 0.8
sold_sfr = np.array([210, 401, 356])
sold_eur = np.array([14, 110, 821])
sold_sfr_red = np.array([89, 45, 690])
sold_eur_red = np.array([7, 10, 518])

revenue_sfr = preise_sfr * sold_sfr + preise_sfr_red * sold_sfr_red
revenue_eur = preise_eur * sold_eur + preise_eur * sold_eur_red
revenue_total = revenue_sfr + (revenue_eur / exchange_rate_sfr_eur)
print("Total revenue in SFR is: ", revenue_total.sum())
