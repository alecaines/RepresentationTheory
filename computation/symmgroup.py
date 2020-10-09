from itertools import chain, combinations
import permutation as perm

class SYMMETRICGROUP(object):

    def __init__(self, order):
        self.order = order
        self.sn = self.getObject()

    def __repr__(self):
        return str(self.sn).replace("[","{").replace("]","}")
    
    def getObject(self):
        s = list(range(1, self.order+1))
        withSingletons =  list(chain.from_iterable(combinations(s,r) for r in range(len(s)+1)))
        removeSingletons = list(filter(lambda k: len(list(k)) > 1, withSingletons))

        return [tuple([1])]+removeSingletons
   
    def generate(self):
        permutations = [tuple([i,j]) for j in range(1,self.order+1) for i in range(1, self.order+1)]
        withoutSingletons = list(filter(lambda p: p[0] != p[1], permutations))
        transitions = list(set(list(map(lambda p: tuple([min(p), max(p)]), withoutSingletons))))

        p = perm.PERMUTATION((2,3))
        q = perm.PERMUTATION((1,2))
        print(str(q)+str(p), "=", q.compose(p))

        return list(set(transitions+[perm.PERMUTATION(p).compose(perm.PERMUTATION(q)) for q in transitions for p in transitions]))
