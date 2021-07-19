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

def calculateFibNumber(n,mod)
  fibNumbers = [0,1]

  for i in 1...n
    fibNumbers = calculteNextFibNumbers(fibNumbers)
  end

  return fibNumbers[1]%mod
end

def fib_huge(n, period)
  n = n%period.length()
  return period[n]
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

def fib_sum_last_digit(n)
  pisanoPeriodBaseDec = getPisanoPeriod(10)
  periodLenght = pisanoPeriodBaseDec.length()
  n = n%periodLenght
  res = getFibSum(n)%periodLenght
  return res.digits.first
end

if __FILE__ == $0
  n = gets.to_i
  puts "#{fib_sum_last_digit(n)}"
end
