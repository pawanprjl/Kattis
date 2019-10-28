X = int(input())
N = int(input())
inp = []
out = X
for i in range(N):
	inp.append(int(input()))

for i in inp:
		out = out - i + X

print(out)