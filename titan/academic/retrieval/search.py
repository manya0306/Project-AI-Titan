from sentence_transformers import util
from titan.academic.embeddings.embedder import model


def semantic_search(query, chunks, embeddings, top_k=3):

    query_embedding = model.encode(query)

    scores = util.cos_sim(query_embedding, embeddings)[0]

    top_results = scores.argsort(descending=True)[:5]

    results = []

    for idx in top_results:

        results.append({
            "score": float(scores[idx]),
            "text": chunks[idx]
        })

    return results