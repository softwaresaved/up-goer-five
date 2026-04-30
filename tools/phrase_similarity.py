from sentence_transformers import SentenceTransformer
import argparse
import numpy as np

def main(phrase_1, phrase_2):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embedding_1 = model.encode([phrase_1])[0]
    embedding_2 = model.encode([phrase_2])[0]
    similarity = np.dot(embedding_1, embedding_2) / (np.linalg.norm(embedding_1) * np.linalg.norm(embedding_2))
    print(f"Similarity between '{phrase_1}' and '{phrase_2}': {similarity:.4f}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('phrase_1', help='The first phrase')
    parser.add_argument('phrase_2', help='The second phrase')
    args = parser.parse_args()
    main(args.phrase_1, args.phrase_2)