import Pmf
import Birth_Order

def pmf_mean(pmf):
    mean = 0
    for val, probability in pmf.Items():
       mean += val * probability
    return mean

def pmf_var(pmf):
    var = 0
    mean = pmf_mean(pmf)
    for val, probability in pmf.Items():
       var += probability * ((val - mean) ** 2)
    return var

def pmf_mode(pmf):
    sorted_list = sorted(pmf.Items(), key=lambda x: x[1])
    max_item = sorted_list[-1]
    return max_item


first_born_pmf = Pmf.MakePmfFromList(Birth_Order.birth_ord_list[0].prgweeks)

assert pmf_mean(first_born_pmf) == first_born_pmf.Mean()
assert pmf_var(first_born_pmf) == first_born_pmf.Var()

print "Pmf mean ", pmf_mean(first_born_pmf)
print "Pmf Variance ", pmf_var(first_born_pmf)

print "Week in which first borns arrive with max probability: ", pmf_mode(first_born_pmf)
