def text_processor(corpus,queries):
    corpus.tokenize()
    print('tokenize done')
    corpus.lemmatize()
    print('lemmatize done')
    
    
    for query in queries:
        query.tokenize()
        query.lemmatize()