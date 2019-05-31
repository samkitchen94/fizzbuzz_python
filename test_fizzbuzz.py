import fizzbuzz

def test_returns_number():
  num = fizzbuzz.fizzbuzz(1)
  assert num == 1

def test_returns_zero():
  num = fizzbuzz.fizzbuzz(0)
  assert num == 0

def test_positive_nums():
  num = fizzbuzz.fizzbuzz(-1)
  assert num == "Only positive numbers please"
  
def test_fizz():
  num = fizzbuzz.fizzbuzz(3)
  assert num == "fizz"

def test_buzz():
  num = fizzbuzz.fizzbuzz(5)
  assert num == "buzz"

def test_fizzbuzz():
  num = fizzbuzz.fizzbuzz(15)
  assert num == "fizzbuzz"
