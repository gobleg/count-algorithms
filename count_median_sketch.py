import xxhash
import sys

if len(sys.argv) is 4:
    file_name = sys.argv[1]
    bin_number = int(sys.argv[2])
    bin_size = int(sys.argv[3])
else:
    print "python count_min_sketch.py file_name bin_number, bin_size"
    sys.exit()

def median(values):
    if len(values) > 2:
        return median(values[1:-1])
    elif len(values) is 2:
        return (values[0] + values[1]) / 2
    else:
        return values[0]

def hash(bins, data):
    for i in range(0, bin_number):
        key = int(xxhash.xxh32(data, seed=i).hexdigest(), 16) % bin_size
        if key in bins:
            bins[key] += 1
        else:
            bins[key] = 1

def check_value(bins, item):
    values = []
    for i in range(0, bin_number):
        key = int(xxhash.xxh32(item, seed=i).hexdigest(), 16) % bin_size
        if key in bins:
            values.append(bins[key])
    if not values:
        values = [0]
    return median(values)

bins = {}
f = open(file_name, 'r')
for line in f:
    hash(bins, line.rstrip())
print bins
print check_value(bins, "4")
