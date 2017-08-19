n, m = map(int, input().split())
tmp = map(int, input().split())
array = [e for e in tmp if (e != " ")]
array = set(array)
tmp = map(int, input().split())
A = [e for e in tmp if (e != " ")]
tmp = map(int, input().split())
B = [e for e in tmp if (e != " ")]

intersectA = list(e for e in array if e in A)
intersectB = list(e for e in array if e in B)

happiness = 0
for e in intersectA:
    happiness += 1

for e in intersectB:
    happiness -= 1

print(happiness)