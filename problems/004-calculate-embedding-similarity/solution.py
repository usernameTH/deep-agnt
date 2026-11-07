import numpy as np


def cosine_similarity(query, documents):
    query = np.asarray(query, dtype=float)
    documents = np.asarray(documents, dtype=float)

    query_norm = np.linalg.norm(query)
    doc_norms = np.linalg.norm(documents, axis=1)

    denominator = doc_norms * query_norm
    dots = documents @ query

    # A zero vector has no direction. `where` keeps the division from ever
    # running on those entries, so no warning is emitted at all.
    
    return np.divide(
        dots, denominator,
        out=np.zeros_like(dots, dtype=float),
        where=denominator != 0,
    )
    
