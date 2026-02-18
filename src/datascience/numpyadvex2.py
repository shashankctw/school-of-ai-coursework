# Generate and filter random datasets using NumPy.

import numpy as np

dataset = np.random.randint(1, 51, size=(5, 5)) # Generation of random dataset
print("Original Dataset: \n", dataset)

dataset[dataset < 25] = 0 #Filtering the dataset
print("Filtered Dataset: \n", dataset)

# Statistical operations on the dataset
print("sum of the dataset: ", np.sum(dataset))
print("mean of the dataset: ", np.mean(dataset))
print("standard deviation of the dataset: ", np.std(dataset)) 
 