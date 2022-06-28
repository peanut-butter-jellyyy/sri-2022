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
    
def eval_measures(queries,recovered,relevancies,beta = 1):
    _precision,_recall,_f,_f1 = 0,0,0,0
    for query in queries:
        if query.id in recovered.keys() and query.id in relevancies.keys():             
                rr = relevancies[query.id] & recovered[query.id]         
                ri = recovered[query.id] - rr
                nr = relevancies[query.id] - rr         

                _precision += precision(rr,ri)
                _recall += recall(rr,nr)
                _f += f(beta,_precision,_recall)
                _f1 += f1(_precision,_recall)

    count = len(queries)
    return _precision/count,_recall/count, _f/count,_f1/count
