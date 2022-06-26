
import math
from operator import le
from cv2 import sort

import spacy

class Document:
    def __init__(self,id = -1,text=""):
        self.id = id
        self.body = text
        self.tokens = []
        self.terms_vector = {}
        self.weights = []
        self.boolean_weights = {}
        self.max_freq = 1
        
class Query:
    def __init__(self,id = -1,text = "",nlp = spacy.load('en_core_web_sm')):
        self.nlp = nlp
        self.id = id
        self.body = text
        self.tokens = []
        self.terms_vector = {}
        self.weights = []
        self.boolean_weight = []
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
        
        
    def set_boolean_weight(self,corpus):
        sorted_terms = sorted(self.terms)
        for term in sorted_terms:
            if term in self.terms_vector.keys():
                self.boolean_weight.append(1)
            else:
                self.boolean_weight.append(0)
                
        
    
class Corpus:
    def __init__(self, document_list, nlp = spacy.load('en_core_web_sm')):
        self.documents = document_list
        self.nlp = nlp
        #total number of documents
        self.N = len(document_list)
        #number of documents where term i appear
        self.n_i = {}
        self.terms = set()
        self.boolean_Dict = {}
        
        
        
        
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
                    self.terms.add(lemma)
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
          
        
        
    def set_boolean_weight(self):
        sorted_terms = sorted(self.terms)
        
        for document in self.documents:
            dummy_list = []
           
            for term in sorted_terms:
                if term in document.terms_vector.keys():
                    #document.boolean_weigth[term] = 1
                    dummy_list.append(1)
                else:
                    dummy_list.append(0)
                    
                    #document.boolean_weigth[term] = 0
            self.boolean_Dict[document.id] = dummy_list
                    
                    
                
                
                
                
                
                
                        
        