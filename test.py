import pytest
import main as main

def test_add():
    assert main.add(1, 2) == 3
    assert main.add(-5, 3) == -2

def test_rectangle_area():
    assert main.rectangle_area(5, 6) == 30
    assert main.rectangle_area(-5, 4) == -20

def test_hypotenuse():
    assert main.hypotenuse(3, 4) == 5
    assert main.hypotenuse(0, 6) == 6

def test_is_even():
    assert main.is_even(2) == True
    assert main.is_even(3) == False
    assert main.is_even(-3) == False

def test_largest():
    assert main.largest(100, 20, 15) == 100
    assert main.largest(30, 150, 3) == 150
    assert main.largest(30, 50, 50) == 50

def test_sum_to():
    assert main.sum_to(1) == 1
    assert main.sum_to(0) == 0
    assert main.sum_to(5) == 15

def test_factorial():
    assert main.factorial(1) == 1
    assert main.factorial(0) == 1
    assert main.factorial(6) == 720

def test_count_digits():
    assert main.count_digits(0) == 1
    assert main.count_digits(100) == 3
    assert main.count_digits(4735935) == 7

def test_reverse_number():
    assert main.reverse_number(0) == 0
    assert main.reverse_number(4700935) == 5390074
    assert main.reverse_number(1001) == 1001

def test_is_prime():
    assert main.is_prime(1) == False
    assert main.is_prime(2) == True
    assert main.is_prime(3) == True
    assert main.is_prime(10) == False
    assert main.is_prime(17) == True

def test_sum_list():
    assert main.sum_list([1, 2, 3, 4]) == 10
    assert main.sum_list([10, -2, 5, -15, 3]) == 1

def test_largest_in_list():
    assert main.largest_in_list([3, 7, 2, 9, 4]) == 9
    assert main.largest_in_list([-10, -7, -2, -9, -4, -100, -255]) == -2

def test_count_occurrences():
    assert main.count_occurrences([1, 2, 2, 3, 2], 2) == 3
    assert main.count_occurrences(["a", "b", "a", "a", "a", "A"], "a") == 4
    assert main.count_occurrences(["a", "b", "a", "a", "a", "A"], "c") == 0
    assert main.count_occurrences([], "a") == 0

def test_common_elements():
    assert main.common_elements([1, 2, 3, 4], [5, 6, 7, 8]) == []
    assert main.common_elements([1, 2, 3, 4], [1, 2, 3, 4]) == [1, 2, 3, 4]
    assert main.common_elements([10, 15, 3, 45, 34, 68], [15, 68, 100]) == [15, 68]

def test_distance_from_origin():
    assert main.distance_from_origin((3, 4)) == 5
    assert main.distance_from_origin((8, 6)) == 10

def test_count_words():
    assert main.count_words("hello world") == {"hello": 1, "world": 1}
    assert main.count_words("hello hello Hello hellO") == {"hello": 2, "Hello" : 1, "hellO" : 1}
    assert main.count_words("") == {}

def test_best_player():
    assert main.best_player(scores = {
    "Adam": 15,
    "Bartek": 21,
    "Kasia": 18,
    "Ola": 25
}) == "Ola"

def test_inventory_value():
    assert main.inventory_value(inventory = {
    "chleb": {"price": 5, "qty": 12},
    "mleko": {"price": 3, "qty": 0},
    "masło": {"price": 9, "qty": 3},
    "ser": {"price": 24, "qty": 7}
}) == 255

    assert main.inventory_value(inventory = {
    "chleb": {"price": 3, "qty": 0},
    "mleko": {"price": 18, "qty": 0},
    "masło": {"price": 12, "qty": 0},
    "ser": {"price": 5, "qty": 0}
}) == 0

    assert main.inventory_value({}) == 0

def test_low_stock():
    assert main.low_stock(inventory = {
    "chleb": {"price": 5, "qty": 12},
    "mleko": {"price": 3, "qty": 0},
    "masło": {"price": 9, "qty": 3},
    "ser": {"price": 24, "qty": 7}
}, threshold = 5) == ['mleko', 'masło']

    assert main.low_stock(inventory = {
    "chleb": {"price": 5, "qty": 12},
    "mleko": {"price": 3, "qty": 0},
    "masło": {"price": 9, "qty": 3},
    "ser": {"price": 24, "qty": 7}
}, threshold = 20) == ['chleb', 'mleko', 'masło', 'ser']

    assert main.low_stock(inventory = {
    "chleb": {"price": 5, "qty": 12},
    "mleko": {"price": 3, "qty": 10},
    "masło": {"price": 9, "qty": 8},
    "ser": {"price": 24, "qty": 7}
}, threshold = 3) == []

    assert main.low_stock(inventory = {
    "chleb": {"price": 5, "qty": 3},
    "mleko": {"price": 3, "qty": 3},
    "masło": {"price": 9, "qty": 3},
    "ser": {"price": 24, "qty": 3}
}, threshold = 3) == []


def test_check_winner():
    assert main.check_winner([
        ["X", "O", "O"],
        ["X", "O", "X"],
        ["X", "X", "O"]
    ]) == "X"

    assert main.check_winner([
        ["X", "O", "X"],
        ["O", "O", "X"],
        ["X", "O", "X"]
    ]) == "O"

    assert main.check_winner(board = [
    ["O", "X", "X"],
    ["X", "X", "O"],
    ["O", "X", "X"]
]) == "X"

    assert main.check_winner(board = [
    ["O", "O", "O"],
    ["X", "X", "O"],
    ["O", "X", "X"]
]) == "O"

    assert main.check_winner(board = [
    ["O", "O", "X"],
    ["X", "X", "O"],
    ["O", "X", "X"]
]) == "DRAW"

    assert main.check_winner(board = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "O", "X"]
]) == "X"

    assert main.check_winner(board = [
    ["X", "X", "O"],
    ["X", "O", "X"],
    ["O", "X", "X"]
]) == "O"