import xxhash
from memory_profiler import profile

def hash(bins, data, value):
    for i in range(len(bins)):
        k = xxhash.xxh32(data, seed=i)
        key = int(k.hexdigest(), 16) % len(bins[i])
        bins[i][key] += value

def check_min(bins, item):
    min_value = float("inf")
    for i in range(len(bins)):
        key = int(xxhash.xxh32(item, seed=i).hexdigest(), 16) % len(bins[i])
        min_value = min(min_value, bins[i][key]) 
    return min_value

@profile
def count_min_sketch(data, bin_number, bin_size):
    bins = [[0] * bin_size for i in range(0, bin_number)]
    for d in data:
        hash(bins, d[0], d[1])
    return bins

@profile
def count_min_sketch2(data, bins):
    bin_number = len(bins)
    for d in data:
        hash(bins, d[0], d[1])
    return bins
