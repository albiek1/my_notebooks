from matplotlib import pyplot
from keras.datasets import cifar10
(trainX, trainY), (testX, testY) = cifar10.load_data()
print('Train: X=%s, Y=%s' % (trainX.shape, trainY.shape))
print('Test: X=%s, Y=%s' % (trainX.shape, trainY.shape))

for i in range(9):
    pyplot.subplot(330+1+i)
    pyplot.imshow(trainX[i])
    
pyplot.show()