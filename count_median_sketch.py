import xxhash
from memory_profiler import profile

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
