# 1 Dodawanie
def add(a, b):
    return a + b

print("1_DODAWANIE")
print(add(5, 7))
print(add(-2, 10))

# 2 Prostokat
def rectangle_area(a, b):
    return a * b

print("2_PROSTOKAT")
print(rectangle_area(5, 7))
print(rectangle_area(3, 10))

# 3 Pitagoras
def hypotenuse(a, b):
    return ((a ** 2) + (b ** 2)) ** 0.5

print("3_PITAGORAS")
print(hypotenuse(3, 4))
print(hypotenuse(3, 10))

# 4 Parzysta
def is_even(num):
    return num % 2 == 0

print("4_PARZYSTA")
print(is_even(3))
print(is_even(2))

# 5 Najwieksza
def largest(a, b, c):
    max = 0
    if a > b:
        if a > c:
            max = a
        else:
            max = c
    else:
        if b > c:
            max = b
        else:
            max = c
    return max

print("5_NAJWIEKSZA")
print(largest(100, 20, 15))
print(largest(1, 2, 4))

# 6 Suma_N
def sum_to(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum

print("6_SUMA_N")
print(sum_to(1))
print(sum_to(10))

# 7 Silnia
def factorial(n):
    if n == 0:
        return 1
    silnia = n
    for i in range(1, n):
        silnia *= i
    return silnia

print("7_SILNIA")
print(factorial(5))
print(factorial(10))

# 8 Cyfry
def count_digits(n):
    i = 10
    count = 0
    liczba = n
    if n == 0:
        count = 1
        return count
    while n > 0:
        n = liczba // i
        i = i * 10
        count += 1
    return count

print("8_CYFRY")
print(count_digits(2341))
print(count_digits(4735935))

#9 Odwrocenie
def reverse_number(n):
    reszta = 0
    odwrocenie = 0
    dzielenie = 10
    while True:
        reszta = n % dzielenie
        n = n // dzielenie
        odwrocenie = (odwrocenie * 10) + reszta
        if (n % dzielenie == 0 and n == 0):
            break
    return odwrocenie

print("9_ODWROCENIE")
print(reverse_number(1200034))
print(reverse_number(987))

#10 Pierwsza
def is_prime(n):
    isprime = 1
    if n == 1:
        return False
    for i in range(2, n - 1):
        if n % i == 0:
            isprime = 0
            break
        else :
            isprime = 1
    if isprime == 0:
        return False
    else:
        return True

print("10_PIERWSZA")
print(is_prime(15))
print(is_prime(25))

#11 Suma_listy
print("11_SUMA_LISTY")
def sum_list(numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

print(sum_list([1, 2, 3, 4]))
print(sum_list([10, -2, 5]))

#12 Max_listy
def largest_in_list(numbers):
    max = numbers[0]
    for n in numbers:
        if n > max:
            max = n
    return max

print("12_MAX_LISTY")
print(largest_in_list([3, 7, 2, 9, 4]))
print(largest_in_list([100, 7, 2, 9, 4]))

#13 Wystapienia
def count_occurrences(items, target):
    count = 0
    for n in items:
        if n == target:
            count += 1
    return count

print("13_WYSTAPIENIA")
print(count_occurrences([1, 2, 2, 3, 2], 2))
print(count_occurrences(["a", "b", "a"], "a"))

#14 Wspolne
def common_elements(list1, list2):
    list3 = []
    for n in list1:
        if n in list2:
            list3.append(n)
    return list3

print("14_WSPOLNE")
print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))

#15 Odleglosc
def distance_from_origin(point):
    return ((point[0] ** 2) + (point[1] ** 2)) ** 0.5

print("15_ODLEGLOSC")
print(distance_from_origin((3,4)))

#16 Licznik
def count_words(text):
    slownik = {}
    words = text.split()
    for word in words:
        if word in slownik.keys():
            slownik[word] += 1
        else:
            slownik[word] = 1
    return slownik

print("16_LICZNIK")
print(count_words("cat dog cat cat dog"))

#17 Najlepszy
def best_player(scores):
    max = 0
    m_player = ""
    for player, score in scores.items():
        if max < score:
            max = score
            m_player = player
    return m_player

print("17 NAJLEPSZY")
print(best_player(scores = {
    "Adam": 15,
    "Bartek": 21,
    "Kasia": 18,
    "Ola": 25
}))
#18 Magazyn

def inventory_value(inventory):
    all = 0
    for stock in inventory.values():
        all += stock["price"] * stock["qty"]
    return all
def low_stock(inventory, threshold):
    produkty = []
    for product, stock in inventory.items():
        if stock["qty"] < threshold:
            produkty.append(product)
    return produkty

print("18.1 CALOSC")
print(inventory_value(inventory = {
    "chleb": {"price": 5, "qty": 12},
    "mleko": {"price": 3, "qty": 0},
    "masło": {"price": 9, "qty": 3},
    "ser": {"price": 24, "qty": 7}
}))
print("18.2 THRESHOLD")
print(low_stock(inventory = {
    "chleb": {"price": 5, "qty": 12},
    "mleko": {"price": 3, "qty": 0},
    "masło": {"price": 9, "qty": 3},
    "ser": {"price": 24, "qty": 7}
}, threshold = 5))

#19 Kolko_krzyzyk
def check_winner(board):
    for row in board:
        if row[0] == "O" and row[1] == "O" and row[2] == "O":
            return "O"
        elif row[0] == "X" and row[1] == "X" and row[2] == "X":
            return "X"

    for i in range(1):
        for j in range(3):
            if board[i][j] == "O" and board[i+1][j] == "O" and board[i+2][j] == "O":
                return "O"
            elif board[i][j] == "X" and board[i+1][j] == "X" and board[i+2][j] == "X":
                return "X"

    if board[2][2] == "O" and board[1][1] == "O" and board[0][0] == "O":
        return "O"
    elif board[2][2] == "X" and board[1][1] == "X" and board[0][0] == "X":
        return "X"
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        return "O"
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return "X"
    else:
        return "DRAW"

print("19 KOLKO KRZYZYK")
print(check_winner(board = [
    ["O", "X", "X"],
    ["X", "X", "O"],
    ["O", "X", "X"]
]))