#!/bin/sh
for R in 10 15 30 50 100 250 1000
do
    for B in 5 10 15 25 50
    do
        python check_memory_usage.py count_sketch t8.shakespeare.txt $R $B > shakespeare_results/results_${R}_${B}.txt shakespeare
        echo Finished Shakespeare R=${R} B=${B}
        python check_memory_usage.py count_sketch SmallNationalNames.csv $R $B > name_results/results_${R}_${B}.txt names
        echo Finished Names R=${R} B=${B}
    done
done
