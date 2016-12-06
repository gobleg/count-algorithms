#!/bin/sh
for R in 10 15 30 50 100 250 1000
do
    for B in 5 10 15 25 50 100 500 1000
    do
        #python check_memory_usage.py count_min_sketch shakespeare_linear.out $R $B > shakespeare_results_cmin/results_${R}_${B}.txt shakespeare
        #echo Finished Shakespeare CMin R=${R} B=${B}
        python check_memory_usage.py count_median_sketch shakespeare_linear.out $R $B > shakespeare_results_cmed/results_${R}_${B}.txt shakespeare
        echo Finished Shakespeare CMed R=${R} B=${B}
        #python check_memory_usage.py count_sketch shakespeare_linear.out $R $B > shakespeare_results_csketch/results_${R}_${B}.txt shakespeare
        #echo Finished Shakespeare CSketch R=${R} B=${B}
        python check_memory_usage.py count_min_sketch names_linear.out $R $B > name_results_cmin/results_${R}_${B}.txt names
        echo Finished Names CMin R=${R} B=${B}
        #python check_memory_usage.py count_median_sketch names_linear.out $R $B > name_results_cmed/results_${R}_${B}.txt names
        #echo Finished Names CMed R=${R} B=${B}
        #python check_memory_usage.py count_sketch names_linear.out $R $B > name_results_csketch/results_${R}_${B}.txt names
        #echo Finished Names CSketch R=${R} B=${B}
    done
done
