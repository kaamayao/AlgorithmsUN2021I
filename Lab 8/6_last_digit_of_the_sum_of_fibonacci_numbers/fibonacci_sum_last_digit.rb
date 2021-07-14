#!/usr/bin/env ruby

def fib_sum_last_digit(n)
  cycle_lenght = 20 
  module_base = 10 
  fib_2 = [0,1,1]
  fib_5 = [0,1,1,2,3,0,3,3,1,4,0,4,4,3,2,0,2,2,4,1]
  res = fib_5[(n+2)%cycle_lenght]
  return (res-1)%module_base if res%2 == fib_2[(n+2)%3] 
  return res+4
end

if __FILE__ == $0
  n = gets.to_i
  puts "#{fib_sum_last_digit(n)}"
end
