import permutation as perm

p = perm.PERMUTATION((1,3,2))
q = perm.PERMUTATION((1,2))
pcompq = p.compose(q)
print(str(p)+str(q), "should be (1 3 2)")
print(str(p)+str(q),"=",pcompq)
