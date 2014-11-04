import Pmf

hours_invested = [2, 8, 10, 6, 6, 5, 7, 8, 9, 10, 4, 6, 8, 9, 10, 6, 8, 9, 10]

def pmf_mean(pmf):
    mean = 0
    for hour, probability in pmf.Items():
       mean += hour * probability
    return mean

def pmf_var(pmf):
    var = 0
    mean = pmf_mean(pmf)
    for hour, probability in pmf.Items():
       var += probability * ((hour - mean) ** 2)
    return var

hours_pmf = Pmf.MakePmfFromList(hours_invested)
if __debug__:
    assert pmf_mean(hours_pmf) == hours_pmf.Mean()
    assert pmf_var(hours_pmf) == hours_pmf.Var()
print "Pmf mean ", pmf_mean(hours_pmf), hours_pmf.Mean()
print "Pmf Variance ", pmf_var(hours_pmf), hours_pmf.Var()
