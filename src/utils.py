def text_processor(corpus,queries,onlyQ=False):
    if not onlyQ:
        corpus.tokenize()
        corpus.stemmize()
        corpus.lemmatize_()
    
    
    for query in queries:
        query.tokenize()
        query.stemmize()
        query.lemmatize_()