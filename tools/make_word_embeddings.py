from sentence_transformers import SentenceTransformer
import argparse
import numpy as np

def main(path):
    model = SentenceTransformer('nomic-ai/nomic-embed-text-v1')
    words = []
    with open(path, 'r') as f:
        for line in f:
            words.append(line.strip())
    word_embeddings = model.encode(words)
    np.save('tools/data/word_embeddings.npy', word_embeddings)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Path to the word list file')
    args = parser.parse_args()
    main(args.path)