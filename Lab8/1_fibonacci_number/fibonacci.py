def calc_fib(n):
  res = [0,1]
  for i in range(2, n+1):
    res.append(res[i-1]+res[i-2])
  return res[n]

n = int(input())
print(calc_fib(n))
