import xxhash
from memory_profiler import profile

def hash(bins, data, value, bin_size):
    for i in range(len(bins)):
        key = int(xxhash.xxh32(data, seed=i).hexdigest(), 16) % bin_size
        sign = int(xxhash.xxh32(data, seed=i+len(bins)).hexdigest(), 16) % 2
        if key in bins[i]:
            bins[i][key] += (value * (-1)**sign)
        else:
            bins[i][key] = (value * (-1)**sign)

@profile
def count_sketch(data, bin_number, bin_size):
    bins = [{} for i in range(0, bin_number)]
    for d in data:
        hash(bins, d, 1, bin_size)
    return bins

@profile
def count_sketch2(data, bin_size, bins):
    bin_number = len(bins)
    for d in data:
        hash(bins, d, 1, bin_size)
    return bins
