#!/bin/usr/python
#-*- coding: utf-8 -*-


'''
This Python program is the main Python file that performs layout confusion. 
The file provides input, output, and call-related operations for layout obfuscation.
input: sol's json_ast
'''

import os
import sys
import json


class layoutConfuse:
	def __init__(self, _filepath, _jsonFile):
		self.outputFileName = self.getOutputFileName(_filepath)
		self.solContent = self.getContent(_filepath)
		self.json = self.getJsonContent(_jsonFile)

	def getContent(self, _filepath):
		with open(_filepath, "r", encoding = "utf-8") as f:
			return f.readlines()
		return list()

	def getOutputFileName(self, _filepath):
		temp = _filepath.split(".")
		newFileName = temp[0] + "_layout_confuse." + temp[1]
		return newFileName

	def getJsonContent(self, _jsonFile):
		jsonStr = str()
		with open(_jsonFile, "r", encoding = "utf-8") as f:
			jsonStr = f.read()
		jsonDict = json.loads(jsonStr)
		return jsonDict

	def replaceVarName(self, _fileContent, _jsonContent):
		pass


	def run(self):
		#print(self.solContent)
		#print(self.outputFileName)
		#print(self.json)


#unit test
if __name__ == "__main__":
	lc = layoutConfuse("testCase.sol", "1_json.ast")
	lc.run()