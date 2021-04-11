%%cython --annotate

import numpy as np
cimport numpy as np
import cython
import time

cdef int fast_atoi(char *buff):
    cdef int c = 0, sign = 0, x = 0
    cdef char *p = buff
    while True:
        c = p[0]
        if c == 0:
            break
        if c == 45:
            sign = 1
        elif c > 47 and c < 58:
            x = x * 10 + c - 48
        p += 1
    return -x if sign else x

@cython.boundscheck(False)
@cython.wraparound(False)
def get_points_cython_numpy(filename):
    cdef int i, j, x, y, z, n_chunks
    cdef bytes line, chunk
    cdef int[:, ::1] points = np.zeros([500000, 3], np.int32)
    f = open(filename, 'rb')
    j = 0
    for line in f:
        n_chunks = int(len(line)/16)
        for i in range(n_chunks):
            chunk = line[16*i:16*(i+1)]
            x = fast_atoi(chunk[0:6])
            y = fast_atoi(chunk[6:12])
            z = fast_atoi(chunk[12:16])
            points[j, 0] = x
            points[j, 1] = y
            points[j, 2] = z
            j = j + 1

    f.close()
    return points.base[:j]

n = input()
maxNumber = 0
maxSecondNumber = 0
aux = 0

start = time.time()
numbers = get_points_cython_numpy("text3.txt")

for i in range(int(n)):
    aux = int(input())
    if(maxNumber < aux):
        maxSecondNumber = maxNumber
        maxNumber = aux
    elif(maxSecondNumber < aux):
        maxSecondNumber = aux

maxProductUltraFast = maxNumber * maxSecondNumber

stop = time.time()

ms_int = stop-start

reading_time = ms_int

print("Result using Ultra Fast method:",maxProductUltraFast)
print("Execution time:",str(ms_int),"s")
