def duplicate_count(text):
    # Your code goes here
    d = dict()
    values = []
    total = 0
    a=text.lower()
    for i in a:
        if i not in d:
            d[i] = 1
        elif i in d:
            d[i] += +1
    values = d.values()
    for j in values:
        if j > 1:
            total = total + 1

    return total
'''print (duplicate_count("abcde"))
print(duplicate_count("abcdea"))
print(duplicate_count("indivisibility"))
print(duplicate_count("aabBcde"))'''


def persistence(n):
    l = list(str(n))
    cuenta = 0
    m = 1
    s = False
    while s != True:
        if len(l) == 1:
            break
        else:
            for i in l:
                m = m * int(i)

            for i in l:
                l.remove(i)
            l = list(str(m))
            print(l)
            cuenta += 1

    return cuenta
print(persistence(25))
#print(persistence(4))
#print(persistence(25))
#print(persistence(999))



