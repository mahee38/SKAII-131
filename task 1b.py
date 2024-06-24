import nltk
from nltk.util import ngrams
from collections import defaultdict

text = "The quick brown fox jumps over the lazy dog. The lazy dog barks loudly."

tokens = nltk.word_tokenize(text.lower())

n = 2
ngram_freq = defaultdict(lambda: defaultdict(int))

for ngram in ngrams(tokens, n):
    prefix = tuple(ngram[:-1])
    suffix = ngram[-1]
    ngram_freq[prefix][suffix] += 1

def predict_next_word(model, prefix):
    choices = model[prefix]
    if not choices:
        return None
    return max(choices, key=choices.get)

prefix = ('the', 'lazy')
predicted_word = predict_next_word(ngram_freq, prefix)

print(f"The predicted next word after '{' '.join(prefix)}' is: {predicted_word}")
