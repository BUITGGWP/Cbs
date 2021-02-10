n = int(input())
a = list(map(int, input().split()))
al, g = len(a), len(a)
s = True
while g > 1 or s:
    g = max(1, int(g / 1.25))
    s = False
    for i in range(al - g):
        if a[i + g] < a[i]:
            a[i], a[i + g] = a[i + g], a[i]
            s = True
        print(*a)
        
