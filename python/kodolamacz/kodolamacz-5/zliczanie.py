sciezka_do_pliku = "/mnt/d/PROGRAMOWANIE/GIT/kodolamacz/kodolamacz-5/kawa.txt"
try:
    liczba_linii = 0
    f = open(sciezka_do_pliku)
    while f.readline():
        liczba_linii += 1
        # print(f.read())
    print(f"Liczba linii: {liczba_linii}")
except FileNotFoundError:
    print("Nie ma pliku")
finally:
    f.close()
