def main():
    print("Podaj w oddzielnych wierszach liczbę, operację matematyczną: +,-,*,/,%, a następnie kolejną liczbę:")
    a = int(input())
    znak = input()
    b = int(input())

    if znak == "+":
        print(f"{a} {znak} {b}: {a + b}")
    elif znak == "-":
        print(f"{a} {znak} {b}: {a - b}")
    elif znak == "*":
        print(f"{a} {znak} {b}: {a * b}")
    elif znak == "/":
        print(f"{a} {znak} {b}: {a / b}")
    elif znak == "%":
        print(f"{a} {znak} {b}: {a % b}")
    else:
        print(f"Nie ma takiego znaku")


if __name__ == '__main__':
    main()

# Podaj w oddzielnych wierszach liczbę, operację matematyczną: +,-,*,/,%, a następnie kolejną liczbę:
# 12
# +
# 3
# Twój wynik to: 15
# Chcesz wykonać kolejne działanie? Wpisz literę t lub n.
