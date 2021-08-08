# Uses python3
import sys
import operator

def get_values_per_kg(weigths, values):
    values_per_kg = []
    for i in range(0,len(weigths)):
        values_per_kg.append({'value':values[i]/weights[i], 'index': i })
    return sorted(values_per_kg, key=lambda k: k['value'],reverse=True)

def get_optimal_value(capacity, weights, values):
    value = 0
    valuesPerKg = get_values_per_kg(weights, values)
    for valueKg in valuesPerKg:
        if(capacity >= weights[valueKg['index']]):
            capacity = capacity - weights[valueKg['index']]
            value = value + values[valueKg['index']]
        elif(capacity < weights[valueKg['index']]):
            value = value + (capacity * valueKg['value'])
            capacity = 0
        if(capacity <= 0):
            break
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
