from sklearn import neural_network
from sklearn import datasets
import matplotlib.pyplot as plt

dataset = datasets.load_digits()
clf = neural_network.MLPClassifier( learning_rate="constant",
                                    learning_rate_init=0.001,
                                    activation="logistic",
                                    hidden_layer_sizes=(200,))
X,Y = dataset.data[:-10], dataset.target[:-10]
clf.fit(X,Y)
print('Prediction:', clf.predict(dataset.data)[-8])
plt.imshow(dataset.images[-8], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()