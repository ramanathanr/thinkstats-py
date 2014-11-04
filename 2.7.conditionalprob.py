import Pmf
import Birth_Order
import myplot

def pmf_conditional(pmf, week):
    """
    Args:
    pmf - PMF of pregnancy weeks
    week - the current week of pregnancy

    Returns a PMF after removing from the distribution values prior to the given week
    """
    pmf_cond = pmf.Copy()
    for preg_week in pmf_cond.Values():
        if preg_week < week:
            pmf_cond.Remove(preg_week)
    pmf_cond.Normalize()
    return pmf_cond

def prob_conditional(pmf, week):
    """
    Args:
    pmf - PMF of pregnancy weeks
    week - the current week of pregnancy

    Returns the conditional probability of birth in the given week
    """
    pmf_cond = pmf_conditional(pmf, week)
    return pmf_cond.Prob(week)

first_born_prgweeks = Birth_Order.birth_ord_list[0].prgweeks
pmf_1st_born = Pmf.MakePmfFromList(first_born_prgweeks)
pmf_1st_born.Normalize()

cur_week = 39
pmf_1st_born_cond = pmf_conditional(pmf_1st_born, cur_week)
print "Probability of 1st child's birth in week %d is %.2f " % (cur_week, pmf_1st_born.Prob(cur_week))
print "Conditional probability of 1st child's birth in week %d is %.2f "\
                    % (cur_week, pmf_1st_born_cond.Prob(cur_week))


others_prgweeks = []
for bo in Birth_Order.birth_ord_list[1:]:
    others_prgweeks.extend(bo.prgweeks)

pmf_others = Pmf.MakePmfFromList(others_prgweeks)
pmf_others.Normalize()
pmf_others_cond = pmf_conditional(pmf_others, cur_week)

myplot.Pmfs([pmf_1st_born_cond, pmf_others_cond])
myplot.Show()