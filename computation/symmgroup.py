from itertools import chain, combinations

class SYMMETRICGROUP(object):

    def __init__(self, order):
        self.order = order
        self.sn = self.getObject()

    def __repr__(self):
        return str(self.sn).replace("[","{").replace("]","}")
    
    def getObject(self):
        s = list(range(1, self.order+1))
        withSingletons =  list(chain.from_iterable(combinations(s,r)
            for r in range(len(s)+1)))
        emptyToSingleton = list(map(
                    lambda k: (tuple((1)) if k == () else k),
                    withSingletons))
        print(emptyToSingleton)
        return list(filter(lambda k: len(list(k)) != 1, emptyToSingleton))
        #return [[j+1 for j in range(i, self.order)] for i in range(self.order)]
    
