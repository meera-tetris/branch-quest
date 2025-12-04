"""
Add functions for add, subtract, multiply and divide
Example:
add: num1 + num2
sub: num1 - num2
mul: num1 * num2
div: num1 / num2
"""



def add(a, b):
    return a + b


def sub(a, b):
  #for float subtraction
  pass

def mul(a, b):
    return a * b

 # Division implementation 
def div(a, b):
    return a / b


def exponent(a, b):
    return a**b


def square(a):
  return a ** 2

def floor_div(a,b):
  return a//b

def main():
  print(add(10, 5))
  print(sub(10, 5))
  print(mul(10, 5))
  print(div(10, 5))
  print(floor_div(10, 5))
  print(exponent(10, 5))


if __name__ == "__main__":
    main()
