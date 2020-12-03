import PERMUTATIONS
import SYMMETRICGROUP 

#Testing permutation class
s3 = SYMMETRICGROUP.SYMMGROUP(3)
eo = PERMUTATIONS.PERMUTATION([1,2])
e = eo.permutation

po = PERMUTATIONS.PERMUTATION([1,2])
p = po.permutation

for i in po.terms:
    print(e(p(i)))


'''
for p in s3.perms:
    print(e.show(p), "::", "1 -> " + str(p(1)), "2 -> " + str(p(2)), "3 -> " + str(p(3)))
'''

'''
#Testing symmetric group
'''
s3 = SYMMETRICGROUP.SYMMGROUP(3)
print(s3)
