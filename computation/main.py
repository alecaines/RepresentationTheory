import permutation as perm
import symmgroup as sg


#S3 = sg.SYMMETRICGROUP(3)
#print(S3)

p = perm.PERMUTATION((1,3))
q = perm.PERMUTATION((1,2))
pcompq = p.compose(q)
print(str(p)+str(q), "should be (1 2 3)")
print(str(p)+str(q),"=",pcompq)
