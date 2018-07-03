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
        'mul': 0,
        'smaller': 0,
        'sub': 0,
        'square': 0,
        'total': 0
    }

    def _list(self, n):
        m = []
        v = n
        m.append(v % 256)
        while v>255:
            v = int(math.floor(v / 256))
            m.append(v % 256)
        return m

    def _sub(self, n, s):
        t = time.time()
        m = n[:]
        for i in range(len(s)):
            m[i] -= s[i]
        for i in range(len(m)-1):
            while m[i] < 0:
                m[i] += 256
                m[i+1] -= 1
        if m[-1] < 0:
            raise Exception('Negative value.')
        while m[-1] == 0:
            if len(m) == 1:
                break
            del m[-1]
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
            t = self._list(m[-1])
            m[-1] = t[0]
            for i in range(1, len(t)):
                m.append(t[i])
        self.speed['add'] += time.time() - t
        return m

    def _and(self, n, a):
        t = time.time()
        m = []
        l1 = n[:]
        l2 = a[:]
        while len(l1) < len(l2):
            l1.append(0)
        for i in range(len(l2)):
            m.append(l1[i] & l2[i])
        while m[-1] == 0:
            if len(m) == 1:
                break
            del m[-1]
        self.speed['and'] += time.time() - t
        return m

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
        for i in range(len(self._R)):
            while not self._smaller(r, self._R[i]):
                r = self._sub(r, self._R[i])
        self.speed['mod'] += time.time() - t
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
            # while r[i] > 255:
            #     r[i] -= 256
            #     r[i+1] += 1
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
    #     return r

    def _square(self, n):
        return self._mul(n[:], n[:])

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
        self._R.append(self._square(self._P))
        self._R.append(self._P);
        p = self._P[:]
        p.insert(0, 0)
        while self._smaller(p, self._R[0]):
            self._R.insert(1, p)
            p = self._mul(p, [2])

        self.debug = debug
        self.speed = {
            'add': 0,
            'and': 0,
            'mod': 0,
            'mul': 0,
            'smaller': 0,
            'sub': 0,
            'square': 0,
            'total': 0
        }
    
    def isPrime(self):
        t = time.time()
        mod = [4]
        for i in range(self._m - 2):
            mod = self._square(mod)
            mod = self._sub(mod, [2])
            mod = self._mod(mod, self._P)
            if self.debug:
                print('{}/{}: {}'.format(i, self._m-2, mod))
                print
        self.speed['total'] = time.time() - t
        if mod == [0]:
            return True
        return False
