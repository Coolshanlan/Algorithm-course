m, n, p = [int(a) for a in input("input m n p :").split(' ')]
print(pow(m, n) % p)
tmp = 1

while n != 1:
    if n % 2 != 0:
        tmp *= m
        n -= 1
    m = m % p
    m *= m
    n = n // 2

m = m*tmp
ans = m % p

print(ans)
