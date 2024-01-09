from numbers import Number


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a - b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs = coefs + self.coefficients[common:] + tuple([-1*x for x in other.coefficients[common:]])
            return Polynomial(coefs)

        elif isinstance(other, Number):
                return Polynomial((self.coefficients[0]-other,)
                              + self.coefficients[1:])
        else:
            return NotImplemented

    def __rsub__(self, other):
        osub = self - other
        nsub = Polynomial(tuple([-1*x for x in osub.coefficients]))
        return nsub
    
    def __mul__(self, other):
        if isinstance(other, Polynomial):
            coefs = Polynomial((0,) * (self.degree() + other.degree() + 1))
            for i in range(self.degree()+1):
                interimstate = tuple([self.coefficients[i] * x for x in other.coefficients])
                shift = (0,) * i
                interimstateshift = shift + interimstate
                coefs = coefs + Polynomial(interimstateshift)
            return coefs
        elif isinstance(other, Number):
            return Polynomial(tuple([other * x for x in self.coefficients]))
        else:
            return NotImplemented
    
    def __rmul__(self,other):
        return self*other

    def __pow__(self,n):
        result = 1
        for i in range(n):
            result = self*result
        return result
    
    def __call__(self, n):
        evaluation = 0
        for i in range(self.degree()+1):
            evaluation = evaluation + self.coefficients[i]*(n**i)
        return evaluation
    
    def dx(self):
        coefs = list((0,) * self.degree())
        if self.degree() == 0:
            return Polynomial((0,))
        print(coefs)
        print(self.coefficients)
        for i in range(self.degree()):
            coefs[i] = self.coefficients[i+1] * (i+1)
            print(coefs)
        return Polynomial(tuple(coefs))


def derivative(poly):
    return poly.dx()
