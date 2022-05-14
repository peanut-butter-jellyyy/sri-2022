#spaCy Code Initialization:
import spacy

nlp = spacy.load('en_core_web_sm')

#file1 = open("/home/sandra/Desktop/Proyecto Final SRI/PF SRI/Test Collections/cran/cran.all.1400","r+")
file1 = open("cran.all.1400","r+")


str1 = file1.read()
nlp.max_length = 5030000


doc = nlp(str1)
lemma_list = []

for token in doc:
    lemma_list.append(token.lemma_)
    
print("Tokenize+Lemmatize:")
print(lemma_list)
   
#Filter the stopword
filtered_sentence =[] 
for word in lemma_list:
    lexeme = nlp.vocab[word]
    if lexeme.is_stop == False:
        filtered_sentence.append(word) 
   
#Remove punctuation
punctuations="?:!.,;"
for word in filtered_sentence:
    if word in punctuations:
        filtered_sentence.remove(word)

print(" ")
print("Remove stopword & punctuation: ")
print(filtered_sentence)
