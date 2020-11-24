import PERMUTATIONS
import itertools

class SYMMGROUP(object):
    
    def __init__(self, n):
        self.n = n
        raw = list(map(lambda x: x+1, list(range(n))))
        self.raw = list(itertools.permutations(raw))
        self.perms = [PERMUTATIONS.PERMUTATION(list(o)).permutation
                for o in self.raw]
       

    def __repr__(self):
        cayley = [
                    [
                        tuple(self.toCycle([
                                pr(pc(i))
                            for i in range(1,self.n+1)]))
                        for pc in self.perms]
                for pr in self.perms]

        print("=========================================================")
        print("  S"+str(self.n)+"    |", str(self.raw).replace("[","").\
                replace("]","").replace(",",""))
        print("_________________________________________________________")
        for i in range(len(cayley)):
            print(str(self.raw[i]).replace(",",""), "|", str(cayley[i]).\
                    replace("[","").replace("]","").replace(",",""))
        print("=========================================================")
        return ""

    def toCycle(self, p):
        couples = list(zip(list(range(1,len(p)+1)), p))
        s = []
        current = -1
        for c in couples:
           if current == -1 and (c[0] != c[1]):
               s.append(c[0])
               s.append(c[1])
               current = c[1]
           elif current == c[0]:
               s.append(c[1])
        return s

