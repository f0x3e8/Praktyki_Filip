import pytest
import class_1_book as book
import class_2_rectangle as rectangle
import class_3_bankAccount as bankAccount
import class_4_student as student
import class_5_product as product
import class_6_library as library

def test_class_1_book():
    b1 = book.Book("Dżuma", "Albert Camus", 200)
    b2 = book.Book("Niezwyciężony", "Stanisław Lem", 400)
    assert b1.describe() == "Dżuma, Albert Camus, 200 stron"
    assert b2.describe() == "Niezwyciężony, Stanisław Lem, 400 stron"

def test_class_2_rectangle():
    r1 = rectangle.Rectangle(5, 5)
    r2 = rectangle.Rectangle(5, 3)
    r3 = rectangle.Rectangle(5, 0)

    assert r1.area() == 25
    assert r1.perimeter() == 20
    assert r1.is_square() == True

    assert r2.area() == 15
    assert r2.perimeter() == 16
    assert r2.is_square() == False

    assert r3.area() == 0
    assert r3.perimeter() == 10
    assert r3.is_square() == False

def test_class_3_bankAccount():
    account1 = bankAccount.BankAccount("Adam")

    assert account1.get_balance() == 0
    account1.deposit(100)
    assert account1.get_balance() == 100

    account1.deposit(50)
    assert account1.get_balance() == 150

    account1.withdraw(30)
    assert account1.get_balance() == 120

    assert account1.withdraw(1000) == False
    assert account1.get_balance() == 120

def test_class_4_student():
    s1 = student.Student("Adam", [5, 4, 3])
    s2 = student.Student("Bartek", [2, 2, 3])
    s3 = student.Student("Kasia", [5, 5, 4])
    s4 = student.Student("Ola", [3, 2, 2])

    assert s1.average() == 4
    assert s1.has_passed() == True
    assert s2.has_passed() == False
    assert s3.has_passed() == True
    assert s4.has_passed() == False