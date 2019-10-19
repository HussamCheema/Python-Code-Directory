from sklearn import datasets
from sklearn import svm
import matplotlib.pyplot as plt

dataset = datasets.load_digits()
clf = svm.SVC(gamma=0.0001, C=100)
X,Y = dataset.data[:-10], dataset.target[:-10]
clf.fit(X,Y)
print('Prediction:',clf.predict(dataset.data)[-3])
plt.imshow(dataset.images[-3], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
