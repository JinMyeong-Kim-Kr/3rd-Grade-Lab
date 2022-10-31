import math, mmh3, random
from tqdm import tqdm

class BloomFilter:
    # @capacity = s 의 크기 (ppt에서 m)
    def __init__(self, capacity, fp_prob):
        self.capacity = capacity
        self.fp_prob = fp_prob
        self.bitarray = 0
        self.n_bits = math.ceil(-math.log(fp_prob, math.e) * capacity / (math.log(2, math.e)**2))
        self.n_hashs = int(self.n_bits / capacity * math.log(2, math.e))
        self.seeds = [random.randint(0,999999) for _ in range(self.n_hashs)]

    def put(self, item):
        for i in range(self.n_hashs):
            pos = mmh3.hash(item, self.seeds[i]) % self.n_bits
            self.bitarray |= (1 << pos)

    def test(self, item):
        for i in range(self.n_hashs):
            pos = mmh3.hash(item, self.seeds[i]) % self.n_bits

            if self.bitarray & (1 << pos) == 0:
                return False
            return True

def put_and_test_BloomFilter(put_list, test_list):
    
    bloom_10000 = BloomFilter(10000, 0)
    bloom_50000 = BloomFilter(50000, 0)
    bloom_100000 = BloomFilter(100000, 0)
    bloom_150000 = BloomFilter(150000, 0)
    bloom_200000 = BloomFilter(200000, 0)

    num_of_fp_10000 = 0
    num_of_fp_50000 = 0
    num_of_fp_100000 = 0
    num_of_fp_150000 = 0
    num_of_fp_200000 = 0

    for i in put_list:
        bloom_10000.put(i)
        bloom_50000.put(i)
        bloom_100000.put(i)
        bloom_150000.put(i)
        bloom_200000.put(i)
        
    for i in test_list:
        if bloom_10000.test(i):
            num_of_fp_10000 += 1
        if bloom_50000.test(i):
            num_of_fp_50000 += 1
        if bloom_100000.test(i):
            num_of_fp_100000 += 1
        if bloom_150000.test(i):
            num_of_fp_150000 += 1
        if bloom_200000.test(i):
            num_of_fp_200000 += 1

    print("Number of test item = ", len(test_list))

    print("Number of false positive_10000 = ", num_of_fp_10000)
    print("Number of false positive_50000 = ", num_of_fp_50000)
    print("Number of false positive_100000 = ", num_of_fp_100000)
    print("Number of false positive_150000 = ", num_of_fp_150000)
    print("Number of false positive_200000 = ", num_of_fp_200000)

    print("false positive ratio_10000 = ", num_of_fp_10000 / len(test_list))
    print("false positive ratio_50000 = ", num_of_fp_50000 / len(test_list))
    print("false positive ratio_100000 = ", num_of_fp_100000 / len(test_list))
    print("false positive ratio_150000 = ", num_of_fp_150000 / len(test_list))
    print("false positive ratio_200000 = ", num_of_fp_200000 / len(test_list))

    print("Number of bloom_10000 bits = ", bloom_10000.n_bits)
    print("Number of bloom_50000 bits = ", bloom_50000.n_bits)
    print("Number of bloom_100000 bits = ", bloom_100000.n_bits)
    print("Number of bloom_150000 bits = ", bloom_150000.n_bits)
    print("Number of bloom_200000 bits = ", bloom_200000.n_bits)

    print("Number of bloom_10000 hashs = ", bloom_10000.n_hashs)
    print("Number of bloom_50000 hashs = ", bloom_50000.n_hashs)
    print("Number of bloom_100000 hashs = ", bloom_100000.n_hashs)
    print("Number of bloom_150000 hashs = ", bloom_150000.n_hashs)
    print("Number of bloom_200000 hashs = ", bloom_200000.n_hashs)

dict_file = open('dict.txt', 'r')
dict_stream = dict_file.read().split('\n')

put_list = []
test_list = []
rand_int_list = []
# Test number of items to put 10000, test 50000.
for i in tqdm(range(60000)):
    rand_int = random.randint(0,len(dict_stream) - 1)
    while rand_int in rand_int_list:
        rand_int = random.randint(0,len(dict_stream) - 1)
    rand_int_list.append(rand_int)
    if i < 10000:
        put_list.append(dict_stream[rand_int])
    else:
        test_list.append(dict_stream[rand_int])

print("Case: put 10000, test 50000")        
put_and_test_BloomFilter(put_list, test_list)

put_list = []
test_list = []
rand_int_list = []
# Test number of items to put 25000, test 25000.
for i in tqdm(range(50000)):
    rand_int = random.randint(0,len(dict_stream) - 1)
    while rand_int in rand_int_list:
        rand_int = random.randint(0,len(dict_stream) - 1)
    rand_int_list.append(rand_int)
    if i < 25000:
        put_list.append(dict_stream[rand_int])
    else:
        test_list.append(dict_stream[rand_int])

print("Case: put 25000, test 25000")        
put_and_test_BloomFilter(put_list, test_list)

put_list = []
test_list = []
rand_int_list = []
# Test number of items to put 50000, test 10000.
for i in tqdm(range(60000)):
    rand_int = random.randint(0,len(dict_stream) - 1)
    while rand_int in rand_int_list:
        rand_int = random.randint(0,len(dict_stream) - 1)
    rand_int_list.append(rand_int)
    if i < 50000:
        put_list.append(dict_stream[rand_int])
    else:
        test_list.append(dict_stream[rand_int])

print("Case: put 50000, test 10000")        
put_and_test_BloomFilter(put_list, test_list)

