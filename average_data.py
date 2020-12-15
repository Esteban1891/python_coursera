# Use the file name mbox-short.txt as the file name
import statistics
fname = input("Enter file name: ")
fh = open(fname)
count = 0
y = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    x = line.find('0')
    t = float(line[x:])
    y += t
    av = y / count
print("Average spam confidence:", av)
