import numpy as np
import pandas as pd
from collections import Counter
"""
Part 1: Find and score incomplete/corrupted lines and score
answer: 442131
exmpale answer: 26397
"""
lookup_table = {')':3, ']':57, "}":1197, ">": 25137}
score = 0
import numpy as np
incomplete_stacks = []
closings = {')':"(", "}":"{", ">":"<", "]":"["}
openings = {'(':")", "{":"}", "<":">", "[":"]"}
with open('data/puzzle10.txt', 'r') as f:
    for chars in f.readlines():
        stack = []
        chars = chars.replace('\n', '')
        # Scan through the chars
        invalid = False
        for idx, char in enumerate(chars):
            # if it's an opening, append
            if char in closings.values():
                stack.append(char)
            
            elif char in closings:
                # if the char closes the last open, pop the last open
                if stack[-1] == closings[char]:
                    stack.pop(-1)
                else:
                    print(f"{chars} is invalid, at {char}")
                    score += lookup_table[char]
                    invalid = True
                    break
        if not invalid:
            print(f"line-{chars}; is incomplete")
            incomplete_stacks.append(stack)
print(score)


"""
PART 2: Find scores of auto-completing remaining strings
"""
score_table = {')':1, "]": 2, "}":3, ">": 4}
scores = []
for incomplete in incomplete_stacks:
    completion_string = ''
    score = 0
    for char in incomplete[::-1]:
        score *= 5
        score += score_table[openings[char]]
        completion_string +=  openings[char]
    scores.append(score)

scores.sort()
middle_score = scores[len(scores)//2]
print(middle_score)