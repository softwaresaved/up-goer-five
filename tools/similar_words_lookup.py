from sentence_transformers import SentenceTransformer
import argparse
import numpy as np

def main(query_word, embeddings_path='tools/data/word_embeddings.npy', words_path='tools/data/word_list.txt'):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    word_embeddings = np.load(embeddings_path)
    with open(words_path, 'r') as f:
        words = [line.strip() for line in f]    
    query_embedding = model.encode([query_word])[0]
    similarities = np.dot(word_embeddings, query_embedding) / (np.linalg.norm(word_embeddings, axis=1) * np.linalg.norm(query_embedding))
    top_indices = np.argsort(similarities)[::-1][:10]
    print(f"Top 10 similar words to '{query_word}':")
    for idx in top_indices:
        print(f"{words[idx]} (similarity: {similarities[idx]:.4f})")
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('query_word', help='The word to search for')
    parser.add_argument('--embeddings_path', default='tools/data/word_embeddings.npy', help='Path to the word embeddings file')
    parser.add_argument('--words_path', default='tools/data/up_goer_words.txt', help='Path to the word list file')
    args = parser.parse_args()
    main(args.query_word, args.embeddings_path, args.words_path)