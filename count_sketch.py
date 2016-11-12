import xxhash
import sys

if len(sys.argv) is 4:
    file_name = sys.argv[1]
    bin_number = int(sys.argv[2])
    bin_size = int(sys.argv[3])
else:
    print "python count_sketch.py file_name bin_number, bin_size"
    sys.exit()

def median(values):
    if len(values) > 2:
        return median(values[1:-1])
    elif len(values) is 2:
        return (values[0] + values[1]) / 2
    else:
        return values[0]

def hash(bins, data, value):
    for i in range(0, bin_number):
        key = int(xxhash.xxh32(data, seed=i).hexdigest(), 16) % bin_size
        sign = int(xxhash.xxh32(data, seed=i+bin_number).hexdigest(), 16) % 2
        if key in bins[i]:
            bins[i][key] += (value * (-1)**sign)
        else:
            bins[i][key] = (value * (-1)**sign)

def check_value(bins, item):
    values = []
    for i in range(0, bin_number):
        key = int(xxhash.xxh32(item, seed=i).hexdigest(), 16) % bin_size
        if key in bins[i]:
            values.append(bins[i][key])
    if not values:
        values = [0]
    return median(values)

bins = [{} for i in range(0, bin_number)]
f = open(file_name, 'r')
for line in f:
    hash(bins, line.rstrip(), 1)
print bins
print check_value(bins, "4")
