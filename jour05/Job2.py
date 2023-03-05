num = int(input("Entrer un nombre entier positif : "))


def puissance(n):
    result = 10
    result = result * 10
    puissance(n-1)
    if n == 0:
        print(result)


puissance(num)
