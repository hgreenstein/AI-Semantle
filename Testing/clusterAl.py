import gensim
from sklearn.cluster import AgglomerativeClustering
from answers import secretWords as answers
from constants import PATH_TO_DATASET

# Load pre-trained Google News 2021 Word2Vec Model, same used by Semantle 
gnews_model = gensim.models.KeyedVectors.load_word2vec_format(PATH_TO_DATASET, binary=True)

# Get embeddings for answer words
embeddings = []
for answer in answers:
    embeddings.append(gnews_model[answer])

agg_model = AgglomerativeClustering(n_clusters=8, metric='euclidean', linkage='ward')
cluster_labels = agg_model.fit_predict(embeddings)

