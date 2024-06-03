# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 22:49:20 2024

@author: pushy
"""

#%%
# libraries
import os
import time
import pandas as pd
import numpy as np
from pinecone import Pinecone, PodSpec;
from sentence_transformers import SentenceTransformer
import joblib
from django.conf import settings;


#%%

# initilise everything

with open('data.txt', 'r') as file:
    quotes = file.readlines()
    
model = model = joblib.load('model.pkl')

#%%

# create pinecone vector database
api_key = os.environ.get('PINECONE_API')
pc = Pinecone(api_key = api_key)
spec = PodSpec(environment = 'gcp-starter')

index_name = 'happy-bday-2024'

if index_name in pc.list_indexes().names():
    pc.delete_index(index_name)
     
dimension = 384
pc.create_index(
    name = index_name,
    dimension = dimension,
    metric = 'cosine',
    spec = spec)

# wait for it to be ready
while not pc.describe_index(index_name).status['ready']:
    time.sleep(1)
    

index= pc.Index(index_name)

#%%
    
embeddings = model.encode(quotes)
# ids = [str(i) for i in range(embeddings.shape[0])]
ids = [quote for quote in quotes]
vectors = [np.array(row) for row in embeddings]

# data uploaded 
# metadata = [{'quote': quote.strip()} for quote in quotes]
print(index.upsert(vectors = zip(ids, vectors)))