import matplotlib.pyplot as plt

def get_number_of_agents_have_a_target(t, agentMap):
    count = 0

    for key in agentMap:
        R = agentMap[key]

        for r in R:
            if r == t:
                count = count + 1

    return count

def get_guilt_probability(p,agentMap,S,T):
    agentGuiltValueMap = {}

    for agentKey in agentMap:
        R = agentMap[agentKey]

        NoGp = 0.0

        for t in S:
            if t in R:
                Vt = get_number_of_agents_have_a_target(t,agentMap)
                a = 1 - ((1 - p) / Vt)

                if NoGp == 0.0:
                    NoGp = a
                else:
                    NoGp = NoGp * a

        Gp = 1 - NoGp

        agentGuiltValueMap[agentKey] = Gp

    return agentGuiltValueMap

TT = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]

RR1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]

RR2 = ["A", "B", "C", "D", "E", "F", "G", "H"]

SS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]

agentMap = {"RR1" : RR1, "RR2" : RR2}
agentGPsMap = {"RR1" : [], "RR2" : []}

p = 0.0
ps = []

while True:
    ps.append(p)
    Gp = get_guilt_probability(p, agentMap, SS, TT)

    print(p, '->', Gp)

    for agentKey in agentMap:
        agentGPsMap[agentKey].append(Gp[agentKey])

    if p >= 1.0:
        break

    p = p + 0.01

i1 = agentGPsMap["RR1"]
i2 = agentGPsMap["RR2"]
plt.plot(ps, i1, color='g')
plt.plot(ps, i2, color='orange')
plt.xlabel('p')
plt.ylabel('Pr{Gi}')
plt.title('Guilt probability as a function of the guessing probability p')
plt.show()