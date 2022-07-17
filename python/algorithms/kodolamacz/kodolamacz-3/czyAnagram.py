def main():
    word1 = input("Tell me a story: ")
    word2 = input("Tell me a story 2: ")
    print(czyAnagram(word1, word2))


def czyAnagram(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        for letter in word1:
            if word1.count(letter) != word2.count(letter):
                return False

    return True


if __name__ == '__main__':
    main()

# Napisz funkcję czyAnagram(), która zwraca prawdę, gdy dwa napisy podane jako dwa argumenty funkcji mają tę własność, że da się z liter pierwszego napisu ułożyć drugi napis. To zadanie da się rozwiązać na naprawdę wiele sposobów, a najwydajniejszy z nich zakłada użycie słowników.
