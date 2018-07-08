class HexList(list):
    def __add__(a, b):
        if len(a)>len(b):
            n = a
            m = b
        else:
            n = b
            m = a
        r = n[:]
        for i in range(min(len(n), len(m))):
            r[i] += m[i]
        return HexList(r)

    def __iadd__(a, b):
        if len(a)>len(b):
            n = a
            m = b
        else:
            n = b
            m = a
        r = n[:]
        for i in range(min(len(n), len(m))):
            r[i] += m[i]
        return HexList(r)

    def __sub__(a, b):
        if len(a)>len(b):
            n = a
            m = b
        else:
            n = b
            m = a
        r = n[:]
        for i in range(min(len(n), len(m))):
            r[i] -= m[i]
        return HexList(r)

    def __isub__(a, b):
        if len(a)>len(b):
            n = a
            m = b
        else:
            n = b
            m = a
        r = n[:]
        for i in range(min(len(n), len(m))):
            r[i] -= m[i]
        return HexList(r)
    
    def __lshift__(a, b):
        r = HexList(a[:])
        m = 2**b
        for i in range(len(r)):
            r[i] *= m
        return r

a = [1, 1]
b = [2]

print a+b

a = HexList(a)
b = HexList(b)
print a+b
c=a-b
print c
c-=[2]
print c

print c<<8

print a<b
print a>b
print a<[0, 1]
print a<[2, 1]
print a<[1, 2]
print [2, 1]<[1, 2]