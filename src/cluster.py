import gensim
#import random
from sklearn.cluster import AgglomerativeClustering
#import tkinter as tk
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, ward
from answers import secretWords as answers
from constants import PATH_TO_DATASET

# Load pre-trained Google News 2021 Word2Vec Model, same used by Semantle 
gnews_model = gensim.models.KeyedVectors.load_word2vec_format(PATH_TO_DATASET, binary=True)
embeddings = []
for answer in answers:
    embeddings.append(gnews_model[answer])
aModel = AgglomerativeClustering(n_clusters = 64, linkage= 'ward')
clusters = aModel.fit_predict(embeddings)
print(aModel.cluster_centers_)