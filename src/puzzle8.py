import numpy as np
import pandas as pd

"""
Part 1: Count digits in corrupted displays
"""
pre_list = []
post_list = []

with open('data/puzzle8.txt', 'r') as f:
    for line in f.readlines():
        line = line.replace('\n', '')
        pre, post = line.split(" | ")
        pre_list.append(pre.split(" "))
        post_list.append(post.split(" "))

counter = 0
for post in post_list:
    for digit in post:
        if len(digit) in [2,3,4,7]:
            counter += 1
print(f"Total numbers of 1,4,7 and 8 is {counter}")
# p1 - 352

# Now we get to actually decode all of this
sd = lambda x,y: set(x) - set(y)
decoded_nums = []
for idx, (pre, post) in enumerate(zip(pre_list, post_list)):
    total_list = sorted([''.join(sorted(x)) for x in pre+post], key=lambda x: len(x))
    lt = {}
    

    for digit in total_list:
        if len(digit) == 2:
            lt[1] = digit
        if len(digit) == 3:
            lt[7] = digit
        if len(digit) == 4:
            lt[4] = digit
        if len(digit) == 7:
            lt[8] = digit
        # import pdb;pdb.set_trace()
        if len(digit) == 5:
            if len(set(digit) - sd(lt[4], lt[1]))==3:
                lt[5]=digit
            elif len(sd(digit,lt[1]))==3:
                lt[3]=digit
            else:
                lt[2]=digit
        if len(digit) == 6:
            if len(sd(digit, lt[4]))==2:
                lt[9] = digit
            elif len(sd(digit, lt[1]))==4:
                lt[0] = digit
            else:
                lt[6] = digit
        if len(digit) == 7:
            lt[8] = digit
    try:
        print(len(lt))
        decoder = {v:k for k,v in lt.items()}
        decoded_num = [''.join(sorted(x)) for x in post]
        decoded_num = int(''.join([str(decoder[x]) for x in decoded_num]))
        decoded_nums.append(decoded_num)
    except:
        import pdb;pdb.set_trace()
print(f"The sum of all decoded valeus is {sum(decoded_nums)}")