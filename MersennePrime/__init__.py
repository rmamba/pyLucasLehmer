# On the other hand, M11 = 2047 = 23 × 89 is not prime. Again, s is set to 4 but is now updated 11−2 = 9 times:

# s ← ((4 × 4) − 2) mod 2047 = 14
# s ← ((14 × 14) − 2) mod 2047 = 194
# s ← ((194 × 194) − 2) mod 2047 = 788
# s ← ((788 × 788) − 2) mod 2047 = 701
# s ← ((701 × 701) − 2) mod 2047 = 119
# s ← ((119 × 119) − 2) mod 2047 = 1877
# s ← ((1877 × 1877) − 2) mod 2047 = 240
# s ← ((240 × 240) − 2) mod 2047 = 282
# s ← ((282 × 282) − 2) mod 2047 = 1736

class MersennePrime:
    def __list(self, n):
        m = []
        m[0] = 0xff
        m[1] = 0x07
        return m

    def __sub(self, n, s):
        m = n[:]
        for i in range(len(s)):
            m[i] -= s[i]
        for i in range(len(m)-1):
            if m[i] < 0:
                m[i] += 256
                m[i+1] -= 1
        if m[-1] < 0:
            raise Exception('Negative value.')
        return m

    def __add(self, n, a):
        m = n[:]
        m[0] += a
        for i in range(len(m)-1):
            if m[i] < 0:
                m[i] += 256
                m[i+1] -= 1
        return m

    def __and(self, n, a):
        m = []
        l1 = n[:]
        l2 = a[:]
        while len(l1) < len(l2):
            l1.append(0)
        for i in range(len(l2)):
            m.append(l1[i] & l2[i])
        return m

    def __smaller(self, n, m):
        # return true if n<m
        if len(n) < len(m):
            return True
        if len(n) > len(m):
            return False
        # else len n==m
        i = len(n) - 1
        while i >= 0:
            if n[i] < m[i]:
                return True
            i -= 1
        return False

    def __mod(self, n, m):
        r = n[:]
        if self.__smaller(r, m):
            return r
        while not self.__smaller(r, m):
            r = self.__sub(r, m)
        return r

    def __init__(self, m):
        self.__m = 11
        # P = 2 ** m - 1
        self.__P = self.__list(m)
    
    def isPrime(self):
        mod = [4]
        for i in range(self.__m - 2):
            mod = self.__square(mod)
            mod = self.__sub(mod, 2)
            mod = self.__mod(mod)
        if mod == 0:
            return True
        return False
