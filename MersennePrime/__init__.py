"""
Python library to test Mersenne prime numbers with Lucas-Lehmer algorythm.

This module contains the core framework classes that form the basis of
specific test cases and suites (TestCase, TestSuite etc.), and also a
text-based utility class for running the tests and reporting the results
 (TextTestRunner).

Simple usage:

    from MersenePrime import MersennePrime

    mp = MersenePrime(3)
    print(mp.isPrime())

Further information is available in the bundled documentation, and from

  https://github.com/rmamba/pyLucasLehmer

"""

import math
import time

class MersennePrime:
    speed = {
        'add': 0,
        'and': 0,
        'mod': 0,
        'mod2n': 0,
        'mul': 0,
        'smaller': 0,
        'sub': 0,
        'square': 0,
        'total': 0,
        'list': 0,
        'div2n': 0
    }

    def _remove0s(self, n):
        r = n[:]
        while r[-1] == 0:
            if len(r) == 1:
                break
            del r[-1]
        return r

    def _list(self, n):
        t = time.time()
        m = []
        v = n
        m.append(v % 256)
        while v>255:
            v = int(math.floor(v / 256))
            m.append(v % 256)
        self.speed['list'] += time.time() - t
        return m

    def _sub(self, n, s, p=0):
        t = time.time()
        z = []
        # if self.debug:
        # print('\t{}/{}'.format(len(n), len(s)))
        m = n[:]
        for i in range(p, len(s)):
            m[i] -= s[i]
        #     if m[i] < 0:
        #         z.append(i)
        # if len(z) > 0 :
        #     z.append(len(m)-1)
        #     for i in range(len(z)-1):
        #         for j in range(z[i], z[i+1]):
        #             m[j] += 256
        #             m[j+1] -= 1
        #             if m[j+1] >= 0:
        #                 j = z[-1]
        for i in range(p, len(m)-1):
            while m[i] < 0:
                m[i] += 256
                m[i+1] -= 1
                if m[i+1] >= 0:
                    break
        if m[-1] < 0:
            print(z)
            print(m)
            raise Exception('Negative value.')
        m = self._remove0s(m)
        self.speed['sub'] += time.time() - t
        return m

    def _add(self, n, a):
        t = time.time()
        m = n[:]
        while len(m) < len(a):
            m.append(0)
        for i in range(len(a)):
            m[i] += a[i]
        for i in range(len(m)-1):
            while m[i] > 255:
                m[i] -= 256
                m[i+1] += 1
        if m[-1] > 255:
            l = self._list(m[-1])
            m[-1] = l[0]
            for i in range(1, len(l)):
                m.append(l[i])
        self.speed['add'] += time.time() - t
        return m

    def _and(self, n, a):
        t = time.time()
        if len(a)<=len(n):
            r = n[0:len(a)]
            q = a[:]
        else:
            r = a[0:len(n)]
            q = n[:]
        for i in range(len(q)):
            r[i] &= q[i]
        r = self._remove0s(r)
        self.speed['and'] += time.time() - t
        return r

    def _smaller(self, n, m):
        t = time.time()
        # return true if n<m
        if len(n) < len(m):
            self.speed['smaller'] += time.time() - t
            return True
        if len(n) > len(m):
            self.speed['smaller'] += time.time() - t
            return False
        # else len n==m
        i = len(n) - 1
        while i >= 0:
            if n[i] < m[i]:
                self.speed['smaller'] += time.time() - t
                return True
            if n[i] > m[i]:
                self.speed['smaller'] += time.time() - t
                return False
            i -= 1
        for i in range(len(n)):
            if n[i] != m[i]:
                self.speed['smaller'] += time.time() - t
                return True
        self.speed['smaller'] += time.time() - t
        return False

    def _mod(self, n, m):
        t = time.time()
        r = n[:]
        if len(n)<len(m):
            self.speed['mod'] += time.time() - t
            return r
        if self._smaller(n, m):
            self.speed['mod'] += time.time() - t
            return r
        for i in range(len(self._R)):
            while not self._smaller(r, self._R[i]):
                r = self._sub(r, self._R[i], self._Z[i])
        self.speed['mod'] += time.time() - t
        return r

    def _mod2n(self, n, m1, m2):
        t = time.time()
        r = self._and(n, m1)
        q = self._div2n(n, m2)
        r = self._add(r, q)
        r = self._mod(r, m1)
        self.speed['mod2n'] += time.time() - t
        return r
    
    def _mul(self, n, m):
        t = time.time()
        r = n[:]
        w = n[:]
        q = m[:]
        while len(r)<len(m):
            r.append(0)
        while len(q)<len(r):
            q.append(0)
        for i in range(len(r)):
            r[i] = 0
        while len(w)<len(r):
            w.append(0)
        for i in range(len(w)):
            for j in range(len(q)):
                r[i+j] += w[i] * q[j]
            r.append(0)
        while r[-1] == 0:
            if len(r) == 1:
                break
            del r[-1]
        for i in range(len(r)-1):
            # if r[i]>255:
            r[i+1] += int(math.floor(r[i] / 256))
            r[i] %= 256
        if r[-1] > 255:
            u = self._list(r[-1])
            r[-1] = u[0]
            for i in range(1, len(u)):
                r.append(u[i])
        self.speed['mul'] += time.time() - t
        return r

    # def _div(self, n, d):
    #     r = n[:]
    #     if self._smaller(n, d):
    #         return n[:]
    #     return r

    def _div2n(self, n, d):
        t = time.time()
        if len(n)<len(d):
            self.speed['div2n'] += time.time() - t
            return [0]
        r = n[:]
        q = d[:]
        p = self._zero(d)
        for i in range(p):
            del r[0]
            del q[0]
        if self._smaller(n, d):
            return n[:]
        self.speed['div2n'] += time.time() - t
        return r

    def _square(self, n):
        return self._mul(n[:], n[:])

    def _zero(self, n):
        pos = 0
        for i in range(len(n)):
            if n[i] != 0:
                break
            pos += 1
        return pos

    def __init__(self, m, debug=False):
        if m<2:
            raise Exception('Number should be bigger than 2.')
        if m%2 != 1:
            raise Exception('Number should be odd.')
        # if m is not prime:
        # raise Esxception('No time wasters please. I can only accept prime numbers.')
        self._m = m
        # P = 2 ** m - 1
        self._P = self._sub(self._list(2 ** m), [1])
        self._R = []
        self._Z = []
        t = self._square(self._P)
        self._R.append(t)
        self._Z.append(self._zero(t))
        self._R.append(self._P)
        self._Z.append(0)
        p = self._P[:]
        p.insert(0, 0)
        while self._smaller(p, self._R[0]):
            self._R.insert(1, p)
            self._Z.insert(1, self._zero(p))
            p = self._mul(p, [2])

        self.debug = debug
        self.speed = {
            'add': 0,
            'and': 0,
            'mod': 0,
            'mod2n': 0,
            'mul': 0,
            'smaller': 0,
            'sub': 0,
            'square': 0,
            'total': 0,
            'list': 0,
            'div2n': 0
        }
    
    def isPrime(self):
        t = time.time()
        mod = [4]
        for i in range(self._m - 2):
            mod = self._square(mod)
            mod = self._sub(mod, [2])
            mod = self._mod(mod, self._P)
            if self.debug:
                print('{}/{}: {}'.format(i, self._m-3, mod))
                print
        self.speed['total'] = time.time() - t
        if mod == [0]:
            return True
        return False
