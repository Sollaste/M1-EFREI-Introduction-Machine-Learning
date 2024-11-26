import numpy as np
import matplotlib as plt

def randomArrayGenerator(low, high, nbrValues):

    randomArray = np.random.uniform(low, high, size=nbrValues)
    return randomArray

def dataSetGenerator():

    classeA = randomArrayGenerator(0, 10, (2, 200))

    classeBx = randomArrayGenerator(-10, 0, 200)
    classeBy = randomArrayGenerator(0, 10, 200)
    classeB = np.vstack((classeBx, classeBy))
    
    return classeA, classeB
        
dataset = dataSetGenerator()
print(dataset)