from measures import eval_measures

def run_boolean(corpus,queries,relevancies,oneQ=False):
    
    recovered = recover(corpus, queries)
    _result = ""
    
    if oneQ:
        _result += "Documents by id retrieved using Boolean Model \n"
        for q in queries:
            try:
                _result += " ".join(str(x) for x in recovered[q.id])
            except:
                _result += "Nothing was retrieved\n"
            
        return _result
    
    p,r,f,f1 = eval_measures(queries,recovered,relevancies,1.2)

    
    _result += "Boolean Model Evaluation\n"
    _result += "Precision: "+ str(p) +"\n"
    _result += "Recall: " + str(r) +"\n" 
    _result += "F metric: " + str(f) +"\n"
    _result += "F1 metric: "+ str(f1)+"\n"

    return _result
    
    
    
    
  



def recover(corpus,queries):
    recovered = {}

    for document in corpus.documents:
        for query in queries:
            qlen = len(query.terms_vector.keys())
            count = qlen
            for qterm in query.terms_vector.keys():
                if count < qlen:
                    break
                
                if qterm in document.terms_vector.keys():
                    count
                else:
                    count -= 1
            
            if count == qlen:
                try:
                    recovered[query.id].add(document.id)
                except:
                    recovered[query.id] = set()
                    recovered[query.id].add(document.id)
                    
        
    return recovered
