class PERMUTATION(object):

    def __init__(self, permutation):
        permutation = list(permutation)
        self.og = permutation
        self.permutation = self.constructCycle(permutation)
        self.permutation[permutation[-1]] = permutation[0]

    def __repr__(self):
        return '('+str(self.og).replace(',','').replace('[','').replace(']','')+')'

    def represent(self, other):
        return '('+str(list(other.keys())).replace(',','').replace('[','').replace(']','')+')'

    def constructCycle(self, permutation):
        return dict([ (permutation[p], permutation[p+1])
            for p in range(len(permutation)-1)])

    def getOG(self):
        return self.og
    
    def getRaw(self):
        return self.permutation

    def next(self, p):
       return self.permutation[p]

    def compose(self, other):
        #until you figure out how to one shot...
        if self.og == other.og:
            return tuple([1])
        elif len(other.og) == 1:
            return tuple(self.og)
        elif len(self.og) == 1:
            return tuple(other.og)
        else:
            composition = [other.og[0]]+[
                   self.next(other.next(q)) if (other.next(q) in self.og)
                   else other.next(q)
            for q in other.og]
            
            if composition == other.og:
                return tuple([1])
            else:
                 return tuple(composition) if (list(set(composition)) == composition) else tuple(list(set(composition)))
