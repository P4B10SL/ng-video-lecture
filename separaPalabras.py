import re

with open('Reglamentacion_sin_tildes.txt', 'r', encoding='utf-8') as f:
    text = f.read()

words_and_symbols = re.findall(r'\w+[:]?|\S', text)

# Remove duplicates by converting the list to a set, then sort by converting back to a list
unique_sorted_words_and_symbols = sorted(set(words_and_symbols))

print(unique_sorted_words_and_symbols)

#nltk word=tokenizer