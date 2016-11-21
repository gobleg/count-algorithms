import xxhash
from memory_profiler import profile

def hash(bins, data, value, bin_size):
    for i in range(len(bins)):
        key = int(xxhash.xxh32(data, seed=i).hexdigest(), 16) % bin_size
        if key in bins[i]:
            bins[i][key] += value
        else:
            bins[i][key] = value

def check_value(bins, item, bin_size):
    min_value = float("inf")
    for i in range(len(bins)):
        key = int(xxhash.xxh32(item, seed=i).hexdigest(), 16) % bin_size
        if key in bins[i]:
            min_value = min(min_value, bins[i][key]) 
    return min_value

@profile
def count_min_sketch(data, bin_number, bin_size):
    bins = [{} for i in range(0, bin_number)]
    for d in data:
        hash(bins, d, 1, bin_size)
    print check_value(bins, "4", bin_size)
    return bins

@profile
def count_min_sketch2(data, bin_size, bins):
    bin_number = len(bins)
    for d in data:
        hash(bins, d, 1, bin_size)
    print check_value(bins, "4", bin_size)
    return bins
