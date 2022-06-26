from datasets_utils import get_docs,get_queries,get_relevancies
from structs import Corpus
from vectorialModel import run_vectorial
from utils import text_processor
import ir_datasets
import spacy

    

        
    

if __name__ == '__main__':
   
    cranfield = ir_datasets.load('cranfield')
    nlp = spacy.load('en_core_web_sm')
    
    document_list = get_docs(cranfield)
    queries = get_queries(cranfield,nlp)
    relevancies = get_relevancies(cranfield)
    
    
    corpus = Corpus(document_list)
    
    text_processor(corpus,queries)
    
    run_vectorial(corpus,queries,relevancies)
    
    
    
    
    
    
    
    

    

    
