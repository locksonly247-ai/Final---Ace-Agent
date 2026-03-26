def win_probability(rank1, rank2):
    r1 = int(rank1.replace("#",""))
    r2 = int(rank2.replace("#",""))

    diff = r2 - r1
    prob = 1 / (1 + 10**(-diff/15))

    return round(prob, 3)
