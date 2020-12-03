import PERMUTATIONS
import itertools

class SYMMGROUP(object):
    
    def __init__(self, n):
        self.n = n
        factorial = lambda x: 1 if x == 1 else x*factorial(x-1)
        self.size = factorial(n)
        raw = list(map(lambda x: x+1, list(range(n))))
        self.raw = list(itertools.permutations(raw))
        self.perms = [PERMUTATIONS.PERMUTATION(list(o)).permutation
                for o in self.raw]
       
    def __len__(self):
        return self.size

    def __repr__(self):
        cayley = [
                    [
                        tuple([
                                pr(pc(i))
                            for i in range(1,self.n+1)])
                        for pc in self.perms]
                for pr in self.perms]
        '''
        #for some reason, it isn't actually one-line 
        cayley = [
                    [
                        tuple(self.toCycle([
                                pr(pc(i))
                            for i in range(1,self.n+1)]))
                        for pc in self.perms]
                for pr in self.perms]
        '''

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
        hash_cycle = lambda p, n: {i:p(i) for i in range(1, n+1)}
        d = hash_cycle(p, self.n)
        origin = -1
        for i in range(self.n):
            if i != d[i]:
                origin = i
                break
        current = -1
        cycle = []
        if current == -1:
            return [1, 2, 3]
        else:
            while current != origin:
                cycle.append(d[current])
                current = d[current] 
        return cycle                
        '''
        couples = dict(zip(list(range(1,len(p)+1)), p))
        cycle = []
        origin = -1
        current = -1
        for i in range(len(p)):
            if not (p[i] == couples[p[i]]):
                cycle.append(p[i])
                cycle.append(couples[p[i]])
                current = couples[p[i]]
                origin = p[i] 
                break
        if current == -1:
            return p
        else:
            while current != origin:
                cycle.append(couples[current])
                current = couples[current]
            #for i in range(len(p) - 1):
            #    current = couples[current]
            #    cycle.append(current)
        return cycle
        '''

        '''
        current = -1
        for i in range(len(p)):
            if not(current == -1) and not(p[i] == couples[p[i]]):
                cycle.append(couples[current])
            elif current == -1 and not(p[i] == couples[p[i]]):
                cycle.append(i+1)
                cycle.append(p[i])
                current = couples[p[i]]
                print("second condition", current)
        return cycle
        '''
