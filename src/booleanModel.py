from measures import precision,recall,f,f1


def run_boolean(corpus,queries,relevancies):
    return


def get_key(dict,value):
    values = dict.values()
    keys = dict.keys()
    
    pos = values.index(value)
    return keys[pos]


def prediction(queries,corpus,relevancies,beta=1):
    docs_dict = corpus.boolean_Dict
    len_terms = len(corpus.terms)
    recovered = {}
    _precision,_recall,_f,_f1 = 0,0,0,0
    
    for query in queries:
        rank_dict = {}
        rank_list = []
        
        for doc_id in docs_dict.keys():
            count = 0
            
            for i in range(len_terms):
                if query.boolean_weight == docs_dict[doc_id]:
                    count += 1
            rank_dict[doc_id] = count
            rank_list = count
            
        #ordenando por ranking
        rank_list = sorted(rank_list, reverse=True)
        for i, value in enumerate(rank_list):
            if i == 0:
                rel = value
            else:
                if value < rel:
                    break
            
            if rel > 0: 
                key = get_key(rank_dict,rel)
                try:
                    recovered[query.id].append(key)
                except:
                    recovered[query.id] = set()
                    recovered[query.id].append(key)
                rank_dict.pop(key)
            
                
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
        
        