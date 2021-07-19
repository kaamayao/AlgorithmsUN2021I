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

def fib_huge(n, m)
  period =  getPisanoPeriod(m)
  period_length = period.length()
  n = n%period_length
  return period[n]
end

if __FILE__ == $0
  a, b = gets.split().map(&:to_i)
  puts "#{fib_huge(a, b)}"
end
