def print_menu():
    print("1. Citire lista de nr intregi")
    print("2. Afisare lista dupa eliminarea elementelor prime")
    print("3. Media aritmetica este mai mare decat un nr dat")
    print("4. Lista obtinuta prin adaugare dupa fiecare element a nr de divizori proprii ai elementului")
    print("5. Lista obtinuta din cea initiala in care numerele sunt inlocuite cu un tuplu in care \n")
    print("pe prima pozitie este numarul, pe a doua pozitie este index-ul sau in lista iar pe a treia pozitie \n")
    print("se afla numarul de aparitii a numarului in lista")
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


def div_count(x):
    counter = 0
    for i in range(2, x//2 + 1):
        if x % i == 0:
            counter += 1
    return counter


def add_div_count(list):
    rez = []
    for i in range(len(list)):
        rez.append(list[i])
        rez.append(div_count(list[i]))
    list = rez
    return list


def test_add_div_count():
    assert (add_div_count([19, 5, 24, 12, 9]) == [19, 0, 5, 0, 24, 6, 12, 4, 9, 1]) is True
    assert (add_div_count([2, 3, 5, 7]) == [2, 1, 3, 2, 5, 1, 7, 2]) is False


def frequency(list, a):
    fr = 0
    for x in list:
        if x == a:
            fr += 1
    return fr


def tuples(list):
    rez = []
    for i in range(len(list)):
        rez.append([list[i], i, frequency(list, list[i])])
    list = rez
    return list


def test_tuples():
    assert (tuples([25, 13, 26, 13]) == [[25, 0, 1], [13, 1, 2], [26, 2, 1], [13, 3, 2]]) is True


def main():
    test_remove_prime_numbers()
    test_average_above_n()
    test_add_div_count()
    test_tuples()
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
        elif optiune == "4":
            print(add_div_count(l))
        elif optiune == "5":
            print(tuples(l))
        else:
            break


main()
