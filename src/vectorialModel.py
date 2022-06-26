from evaluation import evaluate_metrics

def run_vectorial(corpus,queries,relevancies):

    corpus.set_freq_values()
    corpus.set_weight_values()

    p,r,f,f1 = evaluate_metrics(corpus,queries,relevancies,1.2)
    
    print("------Vectorial Model Evaluation------")
    print("Precision: ",p)
    print("Recall: ",r)
    print("F metric: ",f)
    print("F1 metric: ",f1)