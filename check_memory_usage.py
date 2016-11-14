import sys
from memory_profiler import profile

from count_median_sketch import count_median_sketch
from count_min_sketch import count_min_sketch
from count_sketch import count_sketch

def linear_count(file, bin_number, bin_size):
    # bin_number and bin_size not used, there might be a better way to do this
    counts = {}
    f = open(file, 'r')
    for line in f:
        key = line.rstrip()
        if key in counts:
            counts[key] += 1
        else:
            counts[key] = 1
    return counts

@profile
def run(algorithm, file_name, bin_number, bin_size):
    return eval(algorithm)(file_name, bin_number, bin_size)

if __name__ == '__main__':
    if len(sys.argv) is 5:
        algorithm = sys.argv[1]
        file_name = sys.argv[2]
        bin_number = int(sys.argv[3])
        bin_size = int(sys.argv[4])
        bins = run(algorithm, file_name, bin_number, bin_size)
    else:
        print "python check_memory_usage.py algorithm file_name bin_number bin_size"
        sys.exit()