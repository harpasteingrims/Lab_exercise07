import sample

def test_returns_number():
    assert sample.FizzBuzz(2) == 2

def test_returns_fizz_if_divisible_by_three():
    assert sample.FizzBuzz(3) == "Fizz"

def test_returns_buzz_if_divisible_by_five():
    assert sample.FizzBuzz(5) == "Buzz"