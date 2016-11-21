import xxhash
from memory_profiler import profile

def median(values):
    if len(values) > 2:
        return median(values[1:-1])
    elif len(values) is 2:
        return (values[0] + values[1]) / 2
    else:
        return values[0]

def hash(bins, data, value):
    for i in range(len(bins)):
        key = int(xxhash.xxh32(data, seed=i).hexdigest(), 16) % len(bins[i])
        bins[i][key] += value

def check_median(bins, item):
    values = []
    for i in range(len(bins)):
        key = int(xxhash.xxh32(item, seed=i).hexdigest(), 16) % len(bins[i])
        values.append(bins[i][key])
    if not values:
        values = [0]
    return median(values)

@profile
def count_median_sketch(data, bin_number, bin_size):
    bins = [[0] * bin_size for i in range(0, bin_number)]
    for d in data:
        hash(bins, d, 1)
    return bins

@profile
def count_median_sketch2(data, bins):
    bin_number = len(bins)
    for d in data:
        hash(bins, d, 1)
    return bins

