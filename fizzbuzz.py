def fizzbuzz(n):
  if n == 0:
    return 0
  elif n < 0:
    return "Only positive numbers please"
  elif n % 3 == 0 and n % 5 ==0:
    return "fizzbuzz"
  elif n % 3 == 0:
    return "fizz"
  elif n % 5 == 0:
    return "buzz"
  else:
    return n
