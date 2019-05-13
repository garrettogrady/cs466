import time
import os
import resource

from keyword_tree import keyword_main
from aho import aho_main
from suffix_tree import main_suffix




patterns = [line.rstrip('\n') for line in open("10-sequences.txt", "r")]
whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# with open('dream_space.txt', 'r') as file:
	
# 	data = file.read().replace('\n', '')
# 	sequence = ''.join(filter(whitelist.__contains__, data))
# 	t2 = time.time()
# 	print(sequence.split())
# 	keyword_main(patterns, sequence.split())
# 	t3 = time.time() 
# 	total = t3-t2
# 	second_space = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss - first_space
# 	print("total time: ", total)
# 	print("total space: ", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


with open('dna-1000000.txt', 'r') as file:
    data = file.read().replace('\n', '')
    sequence = ''.join(filter(whitelist.__contains__, data))
    
    #run aho
    # t0 = time.time()
    # aho_main(patterns, sequence)
    # t1 = time.time() 
    # total = t1-t0
    # first_space = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # print("total time: ", total)
    # print("total space: ", first_space)


 	#run keyword
    t4 = time.time()
    main_suffix(patterns, sequence)
    t5 = time.time() 
    total = t5-t4
    print("total time: ", total)
    print("total space: ", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


