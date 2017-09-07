# -*- coding:utf-8 -*-
import sys
import os

def test(path):
	if not os.path.isfile(path):
		raise TypeError(path, " does not exists")

	countLines(path)
	countChars(path)

def countChars(path):
	count = 0
	f = open(path, 'r')
	for line in open(path):
		line = f.readline()
		count += len(line)
	print(path, " has ", str(count), " characters.")

def countLines(path):
	count = 0
	f = open(path, 'r')
	for line in open(path):
		line = f.readline();
		count += 1
	print(path, " has ", str(count), " lines.")

if __name__ ==  '__main__':
	import changer
	import formats
	import module2
	if len(sys.argv) > 1:
		for path in sys.argv:
			test(path)

