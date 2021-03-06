import commands
import os
import datetime
import sys

#Script to start the MicroStrategy Intelligence Server and check the state afterwards
#Works with Python Version 2.6.8
path = "/bi/MSTR/bin/mstrctl"
starttime = datetime.datetime.now()

def getTimeDiff():
	"getTimeDiff"
	timediff = datetime.datetime.now() - starttime
	sys.stdout.write("\r%s" % str(timediff))
	sys.stdout.flush()
	return

def isstate():
	"isstate"
	val = str(commands.getstatusoutput(path + ' -s IntelligenceServer gs |grep -i state'))
	while "starting" in val:
		val = str(commands.getstatusoutput(path + ' -s IntelligenceServer gs |grep -i state'))
		getTimeDiff()
	val = str(commands.getstatusoutput(path + ' -s IntelligenceServer gs |grep -i state'))
	if "terminated" in val:
		print ""
		print 'terminated'
	else:
		print ""
		print formatOutput(val)
	return

def isstart():
	"isstart"
	os.system(path + ' -s IntelligenceServer start')
	return
	
def formatOutput(input):
	"formatOutput"
	output = ""
	for i, c in enumerate(input):
		if c == ">":
			output = input[i+1:]
			for j, d in enumerate(output):
				if d == "<":
					output = output[:-j]
					output = output.rpartition('<')[0]
					return output
	return output

#Programm
print 'Starting MicroStrategy Intelligence Server'
isstart()
starttime = datetime.datetime.now()
isstate()