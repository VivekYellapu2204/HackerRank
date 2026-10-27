// Problem: Classes: Dealing with Complex Numbers
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem?isFullScreen=true
// Solved on: 2026-10-27T15:43:22.216Z



class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real,
                       self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real,
                       self.imaginary - no.imaginary)

    def __mul__(self, no):
        return Complex(
            self.real * no.real - self.imaginary * no.imaginary,
            self.real * no.imaginary + self.imaginary * no.real
        )

    def __truediv__(self, no):
        denominator = no.real ** 2 + no.imaginary ** 2
        return Complex(
            (self.real * no.real + self.imaginary * no.imaginary) / denominator,
            (self.imaginary * no.real - self.real * no.imaginary) / denominator
        )

    def mod(self):
        return Complex(math.sqrt(self.real ** 2 + self.imaginary ** 2), 0)

    def __str__(self):
        if self.imaginary == 0:
            return "%.2f+0.00i" % self.real
        if self.real == 0:
            return "0.00%+.2fi" % self.imaginary
        return "%.2f%+.2fi" % (self.real, self.imaginary)


