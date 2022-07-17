def main():
    print(sprytne_potegowanie(3, 6))

def sprytne_potegowanie(podstawa, wykladnik):
    if wykladnik == 1:
        return podstawa
    elif wykladnik % 2 == 0:
        return sprytne_potegowanie(podstawa, wykladnik / 2) * sprytne_potegowanie(podstawa, wykladnik / 2)
    else:
        return podstawa * sprytne_potegowanie(podstawa, wykladnik - 1)


if __name__ == '__main__':
    main()

# def silnia(n):
#   if n == 0:
#     return 1
#   return n*silnia(n-1)
#
# Okazuje się, że można obliczyć potęgę przy użyciu mniejszej liczby mnożeń, korzystając z rekurencji. W tym celu przeanalizujmy przykład: $2^7$ = $2^3$ * $2^3$ * 2. Jak widzimy, wystarczy raz obliczyć $2^3$. Następnie można ten wynik przemnożyć przez samego siebie, a potem, jeśli oryginalny wykładnik był nieparzysty (a był, bo było to 7), domnożyć jeszcze raz przez podstawę. Napisz funkcję sprytne_potegowanie(podstawa, wykladnik), która oblicza zadaną potęgę w podany sposób: wywołuje rekurencyjnie samą siebie dla wykładnika podzielonego na dwa (z zaokrągleniem) jak w przykładzie, a następnie operując na tym częściowym wyniku oblicza pełną potęgę.