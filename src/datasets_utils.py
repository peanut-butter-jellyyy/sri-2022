from structs import Document, Query

def get_docs(dataset,name):
    document_list = []
    for doc in dataset.docs_iter():
        if name == 'cranfield':
            body = doc.title + doc.text
        else:
            body = doc.text
        
        document_list.append(Document(int(doc.doc_id),body))
        
    return document_list
        
def get_queries(dataset):
    queries = []
    for q in dataset.queries_iter():
        queries.append(Query(int(q.query_id),q.text))
        
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
