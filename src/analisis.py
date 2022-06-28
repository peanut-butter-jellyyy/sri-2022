import ir_datasets
import pickle
import os
from datasets_utils import get_docs, get_queries,get_relevancies
from structs import Corpus,Query
from booleanModel import run_boolean
from vectorialModel import run_vectorial
from utils import text_processor


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
    
    _result = ""
    _result += "------Dataset " + name + '------\n'
    _result += run_vectorial(corpus,queries,relevancies)
    _result += "\n"
    _result += run_boolean(corpus,queries,relevancies)
    
    return _result


        
def analize_single_query(name,query):
    
    dataset = ir_datasets.load(name)
    
    document_list = get_docs(dataset,name)
    queries = [Query(1,query)]
    
    
    
    corpus = Corpus(document_list)
    
    _file = name+'singleQ'+ '.pickle'
    if os.path.isfile(_file):
        print('loading')
        with open(_file,'rb') as infile:
            corpus = pickle.load(infile)
        text_processor(corpus,queries,onlyQ=True)
    else:
        text_processor(corpus,queries)
        with open(_file,'wb') as outfile:
            pickle.dump(corpus,outfile)
    
    _result = ""
    _result += "------Dataset " + name + '------\n'
    _result += run_vectorial(corpus,queries,relevancies=None,oneQ=True)
    _result += "\n"
    _result += run_boolean(corpus,queries,relevancies=None,oneQ=True)
    
    return _result