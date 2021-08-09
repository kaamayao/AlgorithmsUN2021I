# Uses python3
import sys
import math

COINS = [1,3,4]

def get_change(money):
    minimum_num_coins = [0] 
    minimum_num_coins += [math.inf]*money
    for m in range(1,money+ 1):
        for coin in COINS:
            if m >= coin:
                coins = minimum_num_coins[m-coin]+1
                if coins < minimum_num_coins[m]:
                    minimum_num_coins[m] = coins
    return minimum_num_coins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
