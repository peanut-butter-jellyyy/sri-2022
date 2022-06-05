


import math
from pydoc import doc
import spacy

class Document:
    def __init__(self,id = -1):
        self.id = id
        self.body = ""
        self.tokens = []
        self.terms_vector = {}
        self.weights = []
        self.max_freq = 1
        
class Query:
    def __init__(self,id = -1):
        self.nlp = spacy.load('en_core_web_sm')
        self.id = id
        self.body = ""
        self.tokens = []
        self.terms_vector = {}
        self.weights = []
        self.max_freq = 1
        
    def tokenize(self):
        self.nlp.max_length = 5030000
        self.tokens = self.nlp(self.body)
        
        
    def lemmatize(self):
        punctuations="?:!.,;"
        for token in self.tokens:
            lemma = token.lemma_
            aux = lemma.split(' ')
            if len(aux)>1:
                continue
            #filtering stopwords
            lexeme = self.nlp.vocab[lemma]
            if not lexeme.is_stop and lemma not in punctuations:
                #Frequency of the term in query
                try:
                    self.terms_vector[lemma] += 1
                    
                    if self.terms_vector[lemma] > self.max_freq:
                        self.max_freq = self.terms_vector[lemma]
                except KeyError:
                    self.terms_vector[lemma] = 1
                    
    def  set_weight_values(self,document,corpus,alpha = 0.5):
        for term in document.terms_vector.keys():
            tf,idf = 0,0
            if term in self.terms_vector.keys():
                tf = self.terms_vector[term] / self.max_freq
                
                if term in corpus.n_i.keys():
                    idf = math.log(corpus.N/ corpus.n_i[term])
            
            w = (alpha + ((1-alpha)*tf))*idf
            self.weights.append(w)
        
    
    
class Corpus:
    def __init__(self, document_list):
        self.documents = document_list
        self.nlp = spacy.load('en_core_web_sm')
        #total number of documents
        self.N = len(document_list)
        #number of documents where term i appear
        self.n_i = {}
        
        
        
        
    def tokenize(self):
        self.nlp.max_length = 5030000
        for document in self.documents:
            document.tokens = self.nlp(document.body)
        
        
    def lemmatize(self):
        punctuations="?:!.,;"
        for document in self.documents:
            for token in document.tokens:
                lemma = token.lemma_
                aux = lemma.split(' ')
                if len(aux)>1:
                    continue
                #filtering stopwords
                lexeme = self.nlp.vocab[lemma]
                if not lexeme.is_stop and lemma not in punctuations:
                    #Frequency of the term in the document
                    try:
                        document.terms_vector[lemma] += 1
                        
                        if document.terms_vector[lemma] > document.max_freq:
                            document.max_freq = document.terms_vector[lemma]
                    except KeyError:
                        document.terms_vector[lemma] = 1
                        
    def set_freq_values(self):
        for document in self.documents:
            for term in document.terms_vector.keys():
                try:
                    self.n_i[term] += 1
                except KeyError:
                    self.n_i[term] = 1
                    
                    
    def set_weight_values(self):
        for document in self.documents:
            for term in document.terms_vector.keys():
                tf = document.terms_vector[term] / document.max_freq
                idf = math.log(self.N/self.n_i[term])
                document.weights.append(tf*idf)
          
        
        
    
                    
                    
                
                
                
                
                
                
                        
        