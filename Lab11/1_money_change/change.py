# Uses python3
import sys

def get_change(m):
    TEN_COINS = int(m / 10);
    m = m - (TEN_COINS*10)
    FIVE_COINS = int(m / 5);
    m = m - (FIVE_COINS*5)
    ONE_COINS = m;
    TOTAL_COINS = TEN_COINS + FIVE_COINS + ONE_COINS
    return TOTAL_COINS

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
