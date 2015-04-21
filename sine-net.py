import numpy as np
import matplotlib.pyplot as plt

from pybrain.datasets import SupervisedDataSet
from pybrain.utilities import percentError
from pybrain.structure import FullConnection
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork

import matplotlib.pyplot as plt
import matplotlib.animation as animation

#net = FeedForwardNetwork()
#inLayer = LinearLayer(1)
#hiddenLayer1 = SigmoidLayer(20, name="hidden1")
#outLayer = LinearLayer(1)
#
#net.addInputModule(inLayer)
#net.addModule(hiddenLayer1)
#net.addOutputModule(outLayer)
#
#net.addConnection(FullConnection(inLayer, hiddenLayer1))
#net.addConnection(FullConnection(hiddenLayer1, outLayer))
#net.sortModules()

net = buildNetwork(1, 20, 1, recurrent=True)

xmin = 0
xmax = 4 * np.pi
xs = np.linspace(xmin, xmax, 150)

dataset = SupervisedDataSet(1, 1)
for x in xs:    
    dataset.addSample(x, np.sin(x))

trainset, testset = dataset.splitWithProportion(0.75)
trainer = BackpropTrainer(net, dataset=trainset, learningrate=0.01, momentum=0.5, verbose=False)

fig = plt.figure()
ax1 = plt.axes()


ln1, = ax1.plot([], [], 'r-')
#ln2, = ax1.plot([], [], 'g-')

def animate(i):
    print 'round', i+1
    trainer.trainEpochs(5)    

    train_error = trainer.testOnData(trainset)    
    test_error = trainer.testOnData(testset)
        
    print 'train error', train_error
    print 'test error', test_error
    
    ln1.set_data(i, train_error)
#    ln2.set_data(i, test_error)
    return ln1
    
ani = animation.FuncAnimation(fig, animate, interval=100, frames=200)    
plt.show()