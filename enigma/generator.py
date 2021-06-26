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

s=":i=(n==0)*{:02d}+(n==1)*{:02d}+(n==2)*{:02d}+(n==3)*{:02d}+(n==4)*{:02d}{}"
def show_line(li, i, end):
	arr=li[i*5:i*5+5]
	print(s.format(arr[0], arr[1], arr[2], arr[3], arr[4], end))

def show(name, li, wheel, line):
	end=" :pw{}=0 goto{}".format(wheel, line)
	if line > 16:
		end="-o" + end

	print(name)
	for i in range(6):
		show_line(li, i, end)

show("base:", base, 3, 10)
show("reverse:", rev, 1, 19)
show("\nreflector:", ref, 2, 1)




