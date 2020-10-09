import permutation as perm
import symmgroup as sg


S3 = sg.SYMMETRICGROUP(3)

print(S3.generate())


'''
cayley = {(p,q):tuple(perm.PERMUTATION(p).compose(perm.PERMUTATION(q))) 
        for q in S3.getObject() for p in S3.getObject()}

for r in cayley:
    print(r, ":", cayley[r],"\n\n")
'''

'''
p = perm.PERMUTATION((1,2))
q = perm.PERMUTATION((2,3))
pcompq = p.compose(q)
print(str(p)+str(q), "=", str(pcompq))
'''

'''
p = perm.PERMUTATION((1,3))
q = perm.PERMUTATION((1,2))
pcompq = p.compose(q)
print(str(p)+str(q), "should be (1 2 3)")
print(str(p)+str(q),"=",str(pcompq))
'''
