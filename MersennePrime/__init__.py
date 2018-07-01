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


class MersennePrime:
    def _list(self, n):
        m = []
        v = n
        m.append(v % 256)
        while v>255:
            v = math.floor(v / 256)
            m.append(v % 256)
        return m

    def _sub(self, n, s):
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
        return m

    def _add(self, n, a):
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
        return m

    def _and(self, n, a):
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
        return m

    def _smaller(self, n, m):
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

    def _mod(self, n, m):
        r = n[:]
        if self._smaller(r, m):
            return r
        while not self._smaller(r, m):
            r = self._sub(r, m)
        return r

    def _mul(self, n, m):
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
            while r[i] > 255:
                r[i] -= 256
                r[i+1] += 1
        if r[-1] > 255:
            t = self._list(r[-1])
            r[-1] = t[0]
            for i in range(1, len(t)):
                r.append(t[i])
        
        return r

    def _square(self, n):
        return self._mul(n[:], n[:])

    def __init__(self, m):
        if m<2:
            raise Exception('Number should be bigger than 2.')
        if m%2 != 1:
            raise Exception('Number should be odd.')
        # if m is not prime:
        # raise Esxception('No time wasters please. I can only accept prime numbers.')
        self._m = m
        # P = 2 ** m - 1
        self._P = self._list(m)
    
    def isPrime(self):
        mod = [4]
        for i in range(self._m - 2):
            mod = self._square(mod)
            mod = self._sub(mod, 2)
            mod = self._mod(mod)
        if mod == 0:
            return True
        return False
