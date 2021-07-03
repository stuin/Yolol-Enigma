import random

base=range(30)
base=random.sample(base, len(base))

rev=list(base)
for i in range(len(base)):
	rev[base[i]] = i

l = list(base)
ref = list(base)
for i in range(int(len(base)/2)):
	a = random.choice(l)
	l.remove(a)
	b = random.choice(l)
	l.remove(b)
	ref[a] = b
	ref[b] = a

s=":c=(n==0)*{:02d}+(n==1)*{:02d}+(n==2)*{:02d}+(n==3)*{:02d}+(n==4)*{:02d}{}"
def show_line(li, i, end):
	arr=li[i*5:i*5+5]
	print(s.format(arr[0], arr[1], arr[2], arr[3], arr[4], end))

def show(name, li, line):
	end=" :i++ goto{}".format(line)
	if line < 16:
		end="-o :i-- goto{}".format(line)

	print(name)
	for i in range(6):
		show_line(li, i, end)

show("base:", base, 9)
show("reverse:", rev, 17)
show("\nreflector:", ref, 2, 1)




