# How much are these like each other?
This tool helps you find if two words are  like each other. This can help us turn words that are hard to understand into words that are easier. 

## How to use
First, you should turn the simple words into numbers. To do this, try:

```
python make_word_embeddings.py --path tools/data/up_goer_words.txt
```

Where `tools/data/up_goer_words.txt` points to the set of simple words. 

Next, you can get the ten words that are most like your word using `similar_words_lookup.py`. To do this, try:

```
python similar_words_lookup.py "your word" --embeddings_path "tools/data/word_embeddings.npy" --words_path "tools/data/up_goer_five_words"
```

Where `--embeddings_path` points to the numbers you just made, and `--words_path` points to the words.

You can also see how much two sets of words are like eachother. To do this, try:

```
python phrase_similairty.py "first set of words" "second set of words"
```

## What you will need to make this work
There is a list of the things your computer will need to make this work in `tools/requirements.txt`.
