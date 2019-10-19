import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn import datasets

my_data = datasets.load_digits()
x = my_data.data[:-10]

agClustering = AgglomerativeClustering(n_clusters=3)
agClustering.fit(x)

print(agClustering.labels_)