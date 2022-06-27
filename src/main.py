import pickle
import os
from datasets_utils import get_docs,get_queries,get_relevancies
from structs import Corpus
from vectorialModel import run_vectorial
from booleanModel import run_boolean
from utils import text_processor
import ir_datasets
import spacy

    

def analize_dataset(name):
    
    dataset = ir_datasets.load(name)
    
    document_list = get_docs(dataset,name)
    queries = get_queries(dataset)
    relevancies = get_relevancies(dataset)
    
    corpus = Corpus(document_list)
    
    _file = name + '.pickle'
    if os.path.isfile(_file):
        print('loading')
        with open(_file,'rb') as infile:
            corpus,queries = pickle.load(infile)
    else:
        text_processor(corpus,queries)
        with open(_file,'wb') as outfile:
            pickle.dump((corpus,queries),outfile)

    print('------Dataset '+ name + '------')
    run_vectorial(corpus,queries,relevancies)
    
    run_boolean(corpus,queries,relevancies)
        
    

if __name__ == '__main__':
   
    analize_dataset('cranfield')
    analize_dataset('vaswani')
    

    
    
    
    
    
    
    
    
    
    
    

    

    
