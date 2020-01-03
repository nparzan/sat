from sat import *

n = 10

# for i in range(100):
#     cl1 = Clause.random(n)
#     print(cl1)

# m_p = 2**9
# m_n = 2**4 + 2**8
# c1 = (Clause(m_p, m_n, 10))
# print(c1)
# print(c1(2**9 + 2**4, 0))
# print("ABC")
# F = Formula([c1, -c1])

# for c in F:
#     print(c)

# print(F(2**9 + 2**4, 0))

cl = Clause(4, 0, 3)
taut = Clause(1,1,10)
print(taut)
print(cl(7, 0))
F = Formula([cl])
print(F.brute_force())

G = Formula.random(15, 150)
#print(G)

# ass = Formula.random_assignment(10)
# print(G(ass))

sol = G.brute_force(count=True)
max_cl = G.approximate_sat()
print("Average sat ratio", max_cl)
#print(sol / 2**15)
#print("Approx", G.approximate_count())
exit()

# print(G(ass[0], ass[1]))
# print(Clause(ass[0], ass[1], 10))
# print(bin(ass[0]), bin(ass[1]))
# print(G)

L = Formula.random(20, 50)
sol = L.brute_force()
if sol:
    print(Clause(sol[0], sol[1], 20))

print(L.brute_force(count=True) / (2**20))

approx = 0
k = 10000
for i in range(k):
    ass = Formula.random_assignment(20)
    if (L(ass[0], ass[1])):
        print(Clause(ass[0], ass[1], 20))
        approx += 1

print("Acceptance probability:", approx / k)
