def print_menu():
    print("1. Citire lista de nr intregi")
    print("2. Afisare lista dupa eliminarea elementelor prime")
    print("3. Media aritmetica este mai mare decat un nr dat")
    print("4. Lista obtinuta prin adaugare dupa fiecare element nr de divizori proprii ai elementului")
    print("5. Lista obtinuta din cea initiala in care numerele sunt inlocuite cu un tuplu in care")
    print("x. Iesire")


def read_list():
    l = []
    string_citit = input("Dati lista de nr intregi, separate prin virgula: ")
    numere = string_citit.split(",")
    for x in numere:
        l.append(int(x))
    return l


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    return True


def remove_prime_numbers(list):
    nr = 0
    not_primes = []
    j = 0
    for i in range(len(list)):
        if is_prime(list[i]) == 0:
            not_primes.append(list[i])
    list = not_primes
    return list


def test_remove_prime_numbers():
    assert (remove_prime_numbers([3, 5, 7, 11]) == []) is True
    assert (remove_prime_numbers([1, 2, 6, 10, 13]) == [1, 6, 10]) is True
    assert (remove_prime_numbers([3, 7, 10, 20, 6, 4]) == [7, 10, 20, 6, 4]) is False


def average_above_n(list, n):
    sum = 0
    nr = 0
    for x in list:
        sum += x
        nr += 1
    if sum / nr > n:
        return True
    return False


def test_average_above_n():
    assert average_above_n([1, 2, 3, 4], 1) is True
    assert average_above_n([10, -3, 25, -1, 3, 25, 18], 10) is True
    assert average_above_n([1, 6, 9, 10], 7) is False


def main():
    test_remove_prime_numbers()
    test_average_above_n()
    l = []
    while True:
        print_menu()
        optiune = input("Alegeti optiunea: ")
        if optiune == "1":
            l = read_list()
        elif optiune == "2":
            print(remove_prime_numbers(l))
        elif optiune == "3":
            n = int(input("Dati nr n: "))
            if average_above_n(l, n):
                print("DA")
            else:
                print("NU")
        else:
            break


main()
