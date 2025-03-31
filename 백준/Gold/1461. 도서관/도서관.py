n, m = map(int, input().split())
positions = sorted(list(map(int, input().split())), reverse=True)

plist = sorted([x for x in positions if x > 0], reverse=True)
nlist = sorted([abs(x) for x in positions if x < 0], reverse=True)

dist = []
for i in range(0, len(plist), m):
    dist.append(plist[i])
for i in range(0, len(nlist), m):
    dist.append(nlist[i])

result = sum(2 * d for d in dist) - max(dist)
print(result)