#!/usr/bin/env ruby
def isStartOfSeries(fibNumbers, mod)
  return true if (fibNumbers[0]%mod)==0 && (fibNumbers[1]%mod)==1
  return false
end

def calculteNextFibNumbers(fibNumbers)
  temp = fibNumbers[0]
  fibNumbers[0] = fibNumbers[1]
  fibNumbers[1] = temp + fibNumbers[0]
  return fibNumbers
end

def getFib(n)
  return 0 if n == 0
  fibNumbers = [0,1]
  for i in 1...n
    fibNumbers = calculteNextFibNumbers(fibNumbers)
  end
  return fibNumbers[1]
end

def getPisanoPeriod(mod)
  period = []
  fibNumbers = [0,1] 
  finish = false
  while !finish 
    period.push(fibNumbers[0]%mod)
    fibNumbers= calculteNextFibNumbers(fibNumbers)
    finish = isStartOfSeries(fibNumbers, mod)
  end
  return period
end

def getFibSum(n)
  res = 0 
  fibNumbers = [0,1]
  for i in 0...n 
    fibNumbers = calculteNextFibNumbers(fibNumbers) 
    res = res + fibNumbers[0]
  end
  return res
end

def fib_sum_last_digit(n, periodLenght )
  return res
end

def fib_partial_sum(m, n)
  baseNum = 10 
  pisanoPeriod = getPisanoPeriod(baseNum)
  pisanoPeriodLength = pisanoPeriod.length()
  return getFib(m%pisanoPeriodLength).digits.first if m == n
  m = m % pisanoPeriodLength
  n = n % pisanoPeriodLength
  sumN = getFibSum(n)%pisanoPeriodLength
  sumM = getFibSum(m-1)%pisanoPeriodLength
  return ((sumN - sumM) % baseNum).digits.first
end

if __FILE__ == $0
  m, n = gets.split().map(&:to_i)
  puts "#{fib_partial_sum(m, n)}"
end