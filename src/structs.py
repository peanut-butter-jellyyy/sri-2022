
import math
import re
 
import spacy
from nltk import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from spacy.lang.en.stop_words import STOP_WORDS




class Document:
    def __init__(self,id = -1,text=""):
        self.id = id
        self.body = text
        self.tokens = []
        self.terms_vector = {}
        self.weights = []
        self.boolean_weight = {}
        self.max_freq = 1
        
class Query:
    def __init__(self,id = -1,text = ""):
        self.id = id
        self.body = text
        self.tokens = []
        self.terms_vector = {}
        self.weights = []
        self.boolean_weight = []
        self.max_freq = 1
        

    def tokenize(self):
        for token in re.split(r'\W+', self.body.replace('.', '')):
            if token != '':
                self.tokens.append(token)
        
    def stemmize(self):
        snowball = SnowballStemmer(language='english')
        for token in self.tokens:
            _stem = snowball.stem(token)
            if not _stem in STOP_WORDS:
                try:
                    self.terms_vector[_stem] += 1
                except:
                    self.terms_vector[_stem] = 1
                
                if self.terms_vector[_stem] > self.max_freq:
                    self.max_freq = self.terms_vector[_stem]
                    
    def lemmatize_(self):
        lemmatizer = WordNetLemmatizer()
        for token in self.tokens:
            lemma = lemmatizer.lemmatize(token)
            if not lemma in STOP_WORDS:
                try:
                    self.terms_vector[lemma] += 1
                except:
                    self.terms_vector[lemma] = 1
                    
                if self.terms_vector[lemma] > self.max_freq:
                    self.max_freq = self.terms_vector[lemma]
        
        
                    
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
        #total number of documents
        self.N = len(document_list)
        #number of documents where term i appear
        self.n_i = {}
        self.terms = set()
        
    
    def tokenize(self):
        for document in self.documents:
            for token in re.split(r'\W+', document.body.replace('.', '')):
                if token != '':
                    document.tokens.append(token)
            
    
    def stemmize(self):
        snowball = SnowballStemmer(language='english')
        for document in self.documents:
            for token in document.tokens:
                _stem = snowball.stem(token)
                if not _stem in STOP_WORDS:
                    try:
                        document.terms_vector[_stem]+=1
                    except:
                        self.terms.add(_stem)
                        document.terms_vector[_stem]=1
                        
                    if document.terms_vector[_stem] > document.max_freq:
                        document.max_freq = document.terms_vector[_stem]
        
    def lemmatize_(self):
        lemmatizer = WordNetLemmatizer()
        for document in self.documents:
            for token in document.tokens:
                lemma = lemmatizer.lemmatize(token)
                if not lemma in STOP_WORDS:
                    try:
                        document.terms_vector[lemma]+=1
                    except:
                        self.terms.add(lemma)
                        document.terms_vector[lemma]=1
                        
                    if document.terms_vector[lemma] > document.max_freq:
                        document.max_freq = document.terms_vector[lemma]
        
                        
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
          
        
                   
                       
                
                
                
                        
        