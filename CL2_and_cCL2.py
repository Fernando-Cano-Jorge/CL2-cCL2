print("|||||||||||||||||||||    CL2 and cCL2   |||||||||||||||||||||||||")

T = 9
B = 8
TB = 7
NTB = 6
NB = 5
FT = 4
NFT = 3
NF = 2
F = 1
N = 0

V = {T,B,TB,NTB,NB,FT,NFT,NF,F,N}
D = {T,B,TB,NTB,NB,FT}

for X in V:
    def neg(X):
        if X == T:
            return N
        if X == B:
            return F
        if X == TB:
            return NF
        if X == NTB:
            return NFT
        if X == NB:
            return FT
        if X == FT:
            return NB
        if X == NFT:
            return NTB
        if X == NF:
            return TB
        if X == F:
            return B
        if X == N:
            return T

print("Negation")
for X in V:
    print(str(X) + "--->" + str(neg(X)))

for X in V:
    for Y in V:
        def then(X,Y):
            if X == T and Y == T:
                return T
            if X == T and Y == B:
                return N
            if X == T and Y == TB:
                return N
            if X == T and Y == NTB:
                return N
            if X == T and Y == NB:
                return N
            if X == T and Y == FT:
                return N
            if X == T and Y == NFT:
                return N
            if X == T and Y == NF:
                return N
            if X == T and Y == F:
                return N
            if X == T and Y == N:
                return N
            if X == B and Y == T:
                return T
            if X == B and Y == B:
                return FT
            if X == B and Y == TB:
                return NFT
            if X == B and Y == NTB:
                return NF
            if X == B and Y == NB:
                return F
            if X == B and Y == FT:
                return N
            if X == B and Y == NFT:
                return N
            if X == B and Y == NF:
                return N
            if X == B and Y == F:
                return N
            if X == B and Y == N:
                return N
            if X == TB and Y == T:
                return T
            if X == TB and Y == B:
                return FT
            if X == TB and Y == TB:
                return FT
            if X == TB and Y == NTB:
                return NF
            if X == TB and Y == NB:
                return NF
            if X == TB and Y == FT:
                return N
            if X == TB and Y == NFT:
                return N
            if X == TB and Y == NF:
                return N
            if X == TB and Y == F:
                return N
            if X == TB and Y == N:
                return N
            if X == NTB and Y == T:
                return T
            if X == NTB and Y == B:
                return FT
            if X == NTB and Y == TB:
                return NFT
            if X == NTB and Y == NTB:
                return FT
            if X == NTB and Y == NB:
                return NFT
            if X == NTB and Y == FT:
                return N
            if X == NTB and Y == NFT:
                return N
            if X == NTB and Y == NF:
                return N
            if X == NTB and Y == F:
                return N
            if X == NTB and Y == N:
                return N
            if X == NB and Y == T:
                return T
            if X == NB and Y == B:
                return FT
            if X == NB and Y == TB:
                return FT
            if X == NB and Y == NTB:
                return FT
            if X == NB and Y == NB:
                return FT
            if X == NB and Y == FT:
                return N
            if X == NB and Y == NFT:
                return N
            if X == NB and Y == NF:
                return N
            if X == NB and Y == F:
                return N
            if X == NB and Y == N:
                return N
            if X == FT and Y == T:
                return T
            if X == FT and Y == B:
                return B
            if X == FT and Y == TB:
                return TB
            if X == FT and Y == NTB:
                return NTB
            if X == FT and Y == NB:
                return NB
            if X == FT and Y == FT:
                return FT
            if X == FT and Y == NFT:
                return NFT
            if X == FT and Y == NF:
                return NF
            if X == FT and Y == F:
                return F
            if X == FT and Y == N:
                return N
            if X == NFT and Y == T:
                return T
            if X == NFT and Y == B:
                return B
            if X == NFT and Y == TB:
                return B
            if X == NFT and Y == NTB:
                return NTB
            if X == NFT and Y == NB:
                return NTB
            if X == NFT and Y == FT:
                return FT
            if X == NFT and Y == NFT:
                return FT
            if X == NFT and Y == NF:
                return NF
            if X == NFT and Y == F:
                return NF
            if X == NFT and Y == N:
                return N
            if X == NF and Y == T:
                return T
            if X == NF and Y == B:
                return B
            if X == NF and Y == TB:
                return TB
            if X == NF and Y == NTB:
                return B
            if X == NF and Y == NB:
                return TB
            if X == NF and Y == FT:
                return FT
            if X == NF and Y == NFT:
                return NFT
            if X == NF and Y == NF:
                return FT
            if X == NF and Y == F:
                return NFT
            if X == NF and Y == N:
                return N
            if X == F and Y == T:
                return T
            if X == F and Y == B:
                return B
            if X == F and Y == TB:
                return B
            if X == F and Y == NTB:
                return B
            if X == F and Y == NB:
                return B
            if X == F and Y == FT:
                return FT
            if X == F and Y == NFT:
                return FT
            if X == F and Y == NF:
                return FT
            if X == F and Y == F:
                return FT
            if X == F and Y == N:
                return N
            if X == N and Y == T:
                return T
            if X == N and Y == B:
                return T
            if X == N and Y == TB:
                return T
            if X == N and Y == NTB:
                return T
            if X == N and Y == NB:
                return T
            if X == N and Y == FT:
                return T
            if X == N and Y == NFT:
                return T
            if X == N and Y == NF:
                return T
            if X == N and Y == F:
                return T
            if X == N and Y == N:
                return T

print("Conditional (Meyer & Mortensen)")
for X in V:
    for Y in V:
        print("(" + str(X) + "," + str(Y) + ")" + "--->" + str(then(X,Y)))

for X in V:
    for Y in V:
        def wedge(X,Y):
            if X == T and Y == T:
                return T
            if X == T and Y == B:
                return B
            if X == T and Y == TB:
                return TB
            if X == T and Y == NTB:
                return NTB
            if X == T and Y == NB:
                return NB
            if X == T and Y == FT:
                return FT
            if X == T and Y == NFT:
                return NFT
            if X == T and Y == NF:
                return NF
            if X == T and Y == F:
                return F
            if X == T and Y == N:
                return N
            if X == B and Y == T:
                return B
            if X == B and Y == B:
                return B
            if X == B and Y == TB:
                return TB
            if X == B and Y == NTB:
                return NTB
            if X == B and Y == NB:
                return NB
            if X == B and Y == FT:
                return FT
            if X == B and Y == NFT:
                return NFT
            if X == B and Y == NF:
                return NF
            if X == B and Y == F:
                return F
            if X == B and Y == N:
                return N
            if X == TB and Y == T:
                return TB
            if X == TB and Y == B:
                return TB
            if X == TB and Y == TB:
                return TB
            if X == TB and Y == NTB:
                return NB
            if X == TB and Y == NB:
                return NB
            if X == TB and Y == FT:
                return FT
            if X == TB and Y == NFT:
                return NFT
            if X == TB and Y == NF:
                return NF
            if X == TB and Y == F:
                return F
            if X == TB and Y == N:
                return N
            if X == NTB and Y == T:
                return NTB
            if X == NTB and Y == B:
                return NTB
            if X == NTB and Y == TB:
                return NB
            if X == NTB and Y == NTB:
                return NTB
            if X == NTB and Y == NB:
                return NB
            if X == NTB and Y == FT:
                return FT
            if X == NTB and Y == NFT:
                return NFT
            if X == NTB and Y == NF:
                return NF
            if X == NTB and Y == F:
                return F
            if X == NTB and Y == N:
                return N
            if X == NB and Y == T:
                return NB
            if X == NB and Y == B:
                return NB
            if X == NB and Y == TB:
                return NB
            if X == NB and Y == NTB:
                return NB
            if X == NB and Y == NB:
                return NB
            if X == NB and Y == FT:
                return FT
            if X == NB and Y == NFT:
                return NFT
            if X == NB and Y == NF:
                return NF
            if X == NB and Y == F:
                return F
            if X == NB and Y == N:
                return N
            if X == FT and Y == T:
                return FT
            if X == FT and Y == B:
                return FT
            if X == FT and Y == TB:
                return FT
            if X == FT and Y == NTB:
                return FT
            if X == FT and Y == NB:
                return FT
            if X == FT and Y == FT:
                return FT
            if X == FT and Y == NFT:
                return NFT
            if X == FT and Y == NF:
                return NF
            if X == FT and Y == F:
                return F
            if X == FT and Y == N:
                return N
            if X == NFT and Y == T:
                return NFT
            if X == NFT and Y == B:
                return NFT
            if X == NFT and Y == TB:
                return NFT
            if X == NFT and Y == NTB:
                return NFT
            if X == NFT and Y == NB:
                return NFT
            if X == NFT and Y == FT:
                return NFT
            if X == NFT and Y == NFT:
                return NFT
            if X == NFT and Y == NF:
                return F
            if X == NFT and Y == F:
                return F
            if X == NFT and Y == N:
                return N
            if X == NF and Y == T:
                return NF
            if X == NF and Y == B:
                return NF
            if X == NF and Y == TB:
                return NF
            if X == NF and Y == NTB:
                return NF
            if X == NF and Y == NB:
                return NF
            if X == NF and Y == FT:
                return NF
            if X == NF and Y == NFT:
                return F
            if X == NF and Y == NF:
                return NF
            if X == NF and Y == F:
                return F
            if X == NF and Y == N:
                return N
            if X == F and Y == T:
                return F
            if X == F and Y == B:
                return F
            if X == F and Y == TB:
                return F
            if X == F and Y == NTB:
                return F
            if X == F and Y == NB:
                return F
            if X == F and Y == FT:
                return F
            if X == F and Y == NFT:
                return F
            if X == F and Y == NF:
                return F
            if X == F and Y == F:
                return F
            if X == F and Y == N:
                return N
            if X == N and Y == T:
                return N
            if X == N and Y == B:
                return N
            if X == N and Y == TB:
                return N
            if X == N and Y == NTB:
                return N
            if X == N and Y == NB:
                return N
            if X == N and Y == FT:
                return N
            if X == N and Y == NFT:
                return N
            if X == N and Y == NF:
                return N
            if X == N and Y == F:
                return N
            if X == N and Y == N:
                return N

print("Conjunction")
for X in V:
    for Y in V:
        print("(" + str(X) + "," + str(Y) + ")" + "--->" + str(wedge(X,Y)))

for X in V:
    for Y in V:
        def vee(X,Y):
            return neg(wedge(neg(X),neg(Y)))

print("Disjunction")
for X in V:
    for Y in V:
        print("(" + str(X) + "," + str(Y) + ")" + "--->" + str(vee(X,Y)))

for X in V:
    for Y in V:
        def hence(X,Y):
            if X in D and Y in D:
                return "valid"
            if X in D and Y not in D:
                return "invalid"

for X in V:
    def taut(X):
        if X not in D:
            return "invalid"
        else:
            return "valid"

print("--------------------------------------Counterexamples------------------------------------------")

print("<<<<<Axioms for R>>>>>")
print("----Implicative fragment----")

print("Reflexivity:")

for A in V:
    if str(taut(then(A,A)))=="invalid":
        print(str(A))

print("Prefixing:")
for A in V:
    for C in V:
        for E in V:
            if str(then(then(A,C),then(then(E,A),then(E,C)))) == "invalid":
                print("("+ str(A) + "," + str(C) + "," + str(E) + ")")

print("Suffixing:")
for A in V:
    for C in V:
        for E in V:
            if str(then(then(A,C),then(then(C,E),then(A,E)))) == "invalid":
                print("("+ str(A) + "," + str(C) + "," + str(E) + ")")

print("Contraction:")
for A in V:
    for C in V:
        if str(taut(then(then(A,then(A,C)),then(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Self Distribution:")
for A in V:
    for E in V:
        for C in V:
            if str(taut(then(then(A,then(E,C)), then(then(A,E),then(A,C))))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("Permutation:")
for A in V:
    for E in V:
        for C in V:
            if str(taut(then(then(A,then(E,C)),then(E,then(A,C))))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("Assertion:")
for A in V:
    for C in V:
        if str(taut(then(A,then(then(A,C),C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Modus Ponens:")
for A in V:
    for C in V:
        if str(hence(wedge(A,then(A,C)),C))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("----Positive fragment----")

print("Simplification 1:")
for A in V:
    for C in V:
        if str(taut(then(wedge(A,C),A)))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Simplification 2:")
for A in V:
    for C in V:
        if str(taut(then(wedge(A,C),C)))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("And-Composition:")
for A in V:
    for C in V:
        for E in V:
            if str(taut(then(wedge(then(A,C),then(A,E)),then(A,wedge(C,E)))))=="invalid":
                print("(" + str(A) + "," + str(C) + "," + str(E) + ")")

print("Addition 1:")
for A in V:
    for C in V:
        if str(taut(then(A, vee(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Addition 2:")
for A in V:
    for C in V:
        if str(taut(then(C, vee(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Or-Composition:")
for A in V:
    for E in V:
        for C in V:
            if str(taut(then(wedge(then(A,C), then(E,C)), then(vee(A,E), C)))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("Distribution:")
for A in V:
    for E in V:
        for C in V:
            if str(taut(then(wedge(A,vee(E,C)),vee(wedge(A,E),C)))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("----Negative fragment----")

print("Reductio:")
for A in V:
    if str(taut(then(then(A,neg(A)),neg(A)))) == "invalid":
        print(str(A))

print("Intuitionistic Contraposition:")
for A in V:
    for C in V:
        if str(hence(then(A,neg(C)),then(C,neg(A))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Double Negation Elimination:")
for A in V:
    if str(taut(then(neg(neg(A)),A)))=="invalid":
        print(str(A))

print("Double Negation Introduction:")
for A in V:
    if str(taut(then(A,neg(neg(A)))))=="invalid":
        print(str(A))

print("----Connexive theses----")


print("Aristotle's Thesis:")

for A in V:
    if str(taut(neg(then(A,neg(A)))))=="invalid":
        print(str(A))

print("Aristotle variant:")
for A in V:
    if str(taut(neg(then(neg(A),A))))=="invalid":
        print(str(A))

print("Boethius' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(then(A,C),neg(then(A,neg(C)))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Symmetry of the Conditional:")

for A in V:
    for C in V:
        if str(taut(then(then(A,C),then(C,A)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Converse of Boethius' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(neg(then(A,neg(C))),then(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Variant of Boethius' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(then(A,neg(C)),neg(then(A,C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Converse of Variant of Boethius' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(neg(then(A,C)),then(A,neg(C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Francez' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(then(neg(A),C),neg(then(A,C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Variant of Francez' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(then(A,C),neg(then(neg(A),C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Converse of Francez' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(neg(then(A,C)),then(neg(A),C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Converse of Variant of Francez' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(neg(then(neg(A),C)), then(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Aristotle's Second Thesis:")

for A in V:
    for C in V:
        if str(taut(neg(wedge(then(A,C),then(neg(A),C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Abelard's First Principle:")

for A in V:
    for C in V:
        if str(taut(neg(wedge(then(A,C),then(A,neg(C)))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Abelard's Second Principle:")

for A in V:
    for C in V:
        if str(taut(neg(then(A,neg(C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")


print("----Other principles---")


print("Mingle:")
for A in V:
    if str(taut(then(A,then(A,A))))=="invalid":
        print(str(A))

print("Positive Paradox:")
for A in V:
    for C in V:
        if str(taut(then(A,then(C,A))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Negative Paradox:")
for A in V:
    for C in V:
        if str(taut(then(A,then(neg(A),C))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Paradox of Necessity:")
for A in V:
    for C in V:
        if str(taut(then(A,then(C,C))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Explosion:")

for A in V:
    for C in V:
        if str(taut(then(wedge(A,neg(A)),C))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Implosion:")

for A in V:
    for C in V:
        if str(taut(then(A,vee(C,neg(C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Antilogism:")
for A in V:
    for E in V:
        for C in V:
            if str(hence(then(wedge(A,E),C),then(wedge(A,neg(C)),neg(E))))=="invalid":
                print("("+str(A)+","+str(E)+","+str(C)+")")

print("False Antecedent:")

for A in V:
    for C in V:
        if str(hence(neg(A),then(A,C))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Counterexample:")

for A in V:
    for C in V:
        if str(hence(neg(then(A,C)),wedge(A,neg(C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("True Consequent:")

for A in V:
    for C in V:
        if str(hence(C,then(A,C))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")


print("Modus Tollens:")
for A in V:
    for C in V:
        if str(hence(wedge(neg(C),then(A,C)),neg(A)))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Transitivity (Conjunctive Syllogism):")

for A in V:
    for E in V:
        for C in V:
            if str(hence(wedge(then(A,E),then(E,C)),then(A,C)))=="invalid":
                print("("+str(A)+","+str(E)+","+str(C)+")")

print("Monotonicity:")

for A in V:
    for E in V:
        for C in V:
            if str(taut(then(then(A,C),then(wedge(A,E),C)))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("Pseudo Modus Ponens:")

for A in V:
    for C in V:
        if str(taut(then(wedge(then(A,C),A), C))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Rule Affixing:")

for A in V:
    for G in V:
        for C in V:
            for E in V:
                if str(hence(wedge(then(A,G),then(C,E)),then(then(G,C),then(A,E)))) == "invalid":
                    print("(" + str(A) + "," + str(G) + "," + str(C) + "," + str(E) + ")")

print("Affixing:")

for A in V:
    for G in V:
        for C in V:
            for E in V:
                if str(taut(then(wedge(then(A,G),then(C,E)),then(then(G,C),then(A,E))))) == "invalid":
                    print("(" + str(A) + "," + str(G) + "," + str(C) + "," + str(E) + ")")

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Now we modify the conditional >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

for X in V:
    for Y in V:
        def then(X,Y):
            if X == T and Y == T:
                return T
            if X == T and Y == B:
                return N
            if X == T and Y == TB:
                return N
            if X == T and Y == NTB:
                return N
            if X == T and Y == NB:
                return N
            if X == T and Y == FT:
                return N
            if X == T and Y == NFT:
                return N
            if X == T and Y == NF:
                return N
            if X == T and Y == F:
                return N
            if X == T and Y == N:
                return N
            if X == B and Y == T:
                return T
            if X == B and Y == B:
                return FT
            if X == B and Y == TB:
                return NFT
            if X == B and Y == NTB:
                return NF
            if X == B and Y == NB:
                return F
            if X == B and Y == FT:
                return N
            if X == B and Y == NFT:
                return N
            if X == B and Y == NF:
                return N
            if X == B and Y == F:
                return N
            if X == B and Y == N:
                return N
            if X == TB and Y == T:
                return T
            if X == TB and Y == B:
                return FT
            if X == TB and Y == TB:
                return FT
            if X == TB and Y == NTB:
                return NF
            if X == TB and Y == NB:
                return NF
            if X == TB and Y == FT:
                return N
            if X == TB and Y == NFT:
                return N
            if X == TB and Y == NF:
                return N
            if X == TB and Y == F:
                return N
            if X == TB and Y == N:
                return N
            if X == NTB and Y == T:
                return T
            if X == NTB and Y == B:
                return FT
            if X == NTB and Y == TB:
                return NFT
            if X == NTB and Y == NTB:
                return FT
            if X == NTB and Y == NB:
                return NFT
            if X == NTB and Y == FT:
                return N
            if X == NTB and Y == NFT:
                return N
            if X == NTB and Y == NF:
                return N
            if X == NTB and Y == F:
                return N
            if X == NTB and Y == N:
                return N
            if X == NB and Y == T:
                return T
            if X == NB and Y == B:
                return FT
            if X == NB and Y == TB:
                return FT
            if X == NB and Y == NTB:
                return FT
            if X == NB and Y == NB:
                return FT
            if X == NB and Y == FT:
                return N
            if X == NB and Y == NFT:
                return N
            if X == NB and Y == NF:
                return N
            if X == NB and Y == F:
                return N
            if X == NB and Y == N:
                return N
            if X == FT and Y == T:
                return T
            if X == FT and Y == B:
                return B
            if X == FT and Y == TB:
                return TB
            if X == FT and Y == NTB:
                return NTB
            if X == FT and Y == NB:
                return NB
            if X == FT and Y == FT:
                return FT
            if X == FT and Y == NFT:
                return NFT
            if X == FT and Y == NF:
                return NF
            if X == FT and Y == F:
                return F
            if X == FT and Y == N:
                return N
            if X == NFT and Y == T:
                return FT
            if X == NFT and Y == B:
                return FT
            if X == NFT and Y == TB:
                return FT
            if X == NFT and Y == NTB:
                return FT
            if X == NFT and Y == NB:
                return FT
            if X == NFT and Y == FT:
                return FT
            if X == NFT and Y == NFT:
                return FT
            if X == NFT and Y == NF:
                return NF
            if X == NFT and Y == F:
                return NF
            if X == NFT and Y == N:
                return N
            if X == NF and Y == T:
                return FT
            if X == NF and Y == B:
                return FT
            if X == NF and Y == TB:
                return FT
            if X == NF and Y == NTB:
                return FT
            if X == NF and Y == NB:
                return FT
            if X == NF and Y == FT:
                return FT
            if X == NF and Y == NFT:
                return NFT
            if X == NF and Y == NF:
                return FT
            if X == NF and Y == F:
                return NFT
            if X == NF and Y == N:
                return N
            if X == F and Y == T:
                return FT
            if X == F and Y == B:
                return FT
            if X == F and Y == TB:
                return FT
            if X == F and Y == NTB:
                return FT
            if X == F and Y == NB:
                return FT
            if X == F and Y == FT:
                return FT
            if X == F and Y == NFT:
                return FT
            if X == F and Y == NF:
                return FT
            if X == F and Y == F:
                return FT
            if X == F and Y == N:
                return N
            if X == N and Y == T:
                return FT
            if X == N and Y == B:
                return FT
            if X == N and Y == TB:
                return FT
            if X == N and Y == NTB:
                return FT
            if X == N and Y == NB:
                return FT
            if X == N and Y == FT:
                return FT
            if X == N and Y == NFT:
                return FT
            if X == N and Y == NF:
                return FT
            if X == N and Y == F:
                return FT
            if X == N and Y == N:
                return FT

print("Conditional (10-valued Belikov-Loginov)")
for X in V:
    for Y in V:
        print("(" + str(X) + "," + str(Y) + ")" + "--->" + str(then(X,Y)))

print("-------------------------------Counterexamples--------------------------------")

print("<<<<<Axioms for R>>>>>")
print("----Implicative fragment----")

print("Reflexivity:")

for A in V:
    if str(taut(then(A,A)))=="invalid":
        print(str(A))

print("Prefixing:")
for A in V:
    for C in V:
        for E in V:
            if str(then(then(A,C),then(then(E,A),then(E,C)))) == "invalid":
                print("("+ str(A) + "," + str(C) + "," + str(E) + ")")

print("Suffixing:")
for A in V:
    for C in V:
        for E in V:
            if str(then(then(A,C),then(then(C,E),then(A,E)))) == "invalid":
                print("("+ str(A) + "," + str(C) + "," + str(E) + ")")

print("Contraction:")
for A in V:
    for C in V:
        if str(taut(then(then(A,then(A,C)),then(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Self Distribution:")
for A in V:
    for E in V:
        for C in V:
            if str(taut(then(then(A,then(E,C)), then(then(A,E),then(A,C))))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("Permutation:")
for A in V:
    for E in V:
        for C in V:
            if str(taut(then(then(A,then(E,C)),then(E,then(A,C))))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("Assertion:")
for A in V:
    for C in V:
        if str(taut(then(A,then(then(A,C),C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Modus Ponens:")
for A in V:
    for C in V:
        if str(hence(wedge(A,then(A,C)),C))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("----Positive fragment----")

print("Simplification 1:")
for A in V:
    for C in V:
        if str(taut(then(wedge(A,C),A)))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Simplification 2:")
for A in V:
    for C in V:
        if str(taut(then(wedge(A,C),C)))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("And-Composition:")
for A in V:
    for C in V:
        for E in V:
            if str(taut(then(wedge(then(A,C),then(A,E)),then(A,wedge(C,E)))))=="invalid":
                print("(" + str(A) + "," + str(C) + "," + str(E) + ")")

print("Addition 1:")
for A in V:
    for C in V:
        if str(taut(then(A, vee(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Addition 2:")
for A in V:
    for C in V:
        if str(taut(then(C, vee(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Or-Composition:")
for A in V:
    for E in V:
        for C in V:
            if str(taut(then(wedge(then(A,C), then(E,C)), then(vee(A,E), C)))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("Distribution:")
for A in V:
    for E in V:
        for C in V:
            if str(taut(then(wedge(A,vee(E,C)),vee(wedge(A,E),C)))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("----Negative fragment:")

print("Reductio:")
for A in V:
    if str(taut(then(then(A,neg(A)),neg(A)))) == "invalid":
        print(str(A))

print("Intuitionistic Contraposition:")
for A in V:
    for C in V:
        if str(hence(then(A,neg(C)),then(C,neg(A))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Double Negation Elimination:")
for A in V:
    if str(taut(then(neg(neg(A)),A)))=="invalid":
        print(str(A))

print("Double Negation Introduction:")
for A in V:
    if str(taut(then(A,neg(neg(A)))))=="invalid":
        print(str(A))

print("----Connexive theses----")


print("Aristotle's Thesis:")

for A in V:
    if str(taut(neg(then(A,neg(A)))))=="invalid":
        print(str(A))

print("Aristotle variant:")
for A in V:
    if str(taut(neg(then(neg(A),A))))=="invalid":
        print(str(A))

print("Boethius' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(then(A,C),neg(then(A,neg(C)))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Symmetry of the Conditional:")

for A in V:
    for C in V:
        if str(taut(then(then(A,C),then(C,A)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Converse of Boethius' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(neg(then(A,neg(C))),then(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Variant of Boethius' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(then(A,neg(C)),neg(then(A,C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Converse of Variant of Boethius' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(neg(then(A,C)),then(A,neg(C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Francez' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(then(neg(A),C),neg(then(A,C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Variant of Francez' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(then(A,C),neg(then(neg(A),C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Converse of Francez' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(neg(then(A,C)),then(neg(A),C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Converse of Variant of Francez' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(neg(then(neg(A),C)), then(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Aristotle's Second Thesis:")

for A in V:
    for C in V:
        if str(taut(neg(wedge(then(A,C),then(neg(A),C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Abelard's First Principle:")

for A in V:
    for C in V:
        if str(taut(neg(wedge(then(A,C),then(A,neg(C)))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Abelard's Second Principle:")

for A in V:
    for C in V:
        if str(taut(neg(then(A,neg(C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")


print("----Other principles----")


print("Mingle:")
for A in V:
    if str(taut(then(A,then(A,A))))=="invalid":
        print(str(A))

print("Positive Paradox:")
for A in V:
    for C in V:
        if str(taut(then(A,then(C,A))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Negative Paradox:")
for A in V:
    for C in V:
        if str(taut(then(A,then(neg(A),C))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Paradox of Necessity:")
for A in V:
    for C in V:
        if str(taut(then(A,then(C,C))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Explosion:")

for A in V:
    for C in V:
        if str(taut(then(wedge(A,neg(A)),C))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Implosion:")

for A in V:
    for C in V:
        if str(taut(then(A,vee(C,neg(C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Antilogism:")
for A in V:
    for E in V:
        for C in V:
            if str(hence(then(wedge(A,E),C),then(wedge(A,neg(C)),neg(E))))=="invalid":
                print("("+str(A)+","+str(E)+","+str(C)+")")

print("False Antecedent:")

for A in V:
    for C in V:
        if str(hence(neg(A),then(A,C))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Counterexample:")

for A in V:
    for C in V:
        if str(hence(neg(then(A,C)),wedge(A,neg(C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("True Consequent:")

for A in V:
    for C in V:
        if str(hence(C,then(A,C))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")


print("Modus Tollens:")
for A in V:
    for C in V:
        if str(hence(wedge(neg(C),then(A,C)),neg(A)))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Transitivity (Conjunctive Syllogism):")

for A in V:
    for E in V:
        for C in V:
            if str(hence(wedge(then(A,E),then(E,C)),then(A,C)))=="invalid":
                print("("+str(A)+","+str(E)+","+str(C)+")")

print("Monotonicity:")

for A in V:
    for E in V:
        for C in V:
            if str(taut(then(then(A,C),then(wedge(A,E),C)))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("Pseudo Modus Ponens:")

for A in V:
    for C in V:
        if str(taut(then(wedge(then(A,C),A), C))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Rule Affixing:")

for A in V:
    for G in V:
        for C in V:
            for E in V:
                if str(hence(wedge(then(A,G),then(C,E)),then(then(G,C),then(A,E)))) == "invalid":
                    print("(" + str(A) + "," + str(G) + "," + str(C) + "," + str(E) + ")")

print("Affixing:")

for A in V:
    for G in V:
        for C in V:
            for E in V:
                if str(taut(then(wedge(then(A,G),then(C,E)),then(then(G,C),then(A,E))))) == "invalid":
                    print("(" + str(A) + "," + str(G) + "," + str(C) + "," + str(E) + ")")



print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Another connexive 10-valued conditional >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

for X in V:
    for Y in V:
        def then(X,Y):
            if X == T and Y == T:
                return T
            if X == T and Y == B:
                return N
            if X == T and Y == TB:
                return N
            if X == T and Y == NTB:
                return N
            if X == T and Y == NB:
                return N
            if X == T and Y == FT:
                return N
            if X == T and Y == NFT:
                return N
            if X == T and Y == NF:
                return N
            if X == T and Y == F:
                return N
            if X == T and Y == N:
                return N
            if X == B and Y == T:
                return T
            if X == B and Y == B:
                return FT
            if X == B and Y == TB:
                return NFT
            if X == B and Y == NTB:
                return NF
            if X == B and Y == NB:
                return F
            if X == B and Y == FT:
                return N
            if X == B and Y == NFT:
                return N
            if X == B and Y == NF:
                return N
            if X == B and Y == F:
                return N
            if X == B and Y == N:
                return N
            if X == TB and Y == T:
                return T
            if X == TB and Y == B:
                return FT
            if X == TB and Y == TB:
                return FT
            if X == TB and Y == NTB:
                return NF
            if X == TB and Y == NB:
                return NF
            if X == TB and Y == FT:
                return N
            if X == TB and Y == NFT:
                return N
            if X == TB and Y == NF:
                return N
            if X == TB and Y == F:
                return N
            if X == TB and Y == N:
                return N
            if X == NTB and Y == T:
                return T
            if X == NTB and Y == B:
                return FT
            if X == NTB and Y == TB:
                return NFT
            if X == NTB and Y == NTB:
                return FT
            if X == NTB and Y == NB:
                return NFT
            if X == NTB and Y == FT:
                return N
            if X == NTB and Y == NFT:
                return N
            if X == NTB and Y == NF:
                return N
            if X == NTB and Y == F:
                return N
            if X == NTB and Y == N:
                return N
            if X == NB and Y == T:
                return T
            if X == NB and Y == B:
                return FT
            if X == NB and Y == TB:
                return FT
            if X == NB and Y == NTB:
                return FT
            if X == NB and Y == NB:
                return FT
            if X == NB and Y == FT:
                return N
            if X == NB and Y == NFT:
                return N
            if X == NB and Y == NF:
                return N
            if X == NB and Y == F:
                return N
            if X == NB and Y == N:
                return N
            if X == FT and Y == T:
                return T
            if X == FT and Y == B:
                return B
            if X == FT and Y == TB:
                return TB
            if X == FT and Y == NTB:
                return NTB
            if X == FT and Y == NB:
                return NB
            if X == FT and Y == FT:
                return FT
            if X == FT and Y == NFT:
                return NFT
            if X == FT and Y == NF:
                return NF
            if X == FT and Y == F:
                return F
            if X == FT and Y == N:
                return N
            if X == NFT and Y == T:
                return FT
            if X == NFT and Y == B:
                return FT
            if X == NFT and Y == TB:
                return FT
            if X == NFT and Y == NTB:
                return FT
            if X == NFT and Y == NB:
                return FT
            if X == NFT and Y == FT:
                return FT
            if X == NFT and Y == NFT:
                return FT
            if X == NFT and Y == NF:
                return NF
            if X == NFT and Y == F:
                return NF
            if X == NFT and Y == N:
                return N
            if X == NF and Y == T:
                return FT
            if X == NF and Y == B:
                return FT
            if X == NF and Y == TB:
                return FT
            if X == NF and Y == NTB:
                return FT
            if X == NF and Y == NB:
                return FT
            if X == NF and Y == FT:
                return FT
            if X == NF and Y == NFT:
                return FT
            if X == NF and Y == NF:
                return FT
            if X == NF and Y == F:
                return FT
            if X == NF and Y == N:
                return FT
            if X == F and Y == T:
                return FT
            if X == F and Y == B:
                return FT
            if X == F and Y == TB:
                return FT
            if X == F and Y == NTB:
                return FT
            if X == F and Y == NB:
                return FT
            if X == F and Y == FT:
                return FT
            if X == F and Y == NFT:
                return FT
            if X == F and Y == NF:
                return FT
            if X == F and Y == F:
                return FT
            if X == F and Y == N:
                return FT
            if X == N and Y == T:
                return FT
            if X == N and Y == B:
                return FT
            if X == N and Y == TB:
                return FT
            if X == N and Y == NTB:
                return FT
            if X == N and Y == NB:
                return FT
            if X == N and Y == FT:
                return FT
            if X == N and Y == NFT:
                return FT
            if X == N and Y == NF:
                return FT
            if X == N and Y == F:
                return FT
            if X == N and Y == N:
                return FT

print("Conditional (variant of 10-valued Belikov-Loginov)")
for X in V:
    for Y in V:
        print("(" + str(X) + "," + str(Y) + ")" + "--->" + str(then(X,Y)))

print("-------------------------------Counterexamples--------------------------------")

print("<<<<<Axioms for R>>>>>")
print("----Implicative fragment----")

print("Reflexivity:")

for A in V:
    if str(taut(then(A,A)))=="invalid":
        print(str(A))

print("Prefixing:")
for A in V:
    for C in V:
        for E in V:
            if str(then(then(A,C),then(then(E,A),then(E,C)))) == "invalid":
                print("("+ str(A) + "," + str(C) + "," + str(E) + ")")

print("Suffixing:")
for A in V:
    for C in V:
        for E in V:
            if str(then(then(A,C),then(then(C,E),then(A,E)))) == "invalid":
                print("("+ str(A) + "," + str(C) + "," + str(E) + ")")

print("Contraction:")
for A in V:
    for C in V:
        if str(taut(then(then(A,then(A,C)),then(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Self Distribution:")
for A in V:
    for E in V:
        for C in V:
            if str(taut(then(then(A,then(E,C)), then(then(A,E),then(A,C))))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("Permutation:")
for A in V:
    for E in V:
        for C in V:
            if str(taut(then(then(A,then(E,C)),then(E,then(A,C))))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("Assertion:")
for A in V:
    for C in V:
        if str(taut(then(A,then(then(A,C),C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Modus Ponens:")
for A in V:
    for C in V:
        if str(hence(wedge(A,then(A,C)),C))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("----Positive fragment----")

print("Simplification 1:")
for A in V:
    for C in V:
        if str(taut(then(wedge(A,C),A)))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Simplification 2:")
for A in V:
    for C in V:
        if str(taut(then(wedge(A,C),C)))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("And-Composition:")
for A in V:
    for C in V:
        for E in V:
            if str(taut(then(wedge(then(A,C),then(A,E)),then(A,wedge(C,E)))))=="invalid":
                print("(" + str(A) + "," + str(C) + "," + str(E) + ")")

print("Addition 1:")
for A in V:
    for C in V:
        if str(taut(then(A, vee(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Addition 2:")
for A in V:
    for C in V:
        if str(taut(then(C, vee(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Or-Composition:")
for A in V:
    for E in V:
        for C in V:
            if str(taut(then(wedge(then(A,C), then(E,C)), then(vee(A,E), C)))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("Distribution:")
for A in V:
    for E in V:
        for C in V:
            if str(taut(then(wedge(A,vee(E,C)),vee(wedge(A,E),C)))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("----Negative fragment:")

print("Reductio:")
for A in V:
    if str(taut(then(then(A,neg(A)),neg(A)))) == "invalid":
        print(str(A))

print("Intuitionistic Contraposition:")
for A in V:
    for C in V:
        if str(hence(then(A,neg(C)),then(C,neg(A))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Double Negation Elimination:")
for A in V:
    if str(taut(then(neg(neg(A)),A)))=="invalid":
        print(str(A))

print("Double Negation Introduction:")
for A in V:
    if str(taut(then(A,neg(neg(A)))))=="invalid":
        print(str(A))

print("----Connexive theses----")


print("Aristotle's Thesis:")

for A in V:
    if str(taut(neg(then(A,neg(A)))))=="invalid":
        print(str(A))

print("Aristotle variant:")
for A in V:
    if str(taut(neg(then(neg(A),A))))=="invalid":
        print(str(A))

print("Boethius' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(then(A,C),neg(then(A,neg(C)))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Symmetry of the Conditional:")

for A in V:
    for C in V:
        if str(taut(then(then(A,C),then(C,A)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Converse of Boethius' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(neg(then(A,neg(C))),then(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Variant of Boethius' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(then(A,neg(C)),neg(then(A,C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Converse of Variant of Boethius' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(neg(then(A,C)),then(A,neg(C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Francez' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(then(neg(A),C),neg(then(A,C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Variant of Francez' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(then(A,C),neg(then(neg(A),C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Converse of Francez' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(neg(then(A,C)),then(neg(A),C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Converse of Variant of Francez' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(neg(then(neg(A),C)), then(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Aristotle's Second Thesis:")

for A in V:
    for C in V:
        if str(taut(neg(wedge(then(A,C),then(neg(A),C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Abelard's First Principle:")

for A in V:
    for C in V:
        if str(taut(neg(wedge(then(A,C),then(A,neg(C)))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Abelard's Second Principle:")

for A in V:
    for C in V:
        if str(taut(neg(then(A,neg(C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")


print("----Other principles----")


print("Mingle:")
for A in V:
    if str(taut(then(A,then(A,A))))=="invalid":
        print(str(A))

print("Positive Paradox:")
for A in V:
    for C in V:
        if str(taut(then(A,then(C,A))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Negative Paradox:")
for A in V:
    for C in V:
        if str(taut(then(A,then(neg(A),C))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Paradox of Necessity:")
for A in V:
    for C in V:
        if str(taut(then(A,then(C,C))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Explosion:")

for A in V:
    for C in V:
        if str(taut(then(wedge(A,neg(A)),C))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Implosion:")

for A in V:
    for C in V:
        if str(taut(then(A,vee(C,neg(C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Antilogism:")
for A in V:
    for E in V:
        for C in V:
            if str(hence(then(wedge(A,E),C),then(wedge(A,neg(C)),neg(E))))=="invalid":
                print("("+str(A)+","+str(E)+","+str(C)+")")

print("False Antecedent:")

for A in V:
    for C in V:
        if str(hence(neg(A),then(A,C))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Counterexample:")

for A in V:
    for C in V:
        if str(hence(neg(then(A,C)),wedge(A,neg(C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("True Consequent:")

for A in V:
    for C in V:
        if str(hence(C,then(A,C))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")


print("Modus Tollens:")
for A in V:
    for C in V:
        if str(hence(wedge(neg(C),then(A,C)),neg(A)))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Transitivity (Conjunctive Syllogism):")

for A in V:
    for E in V:
        for C in V:
            if str(hence(wedge(then(A,E),then(E,C)),then(A,C)))=="invalid":
                print("("+str(A)+","+str(E)+","+str(C)+")")

print("Monotonicity:")

for A in V:
    for E in V:
        for C in V:
            if str(taut(then(then(A,C),then(wedge(A,E),C)))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("Pseudo Modus Ponens:")

for A in V:
    for C in V:
        if str(taut(then(wedge(then(A,C),A), C))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Rule Affixing:")

for A in V:
    for G in V:
        for C in V:
            for E in V:
                if str(hence(wedge(then(A,G),then(C,E)),then(then(G,C),then(A,E)))) == "invalid":
                    print("(" + str(A) + "," + str(G) + "," + str(C) + "," + str(E) + ")")

print("Affixing:")

for A in V:
    for G in V:
        for C in V:
            for E in V:
                if str(taut(then(wedge(then(A,G),then(C,E)),then(then(G,C),then(A,E))))) == "invalid":
                    print("(" + str(A) + "," + str(G) + "," + str(C) + "," + str(E) + ")")
