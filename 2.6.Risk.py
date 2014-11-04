import Pmf
import Birth_Order

def prob_early(pmf):
    """ Returns the probability of babies born in Week 37 or earlier
    """
    return prob_bin(pmf, 0, 37)

def prob_on_time(pmf):
    """ Returns the probability of babies born in Week 37 or earlier
    """
    return prob_bin(pmf, 38, 40)

def prob_late(pmf):
    """ Returns the probability of babies born in Week 37 or earlier
    """
    return prob_bin(pmf, 41)

def prob_bin(pmf, bin_low, bin_high=55):
    """ Returns the probability of values in the PMF for the given 'bin'/range
    """
    total_freq = pmf.Total()
    bin_freq_sum = 0
    for val, freq in pmf.Items():
        if val >= bin_low and val <= bin_high:
            bin_freq_sum += freq
    return float(bin_freq_sum) / total_freq

first_born_prgweeks = Birth_Order.birth_ord_list[0].prgweeks
pmf_first_born = Pmf.MakePmfFromList(first_born_prgweeks)
pmf_first_born.Normalize()

print "Probability of (1st born) babies born early [by week 37] %.2f " % prob_early(pmf_first_born)
print "Probability of (1st born) babies born on time [weeks 38 - 40] %.2f " % prob_on_time(pmf_first_born)
print "Probability of (1st born) babies born late [week 41 and after] %.2f " % prob_late(pmf_first_born)

others_prgweeks = []
for bo in Birth_Order.birth_ord_list[1:]:
    others_prgweeks.extend(bo.prgweeks)

pmf_others = Pmf.MakePmfFromList(others_prgweeks)
pmf_others.Normalize()

print ""
print "Probability of (not 1st born) babies born early [by week 37] %.2f " % prob_early(pmf_others)
print "Probability of (not 1st born) babies born on time [weeks 38 - 40] %.2f " % prob_on_time(pmf_others)
print "Probability of (not 1st born) babies born late [week 41 and after] %.2f " % prob_late(pmf_others)

all_live_borns = first_born_prgweeks[::]
all_live_borns.extend(others_prgweeks)

pmf_all_live = Pmf.MakePmfFromList(all_live_borns)
pmf_all_live.Normalize()

print ""
print "Probability of all babies born early [by week 37] %.2f " % prob_early(pmf_all_live)
print "Probability of all babies born on time [weeks 38 - 40] %.2f " % prob_on_time(pmf_all_live)
print "Probability of all babies born late [week 41 and after] %.2f " % prob_late(pmf_all_live)

print ""
prob_early_1stborn = prob_early(pmf_first_born)
prob_early_others = prob_early(pmf_others)
print "Relative risk of being born early for 1st borns : others  --> %.2f" % \
            (prob_early_1stborn / prob_early_others)

prob_ontime_1stborn = prob_on_time(pmf_first_born)
prob_ontime_others = prob_on_time(pmf_others)
print "Relative risk of being born on time for 1st borns : other --> %.2f" % \
            (prob_ontime_1stborn / prob_ontime_others)

prob_late_1stborn = prob_late(pmf_first_born)
prob_late_others = prob_late(pmf_others)
print "Relative risk of being late for 1st borns : other --> %.2f" % \
            (prob_late_1stborn / prob_late_others)
