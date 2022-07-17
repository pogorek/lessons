def main():
    lista = [3, 5, 6, 7, 6, 5]
    print(moda(lista))

def moda(lista):
    num_max = 0
    winner = 0
    for num in lista:
        if lista.count(num) > num_max:
            winner = num
    return winner


if __name__ == '__main__':
    main()

# Napisz funkcję moda(), która jako parametr przyjmuje listę liczb całkowitych. Funkcja zwraca tę liczbę, która pojawia się w tej liście najczęściej. Jeśli mamy remis, zwróć którąkolwiek z tych liczb.