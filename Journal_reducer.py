#!/usr/bin/python
from sys import stdin
import sys
import os
import re
index = {}
for line in stdin:
	# Split the input format <author-filename:count> as word and fileinfo based on hyphen
	word = line.split('-')[0]
	fileinfo = line.split('-')[-1]
	# Set value to return by default if dictionary value is not found
	index.setdefault(word, {})
	# Traverse multiple values in the dictionary
	for fi in fileinfo.split(','):
		# Separate the fileinfo parameter as file_id and count
		file_id, count = fi.split(':')
		# convert the count value from string to int
		count = int(count)
		# Set the default value of count as 0 for each author
		index[word].setdefault(file_id, 0)
		# increment the count value as the word is encountered
		index[word][file_id] += count

for word in index:
	#convert the filename,count to list
	fileinfo_list = ["%s:%d" % (file_id, index[word][file_id]) for file_id in index[word]]
	
	# Join multiple filenames together with comma separation
	fileinfo = ','.join(fileinfo_list)
	# Create dictionary of values for each key
	pd = dict((k.strip(),v.strip()) for k,v in (item.split(':') for item in fileinfo.split(',')))
	# Convert the count value in the value part of the dictionary to int
	pdf = dict((k,int(v)) for k,v in pd.iteritems())
	# Stream the output as <author:{file1:count, file2:count ..}>
	print('%s:%s' % (word,pdf))
