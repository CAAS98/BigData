import sys

counter = 0 

for line in sys.stdin:
    for end in line.strip().split("\n"):
        if end: 
            counter += 1
print(counter)   
