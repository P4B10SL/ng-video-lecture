import nltk
import torch # we use PyTorch: https://pytorch.org

words = nltk.tokenize.word_tokenize(text, language='spanish', preserve_line=False)
vocab_size = len(words)

# create a mapping from words to integers
stoi = { word:i for i, word in enumerate(words) }
itos = { i:word for i, word in enumerate(words) }

encode = lambda s: [stoi[word] for word in s.split()] # encoder: take a string, output a list of integers
decode = lambda l: ' '.join([itos[i] for i in l]) # decoder: take a list of integers, output a string

# let's now encode the entire text dataset and store it into a torch.Tensor
data = torch.tensor(encode(text), dtype=torch.long)
print(data.shape, data.dtype)
print(data[:1000]) # the 1000 characters we looked at earier will to the GPT look like this
