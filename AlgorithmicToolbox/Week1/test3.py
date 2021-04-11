import random
from os import remove

try:
	remove("input3.txt")
except OSError:
	pass

n = 200000-2
f = open("input3.txt", "a")
f.write(str(n+2)+"\n")
f.write("200000\n")
for i in range(n):
	r1 = random.randint(0, 200000)
	f.write(str(r1)+"\n")
f.write("200000")
f.close()
