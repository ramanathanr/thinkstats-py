import Pmf

class_d = {
        7: 8, 
        12: 8, 
        17: 14, 
        22: 4, 
        27: 6, 
        32: 12, 
        37: 8, 
        42: 3, 
        47: 2
        }

def Bias_pmf(pmf):
    """
    Responses from students attending large classes are likely to be 
    oversampled resulting in a biased perception.
    The oversampling would be proportional to the size of the class. 
    So for the given Pmf with actual values, we apply the bias by simply 
    multiplying with the class size. 
    Returns the biased Pmf.

    Args:
    The Pmf of the actual values 

    Returns:
    Pmf with biased values
    """
    bias_pmf = pmf.Copy()  
    for val in bias_pmf.Values():
        bias_pmf.Mult(val, val)
    bias_pmf.Normalize()
    return bias_pmf

def Unbias_pmf(bias_pmf):
    """
    Returns a pmf after removing the bias due to oversampling from 
    the given pmf of class sizes. 

    Args:
    The Pmf of biased values

    Returns:
    Pmf with the biased values removed
    """
    unbias_pmf = bias_pmf.Copy()
    for val in unbias_pmf.Values():
        unbias_pmf.Mult(val, 1 / float(val))
    unbias_pmf.Normalize()
    return unbias_pmf

class_pmf = Pmf.MakePmfFromDict(class_d, "class_size_pmf")
print "Mean class size from Dean's data", class_pmf.Mean()

bias_pmf = Bias_pmf(class_pmf)
print "Mean of biased pmf of class data", bias_pmf.Mean()

unbias_pmf = Unbias_pmf(bias_pmf)
print "Mean of unbiased pmf of class size data", unbias_pmf.Mean()
 
