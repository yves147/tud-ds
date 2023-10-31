N = 9

def zyklenschreibweise(permutation):
    cycles = []
    unknown = list(range(1, N + 1))
    j = 1

    while True:
        if j not in unknown:
            if len(unknown) == 0:
                cycles = [a[:-1] for a in cycles]
                break
            j = unknown[0]

        if j == permutation[j - 1]:
            unknown = [v for v in unknown if v != j]
            continue

        if cycles and j in cycles[-1]:
            unknown = [v for v in unknown if v != j]
            cycles[-1].append(permutation[j - 1])
            j = permutation[j - 1]
        else:
            unknown = [v for v in unknown if v != j]
            cycles.append([j, permutation[j - 1]])
            j = permutation[j - 1]

    return cycles

def zyklen(filename="file.txt"):
    permutationen = []
    with open(filename, "r") as file:
        for line in file:
            permutationStr = line.split()
            permutation = [int(eintrag) for eintrag in permutationStr]
            permutationen.append(permutation)
    return permutationen

def komposition(zyklus1, zyklus2):
    z = []
    for i in range(N):
        z.append(zyklus1[zyklus2[i] - 1])
    return z

result = zyklen()

def komposition_(n):
    if n - 1 < 0:
        return result[n]
    r = komposition(result[n - 1], result[n])
    result[n - 1] = r
    return komposition_(n - 1)

n = int(input("bis zu: "))
print("=>", zyklenschreibweise(komposition_(n - 1)))
