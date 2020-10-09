import os
from bert_embedding import BertEmbedding

curr_dir = os.getcwd()
filepath = os.path.join(curr_dir, 'csv_files')
files = os.listdir(filepath)
#вот здесь ниже поменять циферку
file =  os.path.join(filepath, files[0])
with open (file, encoding='utf-8') as f:
    sentences = f.read()[1:].splitlines()
print(sentences[0])

bert = BertEmbedding(ctx=ctx)



