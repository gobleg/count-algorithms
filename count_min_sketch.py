import xxhash
import sys

if len(sys.argv) is 4:
    file_name = sys.argv[1]
    bin_number = int(sys.argv[2])
    bin_size = int(sys.argv[3])
else:
    print "python count_min_sketch.py file_name bin_number, bin_size"
    sys.exit()

def hash(bins, data):
    for i in range(0, bin_number):
        key = int(xxhash.xxh32(data, seed=i).hexdigest(), 16) % bin_size
        if key in bins:
            bins[key] += 1
        else:
            bins[key] = 1

def check_value(bins, item):
    min_value = float("inf")
    for i in range(0, bin_number):
        key = int(xxhash.xxh32(item, seed=i).hexdigest(), 16) % bin_size
        if key in bins:
            min_value = min(min_value, bins[key]) 
            bins[key] += 1
    return min_value

bins = {}
f = open(file_name, 'r')
for line in f:
    hash(bins, line.rstrip())
print bins
print check_value(bins, "4")
