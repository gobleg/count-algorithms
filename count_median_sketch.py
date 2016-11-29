import xxhash
from memory_profiler import profile
from count_min_sketch import count_min_sketch, count_min_sketch2

def median(values):
    if len(values) > 2:
        return median(values[1:-1])
    elif len(values) is 2:
        return (values[0] + values[1]) / 2
    else:
        return values[0]

def check_median(bins, item):
    values = []
    for i in range(len(bins)):
        key = int(xxhash.xxh32(item, seed=i).hexdigest(), 16) % len(bins[i])
        values.append(bins[i][key])
    if not values:
        values = [0]
    return median(sorted(values))

def count_median_sketch(data, bin_number, bin_size):
    return count_min_sketch(data, bin_number, bin_size)

def count_median_sketch2(data, bins):
    return count_min_sketch2(data, bins)
