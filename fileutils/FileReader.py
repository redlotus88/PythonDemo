# -*- coding:utf-8 -*-
import sys
import os

def readlines(path):
	if exist(path):
		f = open(path, 'r')
		return f.readlines()

def exist(path):
	if not os.path.isfile(path):
		raise TypeError(path, " does not exists")
	return True

if __name__ == '__main__':
	exist('FileReader.py')
	print(readlines('FileReader.py'))