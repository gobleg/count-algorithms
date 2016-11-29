import xxhash
from memory_profiler import profile
from count_median_sketch import median

def hash(bins, data, value):
    for i in range(len(bins)):
        key = int(xxhash.xxh32(data, seed=i).hexdigest(), 16) % len(bins[i])
        sign = int(xxhash.xxh32(data, seed=i+len(bins)).hexdigest(), 16) % 2
        bins[i][key] += (value * (-1)**sign)

def check_sketch(bins, item):
    values = []
    for i in range(len(bins)):
        key = int(xxhash.xxh32(item, seed=i).hexdigest(), 16) % len(bins[i])
        sign = int(xxhash.xxh32(item, seed=i+len(bins)).hexdigest(), 16) % 2
        values.append(bins[i][key] * ((-1) ** sign))
    if not values:
        values = [0]
    return median(sorted(values))

@profile
def count_sketch(data, bin_number, bin_size):
    bins = [[0] * bin_size for i in range(0, bin_number)]
    for d in data:
        hash(bins, d[0], d[1])
    return bins

@profile
def count_sketch2(data, bins):
    bin_number = len(bins)
    for d in data:
        hash(bins, d[0], d[1])
    return bins
