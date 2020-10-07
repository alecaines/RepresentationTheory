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
        return [other.getOG()[0]]+[
                    (self.next(other.next(q)) if (other.next(q) in self.og)
                    else other.next(q))
                    for q in list(other.getOG()) 
                ]
        '''
        for p in other.getOG():
            if other.next(p) not in self.og:
                result.append(p)
                result.append(other.next(p))
            else:
                result.append(
        '''


        '''
        return str([other.getOG()[0]]+ [self.next(other.next(p)) if other.next(p) in self.og
                    else other.next(p)
                    for p in other.getOG()]).replace('[','(').replace(']',')').replace(',','')
        '''
