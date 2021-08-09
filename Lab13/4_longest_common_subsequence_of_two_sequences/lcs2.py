import sys

def fill_matrix(M, row_len, col_len):
    for i in range(0,row_len+1):
        for j in range(0,col_len+1):
            M[i][j] = max(M[i-1][j] , M[i][j-1])
            if i == 0 or j == 0 :
                M[i][j] = 0
            elif a[i-1] == b[j-1]:
                M[i][j] = M[i-1][j-1]+1
    return M 


def initialize_matrix(rows, cols):
    M = [[]] * cols
    for i in range(len(M)):
        M[i] = [0] * rows 
    return M 

def lcs2(a, b):
    len_a, len_b = len(a), len(b)
    M = initialize_matrix(len_b+1, len_a+1)
    M = fill_matrix(M,len_a,len_b)
    return M[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
