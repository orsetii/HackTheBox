#!/usr/bin/env python
import time

def find_by_value(value, index):
    for l in all_line_dict:
        if len(l) < 3:
            continue
        if l[index] == value:
            return l

def collect_val(record):
    collection.append(record[1])

def walk():

    indx = 0

    cur = find_by_value(69420, 0)
    while True:

        if indx == 998:
            break
        for idx, letter in enumerate(password):
            print(f"{letter} -> {ord(letter) ^ cur[1]}")
            password[idx] = chr(ord(letter) ^ cur[1])
            
        print(cur[2])
        collect_val(cur)
        cur = find_by_value(cur[2], 0)
        indx += 1


password = ['l', '0', 'l', '_', 'n', '0', 'p', 'e']

f = open("cleaned.txt")

i = 0

found_end = False
all_line_dict = [[]]
collection = []

for line in f.readlines():
    i += 1
    if i < 16:
        continue

    line = line.strip('\n')
    split_line = line.split(" ")
    for idx, x in enumerate(split_line):
        try:
            split_line[idx] = int(x)
        except:
            continue
    if split_line[2] == 999:
        found_end = True
    all_line_dict.append(split_line)

if found_end:
    print("Found the endpoint")
else:
    print("unable to find endpoint")
    exit()


walk()

print(password)
