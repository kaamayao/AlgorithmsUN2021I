# Uses python3
from sys import stdin

def calculteNextFibNumbers(fibNumbers):
  temp = fibNumbers[0]
  fibNumbers[0] = fibNumbers[1]
  fibNumbers[1] = temp + fibNumbers[0]
  return fibNumbers

def getFib(n):
  if n == 0:
    return 0 
  fibNumbers = [0,1]
  for i in range(1,n):
    fibNumbers = calculteNextFibNumbers(fibNumbers)
  return fibNumbers[1]

def fibonacci_sum_squares_naive(n):
    BASE = 10
    PISANO_PERIOD = 60
    n = n%PISANO_PERIOD
    return (getFib(n)*getFib(n+1))%BASE

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
