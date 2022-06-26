def precision(rr,ri):
    try:
        r = len(rr)/ len(rr | ri)
        return r
    except:
        return 0 


def recall(rr,nr):
    try:
        r = len(rr)/ len(rr | nr)
        return r
    except:
        return 0 

def f(beta,p,r):
    try:
        n = (1+beta**2)
        d = (1/r)+((beta**2)/r)
        return n/d
    except:
        return 0
    
def f1(p,r):
    try:
        x = (1/p) + 1/r
        return 2/x
    except:
        return 0