from structs import Document, Query
import spacy

def get_docs(dataset):
    document_list = []
    for doc in dataset.docs_iter():
        body = doc.title + doc.text
        document_list.append(Document(int(doc.doc_id),body))
        
    return document_list
        
def get_queries(dataset,n):
    queries = []
    nlp = n
    for q in dataset.queries_iter():
        queries.append(Query(int(q.query_id),q.text,nlp=nlp))
        
    return queries


def get_relevancies(dataset):
    relevancies = {}
    for r in dataset.qrels_iter():
        try:
            relevancies[int(r.query_id)].add(int(r.doc_id))
        except:
            relevancies[int(r.query_id)] = set()
            relevancies[int(r.query_id)].add(int(r.doc_id))
            
    return relevancies
