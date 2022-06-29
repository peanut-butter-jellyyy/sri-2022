from measures import eval_measures
import math


def run_vectorial(corpus,queries,relevancies,oneQ=False):

    corpus.set_freq_values()
    corpus.set_weight_values()

    recovered = recover(corpus,queries)
    _result = "" 
    
    if oneQ:
        _result += "Documents by id retrieved using Vectorial Model \n"
        for q in queries:
            try:
                _result += " ".join(str(x) for x in recovered[q.id])
            except:
                _result = "Nothing was retrieved"
            
        return _result
    
    
    p,r,f,f1 = eval_measures(queries,recovered,relevancies,1.2)
    
    
    _result += "Vectorial Model Evaluation\n"
    _result += "Precision: "+ str(p) +"\n"
    _result += "Recall: " + str(r) +"\n" 
    _result += "F metric: " + str(f) +"\n"
    _result += "F1 metric: "+ str(f1)+"\n"
    
    return _result



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
     



def recover(corpus,queries):
    recovered = {}
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
        
        dummy = set()
        for id in similarity.keys():
            _sim = similarity[id]
            if _sim >= (mean_sim/2):
                try:
                    recovered[query.id].add(id)
                except KeyError:
                    recovered[query.id] = set()
                    recovered[query.id].add(id)
    
    return recovered
