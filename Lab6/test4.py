import random
from os import remove

try:
	remove("input4.txt")
except OSError:
	pass

n = 20
f = open("input4.txt", "a")
f.write(str(n)+"\n")
for i in range(n):
	r1 = random.randint(0, 200000)
	f.write(str(r1)+"\n")
f.close()
