import math
from operator import le
from re import X

from sqlalchemy import true

def sim(doc_weight, query_weight):
    length = len(doc_weight)
    numerator = 0
    d_doc = 0
    d_q = 0
    denominator = 0
    
    for i in range(0,length):
        numerator += doc_weight[i] * query_weight[i]
        d_doc = math.pow(doc_weight[i],2)
        d_q = math.pow(query_weight[i],2) 
         
    if d_doc == 0 or d_q == 0:
        return 0
    
    denominator = math.sqrt(d_doc) * math.sqrt(d_q)
    return numerator/denominator
     
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


def evaluate_metrics(corpus,queries,relevancies,beta=1):
    recovered = {}
    _precision,_recall,_f,_f1 = 0,0,0,0
    
    for query in queries:
        for doc in corpus.documents:
            query.set_weight_values(doc,corpus)
            _sim = sim(doc.weights,query.weights)
            
            if _sim > 0.1:
                try:
                    recovered[query.id].add(doc.id)
                except KeyError:
                    recovered[query.id] = set()
                    recovered[query.id].add(doc.id)
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