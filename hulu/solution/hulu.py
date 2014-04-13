'''
Written April 13, 2014

My goal here was to create a simple solution to the problem, not an efficient
or speedy one. Given the size of the dataset, this code provides the correct
output in a reasonable amount of time without optimization, but reverse 
indexing all the rows by n-gram and referring to that for every query would
be faster.
'''

from json import dumps

FILENAME = 'tv_show_groups_sample.in'
#FILENAME = 'tv_show_groups.in'

def split_list(lst, on):
    idx = lst.index(on)
    return lst[:idx], lst[idx+1:]

f = open(FILENAME)
outfile = file('hulu.out', 'w')
f.readline() #discard the line with '1' on it
lines = [a.strip().split(',') for a in f.readlines()]
data, commands = split_list(lines, ['####'])
for words in commands:
    mapping = {}
    for d in data:
        if all([w in d for w in words]):
            for data_word in d:
                if data_word in words:
                    continue
                mapping[data_word] = mapping.get(data_word, 0) + 1
    print(dumps(mapping, sort_keys=True))
    outfile.write("{}\n".format(dumps(mapping, sort_keys=True)))
outfile.close()
