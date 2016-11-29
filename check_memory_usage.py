import sys
import operator
from memory_profiler import profile
import pandas as pd
import numpy as np
import pickle

from count_median_sketch import check_median
from count_min_sketch import count_min_sketch, check_min
from count_sketch import count_sketch, check_sketch

@profile
def linear_count(data, bin_number, bin_size):
    counts = {}
    for d in data:
        if d[0] in counts:
            counts[d[0]] += d[1]
        else:
            counts[d[0]] = d[1]
    return counts

def error(observed, query_func, truth, n=1):
    vec = []
    for k in truth.keys():
        vec.append(truth[k] - query_func(observed, k))
    return np.linalg.norm(vec, n)

def run(algorithm, file_name, bin_number, bin_size):
    # Use for names
    df = pd.read_csv(file_name, index_col='Id')
    data = []
    for row in df.iterrows():
        data.append((row[1]['Name'], row[1]['Count']))

    # Use for shakespeare
    # f = open(file_name)
    # s = f.read()
    # import string
    # s = s.lower()
    # s = s.translate(None, string.punctuation)
    # data = s.split()
    # data = [(d, 1) for d in data]
    
    return eval(algorithm)(data, bin_number, bin_size)

if __name__ == '__main__':
    if len(sys.argv) is 5:
        algorithm = sys.argv[1]
        file_name = sys.argv[2]
        bin_number = int(sys.argv[3])
        bin_size = int(sys.argv[4])
        bins = run(algorithm, file_name, bin_number, bin_size)
        print 'Finished run'
        truth = pickle.load(open('names_linear.out', 'r'))
        print 'Error: ' + str(error(bins, check_median, truth, n=np.inf))
    else:
        print "python check_memory_usage.py algorithm file_name bin_number bin_size"
        sys.exit()
