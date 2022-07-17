napis_wczytany = "2,5"
try:
    liczba = float(napis_wczytany)
    print(f"1 Liczbą jest {liczba}")
except ValueError as e:
    print("Och nie, nie udało się sparsować liczby! Szczegóły poniżej:")
    print(e)
print("tutaj kod działa zwyczajnie, reszta programu")


def silnia(n):
    if n < 0:
        raise ValueError("2 silnia niezdefiniowana dla liczb ujemnych")
    wynik = 1
    for i in range(1, n+1):
        wynik *= i
    return wynik


try:
    print(f"3 Silnia z -5 to {silnia(-5)}")
except ValueError as e:
    print("3 Och nie, coś poszło nie tak! Szczegóły poniżej:")
    print(e)
try:
    print("4 Pozyskuję zasób")
    print(f"Silnia z -5 to {silnia(-5)}")
except ValueError as e:
    print("Och nie, coś poszło nie tak! Szczegóły poniżej:")
    print(e)
finally:
    print("Zwalniam zasób")
