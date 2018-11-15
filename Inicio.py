def isprime(n, p):
    for e in p:
        if n % e == 0:
            return False;
    return True


def primos():
    p = set()
    for e in range(2, 100):
        if isprime(e, p):
            p.add(e)

    return p


print(primos())