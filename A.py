import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument("--input", action="store", dest="input_file")
parser.add_argument('--output', action="store", dest="output_file")
args = parser.parse_args()
input_file = open(args.input_file, 'r')
output_file = open(args.output_file, 'w')

#print("Enter amount of lines in norm algo:")
n = int(input_file.readline())
cycle = []
left = []
right = []
stop = []
#print("enter the norm algo:")
for i in range(n):
    x = str(input_file.readline())
    b = x.split("-")
    left.append(b[0])
    if b[1][0] == ".":
        stop.append(1)
        b[1] = b[1][1:]
    else:
        stop.append(0)
    right.append(b[1])
#print("enter word:")
word = input()
cycle.append(word)
i = 1
while i > 0:
    for j in range(n):
        if word.count(left[j]) > 0:
            word = word.replace(left[j], right[j], 1)
            if cycle.count(word) > 1:
                i = -1
            cycle.append(word)
            if stop[j] == 1:
                i = 0
            break
        if j == n-1:
            i = 0
            break
if i == 0:                          #result
    output_file.write(word)
else:
    output_file.write("infinite loop")
input_file.close()
output_file.close()