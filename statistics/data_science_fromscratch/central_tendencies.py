def mean(xs:List[float]) -> float:
    return sum(xs)/len(xs)


def _median_odd(xs:List[float]) -> float:
    return sorted(xs)[len(xs)//2]

 
def _median_even(xs:List[float]) -> float:
    sorted_xs=sorted(xs)
    hi_midpoint=len(xs)//2
    median = (sorted_xs[hi_midpoint-1]+sorted_xs[hi_midpoint])/2   
    return median



def median(v:List[float])->float:
    if(len(v)%2==0):
        return _median_even(v)
    else:
        return _median_odd(v)