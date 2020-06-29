import sys
print("Enter the data")
print("Note-use cntrl+d to stop the input")
data = sys.stdin.read()   # Use Ctrl d to stop the input
print(data)

with open ('fileHandling3.txt', 'w') as f:
    f.write(data)
    
    
