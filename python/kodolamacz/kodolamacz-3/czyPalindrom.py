def main():
    word = input("Tell me a story: ")
    print(czyPalindrom(word))

def czyPalindrom(text):
    if text == text[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    main()

#Napisz funkcję czyPalindrom(), która zwraca prawdę, gdy podany jako argument napis jest palindromem, to znaczy czytany wspak da ten sam napis, np. “kajak”. Funkcja zwraca fałsz w przeciwnym wypadku.