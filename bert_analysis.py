import os
#from bert_embedding import BertEmbedding

curr_dir = os.getcwd()
filepath = os.path.join(curr_dir, 'data/untagged')
files = os.listdir(filepath)
#вот здесь ниже поменять циферку
file =  os.path.join(filepath, files[1])
with open (file, encoding='utf-8') as f:
    sentences = f.read().splitlines()
print(sentences[0])
#bert_embedding = BertEmbedding()
#result = bert_embedding(sentences)

#print(result[0][1])





