import random
import secrets
import requests
import sys

def get_seed():
	r = requests.get("https://www.random.org/cgi-bin/randbyte?nbytes=20&format=d")
	return r.text.replace(" ","").replace("\n","")

code=":c=(n==0)*{:02d}+(n==1)*{:02d}+(n==2)*{:02d}+(n==3)*{:02d}+(n==4)*{:02d}{}"
def show_line(li, i, end):
	arr=li[i*5:i*5+5]
	print(code.format(arr[0], arr[1], arr[2], arr[3], arr[4], end))

def show(name, li, end, line):
	end="{} goto{}".format(end, line)

	print(name)
	for i in range(7):
		show_line(li, i, end)

def gen_base(seed):
	random.seed(int(seed))

	base=range(35)
	base=random.sample(base, len(base))

	rev=list(base)
	for i in range(len(base)):
		rev[base[i]] = i

	show("base:", base, " :i++", 10)
	show("reverse:", rev, "-o :i--", 19)

def gen_ref(seed):
	random.seed(int(seed))

	base=range(35)
	base=random.sample(base, len(base))
	l = list(base)
	ref = list(base)

	for i in range(int(len(base)/2)):
		a = random.choice(l)
		l.remove(a)
		b = random.choice(l)
		l.remove(b)
		ref[a] = b
		ref[b] = a
	ref[l[0]] = l[0]

	show("reflector:", ref, " :i--", 1)

wheels=2
if len(sys.argv) >= 2:
	wheels=int(sys.argv[1])

if len(sys.argv) >= 3:
	for i in range(wheels):
		gen_base(int(sys.argv[i + 2]))
		print("--------------------------")
	gen_ref(int(sys.argv[wheels + 2]))
else:
	seeds = []
	for i in range(wheels):
		s = get_seed()
		seeds.append(s)
		gen_base(s)
		print("--------------------------")

	s = get_seed()
	seeds.append(s)
	gen_ref(s)

	print("--------------------------")
	print("python Generator.py", wheels, ' '.join(seeds))



