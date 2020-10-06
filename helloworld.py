N = int(input())
bldng = []

for i in range(N):
    bldng.append(list(input()))

bldng = list(map(int,bldng))

print(bldng)