import math
from measures import precision,recall,f1,f


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
     



def evaluate_metrics(corpus,queries,relevancies,beta=1):
    recovered = {}
    _precision,_recall,_f,_f1 = 0,0,0,0
    similarity = {}
    total = 0
    count = 0
    mean_sim = 0
    for query in queries:
        for doc in corpus.documents:
            query.set_weight_values(doc,corpus)
            _sim = sim(doc.weights,query.weights)
            similarity[doc.id] = _sim
            if _sim > 0:
                total += _sim
                count += 1
            
        if count > 0:
            mean_sim = total/count  
        
        for id in similarity.keys():
            _sim = similarity[id]
            if _sim >= (mean_sim/2):
            #if _sim>0.1:
                try:
                    recovered[query.id].add(id)
                except KeyError:
                    recovered[query.id] = set()
                    recovered[query.id].add(id)
                    
        
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