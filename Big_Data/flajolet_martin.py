
from cProfile import label
import mmh3
import math
import random
import matplotlib.pyplot as plt
from tqdm import tqdm

# Flajolet-Martin Approach Version 1 predicts the number of distinct elements in the top 1 bit
class FM1:
    def __init__(self, domain_size):
        self.bitarray = 0
        self.domain_size = domain_size
        self.n_bits = math.ceil(math.log2(domain_size))
        self.seed = random.randint(0, 9999999)
        self.mask = (1 << self.n_bits) - 1

    def put(self, item):
        h = mmh3.hash(item, self.seed) & self.mask
        r = 0

        if h == 0: return

        while h & (1 << r) == 0: r += 1

        self.bitarray |= (1 << r)


    def size(self):
        # ex) 0b1000 => len is 6 but value is 2 ** 3
        R = len(str(bin(self.bitarray))) - 3
        return 2 ** R
        
# Flajolet-Martin Approach Version 2 predicts the number of distinct elements in the least significant unset bit.
class FM2:
    def __init__(self, domain_size):
        self.bitarray = 0
        self.domain_size = domain_size
        self.n_bits = math.ceil(math.log2(domain_size))
        self.seed = random.randint(0, 9999999)
        self.mask = (1 << self.n_bits) - 1

    def put(self, item):
        h = mmh3.hash(item, self.seed) & self.mask
        r = 0

        if h == 0: return

        while h & (1 << r) == 0: r += 1

        self.bitarray |= (1 << r)


    def size(self):
        R = 0
        while self.bitarray & (1 << R) != 0: R += 1

        return 2 ** R / 0.77351

# Compare version 1 version 2

# @fm1 uses version 1.
fm1 = FM1(1000000)
# @fm2 uses version 2.
fm2 = FM2(1000000)

tset = set()
x = []
fm1_y = []
fm2_y = []

for i in tqdm(range(100000)):
    item = str(random.randint(0, 10000))
    fm1.put(item)
    fm2.put(item)
    tset.add(item)
    x.append(len(tset))
    fm1_y.append(fm1.size())
    fm2_y.append(fm2.size())

plt.scatter(x, fm1_y, c = 'g', s = 1.0 , label = 'version 1')
plt.scatter(x, fm2_y, label = 'version 2')
plt.plot(x,x, color = 'r', label = 'real result')
plt.legend()
plt.show()


# Take the following steps for accurate prediction
# 1.Average the median value
# 2.Divide forecasts into groups
# 3.Find the center value for each group
# 4.Average center values

fm2_1 = FM2(1000000); fm2_2 = FM2(1000000); fm2_3 = FM2(1000000)
fm2_4 = FM2(1000000); fm2_5 = FM2(1000000); fm2_6 = FM2(1000000)
fm2_7 = FM2(1000000); fm2_8 = FM2(1000000); fm2_9 = FM2(1000000)
fm2_10 = FM2(1000000); fm2_11 = FM2(1000000); fm2_12 = FM2(1000000)
fm2_13 = FM2(1000000); fm2_14 = FM2(1000000); fm2_15 = FM2(1000000)


fm2_group1_y = []
fm2_group2_y = []
fm2_group3_y = []

# number of hashs = 3, group = 3
fm_group1 = [[fm2_1], [fm2_2], [fm2_3]]

# number of hashs = 9, group = 3
fm_group2 = [[fm2_1, fm2_2, fm2_3], [fm2_4, fm2_5, fm2_6], [fm2_7, fm2_8, fm2_9]]

# number of hashs = 15, group = 3 
fm_group3 = [[fm2_1, fm2_2, fm2_3, fm2_4, fm2_5], [fm2_6, fm2_7, fm2_8, fm2_9, fm2_10], [fm2_11, fm2_12, fm2_13, fm2_14, fm2_15]]


tset = set()
x = []

for i in tqdm(range(100000)):
    item = str(random.randint(0, 10000))
    avg_1 = 0
    avg_2 = 0
    avg_3 = 0

    fm2_1.put(item); fm2_2.put(item); fm2_3.put(item)
    fm2_4.put(item); fm2_5.put(item); fm2_6.put(item)
    fm2_7.put(item); fm2_8.put(item); fm2_9.put(item)
    fm2_10.put(item); fm2_11.put(item); fm2_12.put(item)
    fm2_13.put(item); fm2_14.put(item); fm2_15.put(item)

    # Add center value of group to variable.
    for group in fm_group1:
        mid_1 = []
        for fm in group:
            mid_1.append(fm.size())

        mid_1.sort()
        avg_1 += mid_1[int(len(mid_1)/2)]/len(mid_1)
    for group in fm_group2:
        mid_2 = []
        for fm in group:
            mid_2.append(fm.size())

        mid_2.sort()
        avg_2 += mid_2[int(len(mid_2)/2)]/len(mid_2)
    for group in fm_group3:
        mid_3 = []
        for fm in group:
            mid_3.append(fm.size())
        mid_3.sort()
        avg_3 += mid_3[int(len(mid_3)/2)]/len(mid_3)

    tset.add(item)
    x.append(len(tset))
    # Append to @fm2_group_y the mean values of the median values.
    fm2_group1_y.append(avg_1)
    fm2_group2_y.append(avg_2)
    fm2_group3_y.append(avg_3)

plt.scatter(x, fm2_group1_y, c = 'g', label = 'group 1')
plt.scatter(x, fm2_group2_y, c = 'r', label = 'group 2')
plt.scatter(x, fm2_group3_y, c = 'b', label = 'group 3')
plt.plot(x,x, color = 'r')
plt.legend()
plt.show()

fm2_1 = FM2(1000000); fm2_2 = FM2(1000000); fm2_3 = FM2(1000000)
fm2_4 = FM2(1000000); fm2_5 = FM2(1000000); fm2_6 = FM2(1000000)
fm2_7 = FM2(1000000); fm2_8 = FM2(1000000); fm2_9 = FM2(1000000)
fm2_10 = FM2(1000000); fm2_11 = FM2(1000000); fm2_12 = FM2(1000000)
fm2_13 = FM2(1000000); fm2_14 = FM2(1000000); fm2_15 = FM2(1000000)

# number of hashs = 15, group = 1
fm_group4 = [[fm2_1, fm2_2, fm2_3, fm2_4, fm2_5, fm2_6, fm2_7, fm2_8, fm2_9, fm2_10, fm2_11, fm2_12, fm2_13, fm2_14, fm2_15]]

# number of hashs = 15, group = 3
fm_group5 = [[fm2_1, fm2_2, fm2_3, fm2_4, fm2_5], [fm2_6, fm2_7, fm2_8, fm2_9, fm2_10], [fm2_11, fm2_12, fm2_13, fm2_14, fm2_15]]

# number of hashs = 15, group = 5
fm_group6 = [[fm2_1, fm2_2, fm2_3], [fm2_4, fm2_5, fm2_6], [fm2_7, fm2_8, fm2_9], [fm2_10, fm2_11, fm2_12], [fm2_13, fm2_15, fm2_15]]


tset = set()
x = []
fm2_group4_y = []
fm2_group5_y = []
fm2_group6_y = []

for i in tqdm(range(100000)):
    item = str(random.randint(0, 10000))
    avg_4 = 0
    avg_5 = 0
    avg_6 = 0

    fm2_1.put(item)
    fm2_2.put(item)
    fm2_3.put(item)
    fm2_4.put(item)
    fm2_5.put(item)
    fm2_6.put(item)
    fm2_7.put(item)
    fm2_8.put(item)
    fm2_9.put(item)
    fm2_10.put(item)
    fm2_11.put(item)
    fm2_12.put(item)
    fm2_13.put(item)
    fm2_14.put(item)
    fm2_15.put(item)

    # Add center value of group to variable.
    for group in fm_group4:
        mid_4 = []
        for fm in group:
            mid_4.append(fm.size())

        mid_4.sort()
        avg_4 += mid_4[int(len(mid_4)/2)]/len(mid_4)
    for group in fm_group5:
        mid_5 = []
        for fm in group:
            mid_5.append(fm.size())

        mid_5.sort()
        avg_5 += mid_5[int(len(mid_5)/2)]/len(mid_5)
    for group in fm_group6:
        mid_6 = []
        for fm in group:
            mid_6.append(fm.size())

        mid_6.sort()
        avg_6 += mid_6[int(len(mid_6)/2)]/len(mid_6)

    tset.add(item)
    x.append(len(tset))
    # Append to @fm2_group_y the mean values of the median values.
    fm2_group4_y.append(avg_4)
    fm2_group5_y.append(avg_5)
    fm2_group6_y.append(avg_6)

plt.scatter(x, fm2_group4_y, c = 'g', label = 'group 4')
plt.scatter(x, fm2_group5_y, c = 'r', label = 'group 5')
plt.scatter(x, fm2_group6_y, c = 'b', label = 'group 6')
plt.plot(x,x, color = 'r')
plt.legend()
plt.show()

# number of hashs = 30, group = 6
fm2_1 = FM2(1000000); fm2_2 = FM2(1000000); fm2_3 = FM2(1000000)
fm2_4 = FM2(1000000); fm2_5 = FM2(1000000); fm2_6 = FM2(1000000)
fm2_7 = FM2(1000000); fm2_8 = FM2(1000000); fm2_9 = FM2(1000000)
fm2_10 = FM2(1000000); fm2_11 = FM2(1000000); fm2_12 = FM2(1000000)
fm2_13 = FM2(1000000); fm2_14 = FM2(1000000); fm2_15 = FM2(1000000)
fm2_16 = FM2(1000000); fm2_17 = FM2(1000000); fm2_18 = FM2(1000000)
fm2_19 = FM2(1000000); fm2_20 = FM2(1000000); fm2_21 = FM2(1000000)
fm2_22 = FM2(1000000); fm2_23 = FM2(1000000); fm2_24 = FM2(1000000)
fm2_25 = FM2(1000000); fm2_26 = FM2(1000000); fm2_27 = FM2(1000000)
fm2_28 = FM2(1000000); fm2_29 = FM2(1000000); fm2_30 = FM2(1000000)

fm_group_tmp = [[fm2_1, fm2_2, fm2_3, fm2_4, fm2_5],
 [fm2_6, fm2_7, fm2_8, fm2_9, fm2_10] , [fm2_11, fm2_12, fm2_13, fm2_14, fm2_15], [fm2_16, fm2_17, fm2_18, fm2_19, fm2_20], [fm2_21, fm2_22, fm2_23, fm2_24, fm2_25], [fm2_26,fm2_27, fm2_28, fm2_29, fm2_30]]

tset = set()
x = []
fm2_group_tmp_y = []

for i in tqdm(range(100000)):
    item = str(random.randint(0, 10000))
    avg_tmp = 0

    fm2_1.put(item);fm2_2.put(item);fm2_3.put(item)
    fm2_4.put(item);fm2_5.put(item);fm2_6.put(item)
    fm2_7.put(item);fm2_8.put(item);fm2_9.put(item)
    fm2_10.put(item);fm2_11.put(item);fm2_12.put(item)
    fm2_13.put(item);fm2_14.put(item);fm2_15.put(item)
    fm2_16.put(item);fm2_17.put(item);fm2_18.put(item)
    fm2_19.put(item);fm2_20.put(item);fm2_21.put(item)
    fm2_22.put(item);fm2_23.put(item);fm2_24.put(item)
    fm2_25.put(item);fm2_26.put(item);fm2_27.put(item)
    fm2_28.put(item);fm2_29.put(item);fm2_30.put(item)

    # Add center value of group to variable.
    for group in fm_group_tmp:
        mid_tmp = []
        for fm in group:
            mid_tmp.append(fm.size())

        mid_tmp.sort()
        avg_tmp += mid_tmp[int(len(mid_tmp)/2)]/len(mid_tmp)
    tset.add(item)
    x.append(len(tset))
    fm2_group_tmp_y.append(avg_tmp)

plt.scatter(x, fm2_group_tmp_y, c = 'g', label = 'group_tmp')
plt.plot(x,x, color = 'r')
plt.legend()
plt.show()