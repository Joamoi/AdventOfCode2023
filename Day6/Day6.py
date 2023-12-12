from math import sqrt
import time

with open("input.txt") as f:
    lines = f.readlines()

start_time = time.time()

# part A

times = lines[0].split(":")[1].split()
distances = lines[1].split(":")[1].split()
records = [0,0,0,0]

for j in range(len(times)):
    t = int(times[j])
    oldrecord = int(distances[j])
    print("\ntime: " + str(t) + "\told record: " + str(oldrecord) + "\n")
    for i in range(1, t):
        x = i * (t - i)
        if (x > oldrecord):
            records[j] += 1
            print("i: " + str(i) + "\tx: " + str(x) + "\tover old record")
        else:
            print("i: " + str(i) + "\tx: " + str(x))
         
multi = records[0] * records[1] * records[2] * records[3]       
print("\nrecords: " + str(records))
print("multiplication: " + str(multi))

a_time = time.time() - start_time
print("part A runtime: \t" + str(format(a_time, ".4f")) + " seconds")

# part B

empty = ''
t = int(empty.join(times))
oldrecord = int(empty.join(distances))
records = 0

t = int(t)
print("\nB1, time: " + str(t) + "\told record: " + str(oldrecord))
for i in range(1, t):
    x = i * (t - i)
    if (x > oldrecord):
        records += 1

print("records: " + str(records))

b1_time = time.time() - (start_time + a_time)
print("part B1 runtime:\t" + str(format(b1_time, ".4f")) + " seconds")

# part B optimized, formula x = i * (time - i) is same for first record and last record so they are equally far from i = 0 and i = 48938466 respectively

lowtime = 0
hightime = 0

t = int(t)
print("\nB2, time: " + str(t) + "\told record: " + str(oldrecord))
for i in range(1, t):
    x = i * (t - i)
    if (x > oldrecord):
        lowtime = i
        break
        
records = t - 2 * lowtime + 1

print("lowest hold time with a new record: " + str(lowtime))
print("records: " + str(records))

b2_time = time.time() - (start_time + a_time + b1_time)
print("part B2 runtime:\t" + str(format(b2_time, ".4f")) + " seconds")

# part B more optimized, we use ai^2 + bi + c = 0 solving formula to find first record
# x = i * (t - i) ----> i^2 - ti + x = 0 ----> i = (t +- sqrt(t*t - 4*x)) / 2

t = int(t)
x = oldrecord

print("\nB3, time: " + str(t) + "\told record: " + str(oldrecord))

i1 = (t + sqrt(t*t - 4*x)) / 2
i2 = (t - sqrt(t*t - 4*x)) / 2

ilist = [i1, i2]
ilist.sort()

i = int(ilist[0]) + 1
records = t - 2 * i + 1

print("lowest hold time with a new record: " + str(i))
print("records: " + str(records))

b3_time = time.time() - (start_time + a_time + b1_time + b2_time)
print("part B3 runtime:\t" + str(format(b3_time, ".4f")) + " seconds\n")