#!/usr/bin/env ruby

def pisano_period(m)
  res = 0
  prev = 0
  curr = 1
  for i in 0..((m*m)-1)
    temp = curr
    curr = (curr + prev)%m
    prev = temp
    if prev == 0 && curr === 1 then
      res = i + 1
      break
    end
  end 
  return res
end

def fib_huge(n, m)
  pisano = pisano_period(m) 
  n = n%pisano

  curr = 1
  prev = 0 

  if n == 1
    return 1
  end

  if n == 0
    return 0
  end

  for i in 0..(n-2)
    temp = curr
    curr = (prev + curr)%m
    prev = temp
  end

  return curr % m
end

if __FILE__ == $0
  a, b = gets.split().map(&:to_i)
  puts "#{fib_huge(a, b)}"
end
