#labelled non-unital semigroups:
    #on zero elements: 1
    #on one element: 1
    #on two elements: 8
    #on three elements: 113
    #on four elements:
#this is the OEIS sequence A023814.

def labelled_semigroups_2by2():
    count = 2**4
    print(str(count) + ' multiplication tables to check')
    print()
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    M = [[a, b], [c, d]]
                    for (x, y, z) in ((X, Y, Z) for X in range(2) for Y in range(2) for Z in range(2)):
                        if not(M[M[x][y]][z] == M[x][M[y][z]]):
                            count -= 1
                            break
    print(count)

def labelled_semigroups_3by3():
    count = 3**9
    print(str(count) + ' multiplication tables to check')
    print()
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    for e in range(3):
                        for f in range(3):
                            for g in range(3):
                                for h in range(3):
                                    for i in range(3):
                                        M = [[a, b, c], [d, e, f], [g, h, i]]
                                        for (x, y, z) in ((X, Y, Z) for X in range(3) for Y in range(3) for Z in range(3)):
                                            if not(M[M[x][y]][z] == M[x][M[y][z]]):
                                                count -= 1
                                                break
    print(count)


def labelled_semigroups_4by4():
    count = 2**32   #4**16
    print(str(count) + ' multiplication tables to check')
    print()
    for a in range(4):
        print(a)
        for b in range(4):
            print('   ' + str(b))
            for c in range(4):
                print('      ' + str(c))
                for d in range(4):
                    print('         ' + str(d))
                    for e in range(4):
                        for f in range(4):
                            for g in range(4):
                                for h in range(4):
                                    for i in range(4):
                                        for j in range(4):
                                            for k in range(4):
                                                for l in range(4):
                                                    for m in range(4):
                                                        for n in range(4):
                                                            for o in range(4):
                                                                for p in range(4):
                                                                    M = [[a, b, c, d], [e, f, g, h], [i, j, k, l], [m, n, o, p]]
                                                                    for (x, y, z) in ((X, Y, Z) for X in range(4) for Y in range(4) for Z in range(4)):
                                                                        if not(M[M[x][y]][z] == M[x][M[y][z]]):
                                                                            count -= 1
                                                                            print('\r' + str(count), end='')
                                                                            break
    print(count)

########################################

#unital semigroups (monoids):
#we can take advantage of the unit here which makes n=4 feasible

#labelled unital semigroups (monoids):
    #on zero elements: 0
    #on one element: 1
    #on two elements: 4
    #on three elements: 33
    #on four elements: 624
    #on five elements:
#This is the OEIS sequence A058153.

#labelled unital semigroups (monoids) with fixed unit:
    #on zero elements: 0
    #on one element: 1
    #on two elements: 2
    #on three elements: 11
    #on four elements: 156
#This is the OEIS sequence A058154.

#on two elements e and x we must have either
    #x is the identity:
    #   x y
    #   ___
    # x|x y
    # y|y *
#or
    #y is the identity:
    #   x y
    #   ___
    # x|* x
    # y|x y

#so there are at most four unital semigroups. if we have two of each element in the multiplicattion table then we get
#(a labelling of) the group Z/2 so this works, and the other possibility also works in both cases - for example in the first case,
#if y^2 = x then we can verify associativity: we need only check (ab)c = a(bc) when a,b,c are all non-identity elements,
#so we just need to check (yy)y = y(yy), and indeed y^2 y = x y (= y) = y x = y y^2.

def labelled_monoids_fixed_unit_3by3():
    #we iterate over each of the tables.
    count = 3**4    #there are 3*3*3*3 = 3^4 possibilities

    print(str(count) + ' multiplication tables to check')
    print()

    #we can do all three types simultaneously as follows:
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    M = [[0, 1, 2], [1, a, b], [2, c, d]]
                    for (x, y, z) in ((X, Y, Z) for X in range(3) for Y in range(3) for Z in range(3)):
                        if not(M[M[x][y]][z] == M[x][M[y][z]]):
                            count -= 1
                            break
    print(count)

def labelled_monoids_fixed_unit_4by4():
    count = 2**18   #4**9    #there are 4^9 possibilities

    print(str(count) + ' multiplication tables to check')
    print()

    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    for e in range(4):
                        for f in range(4):
                            for g in range(4):
                                for h in range(4):
                                    for i in range(4):
                                        M = [[0, 1, 2, 3], [1, a, b, c], [2, d, e, f], [3, g, h, i]]
                                        for (x, y, z) in ((X, Y, Z) for X in range(4) for Y in range(4) for Z in range(4)):
                                            if not(M[M[x][y]][z] == M[x][M[y][z]]):
                                                count -= 1
                                                break
    print(count)

####################################################

#5x5:
#this time the types are:

#type 1: 0 is the identity
    #   0 1 2 3 4
    #   _________
    # 0|0 1 2 3 4
    # 1|1 * * * *
    # 2|2 * * * *
    # 3|3 * * * *
    # 4|4 * * * *
#type 2: 1 is the identity
    #   0 1 2 3 4
    #   _________
    # 0|* 0 * * *
    # 1|0 1 2 3 4
    # 2|* 2 * * *
    # 3|* 3 * * *
    # 4|* 4 * * *
#type 3: 2 is the identity
    #   0 1 2 3 4
    #   _________
    # 0|* * 0 * *
    # 1|* * 1 * *
    # 2|0 1 2 3 4
    # 3|* * 3 * *
    # 4|* * 4 * *
#type 4: 3 is the identity
    #   0 1 2 3 4
    #   _________
    # 0|* * * 0 *
    # 1|* * * 1 *
    # 2|* * * 2 *
    # 3|0 1 2 3 4
    # 4|* * * 4 *
#type 5: 4 is the identity
    #   0 1 2 3 4
    #   _________
    # 0|* * * * 0
    # 1|* * * * 1
    # 2|* * * * 2
    # 3|* * * * 3
    # 4|0 1 2 3 4

# count = 5**17   #there are 5^16 possibilities for each of the 5 types, and there can be no overlap between the types
#     #compare this to the 4^16 = 2^32 tables that need to be check for not-necessarily-unital semigroups at n=4:
#     #the base is bigger but the exponent is smaller, so at first we might expect something smaller, however 5^17 ~ 8 x 10^11 ~ 10^12
#     #while 2^32 ~ 4 x 10^9
#         #this makes sense because 5 is more than the square of 2. indeed, just doesn't simplify 4**16: then we're looking at
#         #5^17 vs. 4^16 - the ratio is 5 * 5^16/4^16 = 5*(5/4)^16 >> 1.
# print(str(count) + ' multiplication tables to check')
# print()
#
# for a in range(5):
#     for b in range(5):
#         for c in range(5):
#             for d in range(5):
#                 for e in range(5):
#                     for f in range(5):
#                         for g in range(5):
#                             for h in range(5):
#                                 for i in range(5):
#                                     for j in range(5):
#                                         for k in range(5):
#                                             for l in range(5):
#                                                 for m in range(5):
#                                                     for n in range(5):
#                                                         for o in range(5):
#                                                             for p in range(5):
#                                                                 M = [[0, 1, 2, 3, 4], [1, a, b, c, d], [2, e, f, g, h], [3, i, j, k, l], [4, m, n, o, p]]
#                                                                 N = [[a, 0, b, c, d], [0, 1, 2, 3, 4], [e, 2, f, g, h], [i, 3, j, k, l], [m, 4, n, o, p]]
#                                                                 P = [[a, b, 0, c, d], [e, f, 1, g, h], [0, 1, 2, 3, 4], [i, j, 3, k, l], [m, n, 4, o, p]]
#                                                                 Q = [[a, b, c, 0, d], [e, f, g, 1, h], [i, j, k, 2, l], [0, 1, 2, 3, 4], [m, n, o, 4, p]]
#                                                                 R = [[a, b, c, d, 0], [e, f, g, h, 1], [i, j, k, l, 2], [m, n, o, p, 3], [0, 1, 2, 3, 4]]
#                                                                 #we can also take advantage of the fact that we only have to check non-identity elements
#                                                                 for (x, y, z) in ((X, Y, Z) for X in range(1, 5) for Y in range(1, 5) for Z in range(1, 5)):
#                                                                     if not(M[M[x][y]][z] == M[x][M[y][z]]):
#                                                                         count -= 1
#                                                                         break
#
#                                                                 for (x, y, z) in ((X, Y, Z) for X in range(5) for Y in range(5) for Z in range(5)):
#                                                                     if x == 1 or y == 1 or z == 1:
#                                                                         continue
#                                                                     if not(N[N[x][y]][z] == N[x][N[y][z]]):
#                                                                         count -= 1
#                                                                         break
#
#                                                                 for (x, y, z) in ((X, Y, Z) for X in range(5) for Y in range(5) for Z in range(5)):
#                                                                     if x == 2 or y == 2 or z == 2:
#                                                                         continue
#                                                                     if not(P[P[x][y]][z] == P[x][P[y][z]]):
#                                                                         count -= 1
#                                                                         break
#
#                                                                 for (x, y, z) in ((X, Y, Z) for X in range(5) for Y in range(5) for Z in range(5)):
#                                                                     if x == 3 or y == 3 or z == 3:
#                                                                         continue
#                                                                     if not(Q[Q[x][y]][z] == Q[x][Q[y][z]]):
#                                                                         count -= 1
#                                                                         break
#
#                                                                 for (x, y, z) in ((X, Y, Z) for X in range(5) for Y in range(5) for Z in range(5)):
#                                                                     if x == 4 or y == 4 or z == 4:
#                                                                         continue
#                                                                     if not(R[R[x][y]][z] == R[x][R[y][z]]):
#                                                                         count -= 1
#                                                                         print('\r' + str(count), end='')    #only print the count here so there's less spam
#                                                                         break
# print(count)

#this would take over three months to finish calculating

####################################################################
####################################################################
####################################################################

#the commutative case:

#labelled non-unital semigroups:
    #on zero elements: 1
    #on one element: 1
    #on two elements: 6
    #on three elements: 63
    #on four elements: 1140
#This is the OEIS sequence A023815.

def labelled_commutative_semigroups_2by2():
    count = 2**3
    print(str(count) + ' multiplication tables to check')
    print()
    for a in range(2):
        for b in range(2):
            for c in range(2):
                M = [[a, b], [b, c]]
                for (x, y, z) in ((X, Y, Z) for X in range(2) for Y in range(2) for Z in range(2)):
                    if not(M[M[x][y]][z] == M[x][M[y][z]]):
                        count -= 1
                        break
    print(count)

def labelled_commutative_semigroups_3by3():
    count = 3**6
    print(str(count) + ' multiplication tables to check')
    print()
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    for e in range(3):
                        for f in range(3):
                            M = [[a, b, c], [b, d, e], [c, e, f]]
                            for (x, y, z) in ((X, Y, Z) for X in range(3) for Y in range(3) for Z in range(3)):
                                if not(M[M[x][y]][z] == M[x][M[y][z]]):
                                    count -= 1
                                    break
    print(count)

def labelled_commutative_semigroups_4by4():
    count = 2**20   # =4**10
    print(str(count) + ' multiplication tables to check')
    print()
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    for e in range(4):
                        for f in range(4):
                            for g in range(4):
                                for h in range(4):
                                    for i in range(4):
                                        for j in range(4):
                                            M = [[a, b, c, d], [b, e, f, g], [c, f, h, i], [d, g, i, j]]
                                            for (x, y, z) in ((X, Y, Z) for X in range(4) for Y in range(4) for Z in range(4)):
                                                if not(M[M[x][y]][z] == M[x][M[y][z]]):
                                                    count -= 1
                                                    #print('\r' + str(count), end='')
                                                    break
    print(count)

########################################

#labelled commutative unital semigroups (monoids):
    #we can take advantage of the unit here which makes n=4 feasible

#on zero elements: 0
#on one element: 1
#on two elements: 4
#on three elements: 27
#on four elements: 376
#on five elements: 7430

#labelled commutative semigroups with fixed identity:
    #on zero elements: 0
    #on one element: 1
    #on two elements: 2
    #on three elements: 9
    #on four elements: 94
    #on five elements: 1486

#labelled groups with fixed identity:
    #on zero elements: 0
    #on one element: 1
    #on two elements: 1
    #on three elements: 1
    #on four elements: 4
    #on five elements:

#labelled abelian groups with fixed identity:
    #on zero elements: 0
    #on one element: 1
    #on two elements: 1
    #on three elements: 1
    #on four elements: 4
    #on five elements: 6

#3x3:
def assoc_3by3(M):
    for (x, y, z) in ((X, Y, Z) for X in range(3) for Y in range(3) for Z in range(3)):
        if not (M[M[x][y]][z] == M[x][M[y][z]]):
            return False
    return True
def invers_3by3(M):
    inverses = []
    for x in range(3):  #we check whether x has a unique inverse. we can take advantage of the fact that a monoid
                        #is a group if and only if every element has a right inverse
        inverses = []
        for y in range(3):
            if M[x][y] == 0:
                inverses.append(y)
        if not(len(inverses) == 1):
            return False
    return True

# count = 3**3    #there are 3^3 possibilities
# print(str(count) + ' multiplication tables to check')
# print()
#
# #we can do all three types simultaneously as follows:
# for a in range(3):
#     for b in range(3):
#         for c in range(3):
#             M = [[0, 1, 2], [1, a, b], [2, b, c]]
#             if assoc_3by3(M) == False:
#                 count -= 1
#             else:
#                 if invers_3by3(M) == False:
#                     count -= 1
#
# print(count)

#4x4:
def assoc_4by4(M):
    for (x, y, z) in ((X, Y, Z) for X in range(4) for Y in range(4) for Z in range(4)):
        if not (M[M[x][y]][z] == M[x][M[y][z]]):
            return False
    return True
def invers_4by4(M):
    inverses = []
    for x in range(4):  #we check whether x has a unique inverse. we can take advantage of the fact that a monoid
                        #is a group if and only if every element has a right inverse
        inverses = []
        for y in range(4):
            if M[x][y] == 0:
                inverses.append(y)
        if not(len(inverses) == 1):
            return False
    return True

# count = 2**12   #4**6    #there are 4*6 possibilities
#     #and there can be no overlap between the types
# print(str(count) + ' multiplication tables to check')
# print()
#
# for a in range(4):
#     for b in range(4):
#         for c in range(4):
#             for d in range(4):
#                 for e in range(4):
#                     for f in range(4):
#                         M = [[0, 1, 2, 3], [1, a, b, c], [2, b, d, e], [3, c, e, f]]
#                         if assoc_4by4(M) == False:
#                             count -= 1
#                         else:
#                             if invers_4by4(M) == False:
#                                 count -= 1
#
# print(count)

####################################################

#5x5:
def assoc_5by5(M):
    for (x, y, z) in ((X, Y, Z) for X in range(1, 5) for Y in range(1, 5) for Z in range(1, 5)):
        if not (M[M[x][y]][z] == M[x][M[y][z]]):
            return False
    return True

def invers_5by5(M):
    inverses = []
    for x in range(5):
        inverses = []
        for y in range(5):
            if M[x][y] == 0:
                inverses.append(y)
        if not(len(inverses) == 1):
            return False
    return True

#non-abelian:

# count = 5**16   #there are 5**16 possibilities
# print(str(count) + ' multiplication tables to check')
# print()
#
# for a in range(5):
#     print(a)
#     for b in range(5):
#         print('   ' + str(b))
#         for c in range(5):
#             print('      ' + str(c))
#             for d in range(5):
#                 print('         ' + str(d))
#                 for e in range(5):
#                     print('            ' + str(e))
#                     for f in range(5):
#                         print('               ' + str(f))
#                         for g in range(5):
#                             for h in range(5):
#                                 for i in range(5):
#                                     for j in range(5):
#                                         for k in range(5):
#                                             for l in range(5):
#                                                 for m in range(5):
#                                                     for n in range(5):
#                                                         for o in range(5):
#                                                             for p in range(5):
#                                                                 M = [[0, 1, 2, 3, 4], [1, a, b, c, d], [2, e, f, g, h], [3, i, j, k, l], [4, m, n, o, p]]
#                                                                 if assoc_5by5(M) == False:
#                                                                     count -= 1
#                                                                 else:
#                                                                     if invers_5by5(M) == False:
#                                                                         count -= 1
#
# print()
# print(count)

#abelian:

# count = 5**10   #there are 5**10 possibilities
# print(str(count) + ' multiplication tables to check')
# print()
#
# for a in range(5):
#     print(a)
#     for b in range(5):
#         print('   ' + str(b))
#         for c in range(5):
#             #print('      ' + str(c))
#             for d in range(5):
#                 #print('         ' + str(d))
#                 for e in range(5):
#                     for f in range(5):
#                         for g in range(5):
#                             for h in range(5):
#                                 for i in range(5):
#                                     for j in range(5):
#                                         M = [[0, 1, 2, 3, 4], [1, a, b, c, d], [2, b, e, f, g], [3, c, f, h, i], [4, d, g, i, j]]
#                                         if assoc_5by5(M) == False:
#                                             count -= 1
#                                         else:
#                                             if invers_5by5(M) == False:
#                                                 count -= 1
#
# print()
# print(count)