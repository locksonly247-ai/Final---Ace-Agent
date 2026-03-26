def american_to_prob(odds):
    o = float(odds)
    return 100/(o+100) if o > 0 else abs(o)/(abs(o)+100)

def calc_edge(model_prob, vegas_prob):
    return round((model_prob - vegas_prob)*100, 2)
