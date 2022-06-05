from parse import parse_documents, parse_queries,parse_relevancies
from structs import Corpus
from evaluation import evaluate_metrics

if __name__ == '__main__':
    #_docs_path = ("test_docs.txt")
    #_queries_path = ("test_queries.txt")
    #_relevancies_path = ("test_relevancies.txt")
    
    _docs_path = ("cran.all.1400")
    _queries_path = ("cran.qry")
    _relevancies_path = ("cranqrel")
    
    document_list = parse_documents(_docs_path)
    queries = parse_queries(_queries_path)
    relevancies = parse_relevancies(_relevancies_path) 
    
    corpus = Corpus(document_list)
    corpus.tokenize()
    corpus.lemmatize()
    corpus.set_freq_values()
    corpus.set_weight_values()
    
    for query in queries:
        query.tokenize()
        query.lemmatize()
    
    p,r,f,f1 = evaluate_metrics(corpus,queries,relevancies,1.2)
    
    print("------Evaluation------")
    print("Precision: ",p)
    print("Recall: ",r)
    print("F metric: ",f)
    print("F1 metric: ",f1)
    
    
    
    
    #print("-----------Queries------------------------")
    #for q in queries:
    #    q.tokenize()
    #    q.lemmatize()
    #    print(q.tokens)
    #    print("--------------------------------")
    #    print(q.terms_vector)
    #    q.set_weight_values(corpus)
    #    print("--------------------------------")
    #    print(q.weights)
    #    print("######################################################")
         
    #print("-----------Documents------------------------")
    #for d in document_list:
    #    print(d.terms_vector)
    #    print("--------------------------------")
    #    print(d.weights)
    #    print("######################################################")
        
        
    