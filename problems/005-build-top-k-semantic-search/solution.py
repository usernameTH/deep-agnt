import numpy as np



def top_k_search(query, documents, k):
    if k <= 0:
        return []

    scores = cosine_similarity(query, documents)
    k = min(k, len(scores))

    order = sorted(range(len(scores)), key=lambda i: (-scores[i], i))
    return [(int(i), float(scores[i])) for i in order[:k]]
    


    
    
