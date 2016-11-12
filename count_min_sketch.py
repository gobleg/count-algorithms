import xxhash
import sys

if len(sys.argv) is 4:
    file_name = sys.argv[1]
    bin_number = int(sys.argv[2])
    bin_size = int(sys.argv[3])
else:
    print "python count_min_sketch.py file_name bin_number, bin_size"
    sys.exit()

def hash(bins, data, value):
    for i in range(0, bin_number):
        key = int(xxhash.xxh32(data, seed=i).hexdigest(), 16) % bin_size
        if key in bins[i]:
            bins[i][key] += value
        else:
            bins[i][key] = value

def check_value(bins, item):
    min_value = float("inf")
    for i in range(0, bin_number):
        key = int(xxhash.xxh32(item, seed=i).hexdigest(), 16) % bin_size
        if key in bins[i]:
            min_value = min(min_value, bins[i][key]) 
    return min_value

bins = [{} for i in range(0, bin_number)]
f = open(file_name, 'r')
for line in f:
    hash(bins, line.rstrip(), 1)
print bins
print check_value(bins, "4")
