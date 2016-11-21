import sys
from memory_profiler import profile
import pandas as pd

from count_median_sketch import count_median_sketch
from count_min_sketch import count_min_sketch
from count_sketch import count_sketch

def linear_count(data, bin_number, bin_size):
    counts = {}
    for d in data:
        if d in counts:
            counts[d] += 1
        else:
            counts[d] = 1
    return dict(sorted(counts, key=counts.get, reverse=True)[:bin_size])

@profile
def run(algorithm, file_name, bin_number, bin_size):
    df = pd.read_csv(file_name, index_col='Id')
    data = []
    for row in df.iterrows():
        data.extend(row[1]['Name'] * row[1]['Count'])
    return eval(algorithm)(data, bin_number, bin_size)

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