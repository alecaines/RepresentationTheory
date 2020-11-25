import PERMUTATIONS
import SYMMETRICGROUP 

#Testing permutation class
s3 = SYMMETRICGROUP.SYMMGROUP(3)
e = PERMUTATIONS.PERMUTATION([1,2,3])
ee = e.permutation

'''
for p in s3.perms:
    print(e.show(p), "::", "1 -> " + str(p(1)), "2 -> " + str(p(2)), "3 -> " + str(p(3)))


'''
#Testing symmetric group
s3 = SYMMETRICGROUP.SYMMGROUP(3)
print(s3)
