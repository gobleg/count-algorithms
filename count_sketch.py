import xxhash

def median(values):
    if len(values) > 2:
        return median(values[1:-1])
    elif len(values) is 2:
        return (values[0] + values[1]) / 2
    else:
        return values[0]

def hash(bins, data, value, bin_size):
    for i in range(len(bins)):
        key = int(xxhash.xxh32(data, seed=i).hexdigest(), 16) % bin_size
        sign = int(xxhash.xxh32(data, seed=i+len(bins)).hexdigest(), 16) % 2
        if key in bins[i]:
            bins[i][key] += (value * (-1)**sign)
        else:
            bins[i][key] = (value * (-1)**sign)

def check_value(bins, item, bin_size):
    values = []
    for i in range(len(bins)):
        key = int(xxhash.xxh32(item, seed=i).hexdigest(), 16) % bin_size
        if key in bins[i]:
            values.append(bins[i][key])
    if not values:
        values = [0]
    return median(values)

def count_sketch(file_name, bin_number, bin_size):
    bins = [{} for i in range(0, bin_number)]
    f = open(file_name, 'r')
    for line in f:
        hash(bins, line.rstrip(), 1, bin_size)
    print bins
    print check_value(bins, "4", bin_size)
    return bins

def count_sketch(file_name, bin_size, bins):
    bin_number = len(bins)
    f = open(file_name, 'r')
    for line in f:
        hash(bins, line.rstrip(), 1, bin_size)
    print bins
    print check_value(bins, "4", bin_size)
    return bins
