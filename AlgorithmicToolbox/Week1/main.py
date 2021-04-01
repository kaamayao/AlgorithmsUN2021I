import time

def maxPairwiseProduct(numbers):
    max_product = 0
    aux_product = 0
    n = len(numbers)
    for first in range(n):
        for second in range(1,n):
            aux_product = numbers[first] * numbers[second]
            if(max_product < aux_product):
                max_product = aux_product
    return max_product

def maxPairwiseProductList(numbers):
	numbers.sort()
	return numbers[-1]*numbers[-2]

def maxPairwiseProductFast(numbers):
    n = len(numbers)
    index1 = 0
    for i in range(n):
        if(numbers[i] > numbers[index1]):
            index1 = i
    
    index2 = 0
    for i in range(n):
        if(numbers[i] != numbers[index1] and numbers[i] > numbers[index2]):
            index2 = i
    return numbers[index1]*numbers[index2]

n = input()
maxNumber = 0
maxSecondNumber = 0
aux = 0
numbers = []

start = time.time()

for i in range(int(n)):
    numbers.append(int(input()))
    if(maxNumber < int(numbers[i])):
        maxSecondNumber = maxNumber
        maxNumber = numbers[i]
    elif(maxSecondNumber < numbers[i]):
        maxSecondNumber = numbers[i]

maxProductUltraFast = maxNumber * maxSecondNumber

stop = time.time()

ms_int = stop-start

reading_time = ms_int

print("Result using Ultra Fast method:",maxProductUltraFast)
print("Execution time:",str(ms_int),"s")
print()

start = time.time()
print("Result using Product Fast method:",maxPairwiseProductFast(numbers))
stop = time.time()
ms_int = stop-start
print("Execution time:",str(float(reading_time + ms_int)),"s")
print()

start = time.time()
print("Result using List method:",maxPairwiseProductList(numbers))
stop = time.time()
ms_int = stop-start
print("Execution time:",str(float(reading_time + ms_int)),"s")
print()

start = time.time()
print("Result using naive method:",maxPairwiseProduct(numbers))
stop = time.time()
ms_int = stop-start
print("Execution time:",str(float(reading_time + ms_int)),"s")
