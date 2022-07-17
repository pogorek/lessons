sciezka_do_pliku = "/mnt/d/PROGRAMOWANIE/GIT/kodolamacz/kodolamacz-5/kawa.txt"
sciezka_do_pliku2 = "/mnt/d/PROGRAMOWANIE/GIT/kodolamacz/kodolamacz-5/kawa_wynik.txt"
try:
    liczba_linii = 0
    with open(sciezka_do_pliku) as f:
        while f.readline():
            liczba_linii += 1
        print(f"Liczba linii: {liczba_linii}")
        with open(sciezka_do_pliku2, "w") as f2:
            f2.write(
                f"Scieżka do pliku: {sciezka_do_pliku2}\nLiczba wierszy: {liczba_linii}")

except FileNotFoundError:
    print("Nie ma pliku")
