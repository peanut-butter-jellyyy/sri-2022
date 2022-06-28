def text_processor(corpus,queries,onlyQ=False):
    if not onlyQ:
        corpus.tokenize()
        print('tokenize done')
        corpus.stemmize()
        print('stemmize done')
        corpus.lemmatize_()
        print('lemmatize done')
    
    
    for query in queries:
        query.tokenize()
        query.stemmize()
        query.lemmatize_()