import random
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

# reservoir sampling is a method of extraction of a part of a data stream.
class Reservoir:

    def __init__(self, k):
        # @self.sampled is an array of data stream.
        self.sampled = []
        # @self.k is the number of data to be extracted.
        self.k = k
        # @self.cnt is the current number of items.
        self.cnt = 0

    # put puts item in @self.sampled.
    def put(self, item):
        if self.cnt < self.k:
            self.sampled.append(item)
        else:
            r = random.randint(0, self.cnt)
            if r < self.k:
                self.sampled[r] = item
        self.cnt += 1


# @sample_count is an array containing the number of times each number is extracted.
sample_count = np.zeros(1000, dtype = int)

# test reservoir sampling 10000 times.
for i in tqdm(range(10000)):
     # initialize Reservoir with @k = 100.
    reservoir = Reservoir(100)
    # put 0 ~ 999 interger stream in reservoir object.
    for j in range(1000):
        reservoir.put(j)
    # add 1 count of the integers extracted by sampling.
    for idx in reservoir.sampled:
        sample_count[idx] += 1

# plot @sample_count.
plt.title("reservoir_sampling without replacement")
plt.plot(sample_count)
plt.show()