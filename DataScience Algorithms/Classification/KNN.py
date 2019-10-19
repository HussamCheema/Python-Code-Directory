from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
import matplotlib.pyplot as plt

dataset = datasets.load_digits()
clf = KNeighborsClassifier(n_neighbors=3)

X,Y = dataset.data[:-10], dataset.target[:-10]
clf.fit(X,Y)
print('Prediction:',clf.predict(dataset.data)[-9])
plt.imshow(dataset.images[-9], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()