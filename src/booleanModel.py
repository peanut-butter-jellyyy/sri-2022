from measures import eval_measures
import pickle
import os

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

            
                             



#def prediction(corpus,queries,relevancies,beta=1):
#    docs_dict = corpus.boolean_Dict
#    len_terms = len(corpus.terms)
#    recovered = {}
#    _precision,_recall,_f,_f1 = 0,0,0,0
#    
#    for query in queries:
#        rank_dict = {}
#        rank_list = []
#        
#        #De esta forma se demora muuucho
#        ####query.set_boolean_weight(corpus)
#        ####
#        ####for doc_id in docs_dict.keys():
#        ####    count = 0
#        ####    
#        ####    for i in range(len_terms):
#        ####        if query.boolean_weight[i] == docs_dict[doc_id][i]:
#        ####            count += 1
#        ####    rank_dict[doc_id] = count
#        ####    rank_list.append(count)
#         
#                
#                 
#         
#            
#        #ordenando por ranking
#        rank_list = sorted(rank_list, reverse=True)
#        for i, value in enumerate(rank_list):
#            if i == 0:
#                rel = value
#            else:
#                if value < rel:
#                    break
#            
#            if rel >= len_terms/2: 
#                key = get_key(rank_dict,rel)
#                try:
#                    recovered[query.id].add(key)
#                except:
#                    recovered[query.id] = set()
#                    recovered[query.id].add(key)
#                rank_dict.pop(key)
#            
#                
#        if query.id in recovered.keys() and query.id in relevancies.keys():             
#            rr = relevancies[query.id] & recovered[query.id]         
#            ri = recovered[query.id] - rr
#            nr = relevancies[query.id] - rr         
#
#            _precision += precision(rr,ri)
#            _recall += recall(rr,nr)
#            _f += f(beta,_precision,_recall)
#            _f1 += f1(_precision,_recall)
#    
#    count = len(queries)
#    return _precision/count,_recall/count, _f/count,_f1/count       
#        
        