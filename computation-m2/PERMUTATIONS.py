import itertools

class PERMUTATION(object):

    def __init__(self, terms):
        self.cycletype = len(terms)
        self.terms = terms
        self.permutation = self.createPermutation(terms)
        self.inverse = self.getInverse()

    def __repr__(self):
        return str(self.terms).replace("[","(").replace("]",")").replace(",", "")

    def show(self, p):
        s = [p(i) for i in self.terms]
        s = s[len(s)-1:] + s[:len(s)-1]
        s = str(s[::-1])

        return s.replace("[","(").replace("]",")").replace(",", "")
    
    def checkInverse(self, p, q):
        for i in self.terms:
            if p(i) != q(i):
                return False
        return True

    def getInverse(self):
        inverse = lambda x: x
        perms = list(itertools.permutations(self.terms))
        perms = list(filter(lambda x: x != tuple(self.terms), perms))
        possible_inverses = [self.createPermutation(pi) 
                for pi in perms]
        for pi in possible_inverses:
            if self.checkInverse(self.permutation, pi):
                #inverse = pi
                return inverse

        return inverse

    def createPermutation(self, terms):
        s = "lambda x: "
        for i in range(len(terms)):
            if i == len(terms)-1:
                s+= str(terms[0]) + " if x == " + str(terms[i]) + " else x"
            else:
                s+= str(terms[i+1]) + " if x == " + str(terms[i]) + " else "

        return eval(s)
