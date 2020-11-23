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
                        tuple([
                                pr(pc(i))
                            for i in range(1,self.n+1)])
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
       pass 

