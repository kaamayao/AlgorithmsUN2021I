#Uses python3
import sys

def fill_matrix(M,len_a,len_b,len_c,a,b,c):
    for i in range(len_a):
            for j in range(len_b):
                for k in range(len_c):
                    M[i][j][k] = max(max(M[i-1][j][k], M[i][j-1][k]), M[i][j][k-1])
                    if (i == 0 or j == 0 or k == 0):
                        M[i][j][k] = 0
                    elif (a[i-1] == b[j-1] and a[i-1] == c[k-1]):
                        M[i][j][k] = M[i-1][j-1][k-1] + 1
    return M 

def start_matrix(x,y,z):
    M = []
    for i in range(x):
        M.append([])
        for j in range(y):
            M[i].append([])
            for k in range(z):
                M[i][j].append(0)
    return M

def lcs3(a,b,c):
    len_a = len(a)
    len_b = len(b)
    len_c = len(c)
    M = start_matrix(len_a,len_b,len_c)
    M = fill_matrix(M,len_a,len_b,len_c,a,b,c)
    return M[-1][-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
