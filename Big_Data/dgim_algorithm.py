import enum
import random
import matplotlib.pyplot as plt
from tqdm import tqdm

# Bucket represents the time stamp that the bit entered.
class Bucket:
    def __init__(self, start, end):
        # @self.start is the starting point of the area where the bit came in.
        self.start = start
        # @self.end is the end point of the area where the bit came out.
        self.end = end

    def __repr__(self):
        return f"({self.start},{self.end})"


# DGIM algorithm is a method of counting bits 1 by creating zones by exponentially increasing area size.
class DGIM:
    def __init__(self):
        # @self.bucket_tower is an array that stores the @self.ts of each bit.
        self.bucket_tower = [[]]
        # @self.bucket_integer_tower is an array that stores integers.
        self.bucket_integer_tower = [[]]
        # @self.ts represents a time stamp.
        self.ts = 0  

        self.bucket_integer_sum_tower = [[]]

    # put puts the time stamp in @bucket_tower if @bit is 1.
    def put(self, bit):
        if bit == 1:
            self.bucket_tower[0].insert(0, Bucket(self.ts, self.ts))
            layer = 0
            while len(self.bucket_tower[layer]) > 2:
                if len(self.bucket_tower) <= layer + 1:
                    self.bucket_tower.append([])

                b1 = self.bucket_tower[layer].pop()
                b2 = self.bucket_tower[layer].pop()
                b1.end = b2.end

                self.bucket_tower[layer + 1].insert(0, b1)
                layer += 1

        self.ts += 1
    # count counts the number of bits that came in up to the last @k.
    def count(self, k):
        start_point = self.ts - k
        cnt = 0
        for layer, buckets in enumerate(self.bucket_tower):
            for bucket in buckets:
                if start_point <= bucket.start:
                    cnt += (1 << layer)
                elif start_point <= bucket.end:
                    cnt += (1 << layer) * (bucket.end - start_point + 1) // (bucket.end - bucket.start + 1)
                    return cnt
                else:
                    return cnt
        return cnt
    
    # put_integer puts the time stamp in @bucket_tower and @item in @self.bucket_integer_tower.
    def put_integer(self, item):
    
        layer = 0

        self.bucket_integer_tower[0].insert(0, [item])
        self.bucket_tower[0].insert(0, [Bucket(self.ts, self.ts)])

        while len(self.bucket_integer_tower[layer]) > 2:
            if len(self.bucket_integer_tower) <= layer + 1:
                self.bucket_integer_tower.append([])
                self.bucket_tower.append([])

            if self.bucket_integer_tower[layer][2][0] + self.bucket_integer_tower[layer][1][0] > 2 ** (layer + 1):
                tmp = self.bucket_integer_tower[layer].pop()
                tmp_ts = self.bucket_tower[layer].pop()

                self.bucket_integer_tower[layer + 1].insert(0, tmp)
                self.bucket_tower[layer + 1].insert(0, tmp_ts)
            else:
                tmp = []
                tmp.append(self.bucket_integer_tower[layer][2][0])
                tmp.append(self.bucket_integer_tower[layer][1][0])

                tmp_ts = []
                tmp_ts1 = self.bucket_tower[layer][2][0]
                tmp_ts2 = self.bucket_tower[layer][1][0]

                tmp_ts1.end = tmp_ts2.end
                tmp_ts.append(tmp_ts1)

                self.bucket_integer_tower[layer + 1].insert(0, tmp)
                self.bucket_tower[layer + 1].insert(0, tmp_ts)

                self.bucket_integer_tower[layer].pop()
                self.bucket_integer_tower[layer].pop()

                self.bucket_tower[layer].pop()
                self.bucket_tower[layer].pop()

            layer += 1
        self.ts += 1

    # calc_partial_sum calculates the sum of the integers up to the last @k.
    def calc_partial_sum(self, k):
        partial_sum = 0
        layer = 0
        start_point = self.ts - k
        for area in self.bucket_integer_tower:
            tmp = 0
            for _ , buckets in enumerate(area):
                tmp += sum(buckets)
            self.bucket_integer_sum_tower.append(tmp)
            
        del self.bucket_integer_sum_tower[0]

        for area in self.bucket_tower:
            for _ , buckets in enumerate(area):
                for bucket in buckets:
                    if start_point <= bucket.start:
                        partial_sum += self.bucket_integer_sum_tower[layer]
                    elif start_point <= bucket.end:
                        partial_sum += (self.bucket_integer_sum_tower[layer]) * (bucket.end - start_point + 1) // (bucket.end - bucket.start + 1)
                        return partial_sum
                    else:
                        return partial_sum
                layer += 1
        return partial_sum

# test put_integer()
test_partial_sum = DGIM()
for i in [3, 7, 6, 5, 3, 5, 7, 1, 3, 3]:
    test_partial_sum.put_integer(i)
print("합 = ", test_partial_sum.calc_partial_sum(3))
print("test bucket_integer_tower = ", test_partial_sum.bucket_integer_tower)
print("test bucket_tower = ", test_partial_sum.bucket_tower)
print("test bucket_integer_sum_tower = ", test_partial_sum.bucket_integer_sum_tower)

 
# Testing the Application of Integer Stream to DGIM Algorithm
# -> calculate the sum of the recent k integer values

# method 1 : Consider each bits as a separate stream and apply DGIM algorithm to each stream.
dgim_bit1 = DGIM()
dgim_bit2 = DGIM()
dgim_bit4 = DGIM()
dgim_bit8 = DGIM()
dgim_bit = [dgim_bit1, dgim_bit2, dgim_bit4, dgim_bit8]

# method 2 : If the size of the area is called b, Keep the sum of the values in the area below 2^b.
dgim_partial = DGIM()

real_sum_arr = []
bit_sum_arr = []
partial_sum_arr = []

rand_stream = []
for i in tqdm(range(10000)):
    rand_int = random.randint(0, 15)
    rand_stream.append(rand_int)

    # ex) 0b10 -> 0010
    rand_int_to_bin = bin(rand_int)[2:].rjust(4,'0')
    for idx in range(len(rand_int_to_bin)):
        dgim_bit[idx].put(int(rand_int_to_bin[idx]))
    
    dgim_partial.put_integer(rand_int)

# calculate the sum up to the most recent @k in each method.
for k in tqdm(range(1, 2001)):
    real_sum = 0
    bit_sum = 0
    partial_sum = 0

    for idx in range(10000 - k, 10000):
        real_sum += rand_stream[idx]
    bit_sum = (dgim_bit[0].count(k) + dgim_bit[1].count(k) * 2 + dgim_bit[2].count(k) * 4 + dgim_bit[3].count(k) * 8)
    partial_sum = dgim_partial.calc_partial_sum(k)

    real_sum_arr.append(real_sum)
    bit_sum_arr.append(bit_sum)
    partial_sum_arr.append(partial_sum)

# plot @real_sum_arr, @bit_sum_arr, @partial_sum_arr.
plt.title("Calculation results for each method")
plt.plot(real_sum_arr, color ='red', label = 'real_sum')
plt.plot(bit_sum_arr, label = 'bit_sum')
plt.plot(partial_sum_arr, color = 'green', label = 'partial_sum')
plt.legend(['real_sum', 'bit_sum', 'partial_sum'])
plt.xlabel('k')
plt.ylabel('sum')
plt.show()
