# -*- coding:utf-8 -*-
import os

def readlines(path):
	if exist(path):
		f = open(path, 'r')
		return file.readlines(path, 'r')

def exist(path):
	if not os.path.isfile(path):
		raise TypeError(path, " does not exists")
	return True