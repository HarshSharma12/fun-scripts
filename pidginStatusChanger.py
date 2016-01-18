'''
Created on Mon Nov 23 12:56:34 2015
@author: HarshSharma12

Updates the status in Pidgin with a quote
from quotes.txt file on a daily basis.

Updates only betwwen 8 AM and 3 PM
'''

#!/usr/local/bin/python2.7

import os
import subprocess as sp
import random
import time
# Kill any open pidgin instances
if(8<time.localtime()[3]<15):
	os.system("TASKKILL /F /IM pidgin.exe")


	# Get the quote from the file 

	fname = 'quotes.txt'
	fid = open(fname, 'r');
	quote = str(fid.readline())[1:-2]
	by = str(fid.readline())[2:-1]
	status = '&amp;quot;'+ quote + '&amp;quot;&lt;br&gt; - ' + by;
	others = fid.readlines();
	fid.close()


	# Remove the used quote from the file
	fid = open('quotes.txt', 'w');
	for l in others[1:]:
		fid.write(l)
	fid.close()


	# Put the used quote in history.txt file
	hist = open('history.txt', 'a')
	print quote+' - ' + by
	hist.write('&amp;quot;' + quote + '&amp;quot;\n- ' + by + '\n\n')
	hist.close()

	''' 
	Not a good way to do.
	To do correctly add a new with epoch timestamps
	and update line 30 of prefs.xml
	'''
	statusFile = open('status.xml', 'r');
	statusData = statusFile.readlines()
	statusData[5] = '\t\t<message>'+ status + '</message>\n'
	statusData[9] = '\t\t<message>'+ status + '</message>\n'
	epochTime = statusData[3][54:64]
	print type(epochTime)
	statusFile.close()
	with open('C:\Users\harshs\AppData\Roaming\.purple\status.xml', 'w') as statusFile:
		statusFile.writelines(statusData)
		
	#Verify prefs.xml
	prefsFile = open('prefs.xml','r')
	prefsData = prefsFile.readlines()
	prefsFile.close()
	
	if(prefsData[29][42:52]!=epochTime):
		prefsList = list(prefsData[29])
		prefsList[42:52]=list(epochTime)
		prefsData[29]=''.join(prefsList)
		with open('C:\Users\harshs\AppData\Roaming\.purple\prefs.xml', 'w') as prefsFile:
			prefsFile.writelines(prefsData)
		
		


print 'Launching Pidgin'
os.startfile('C:\Program Files (x86)\Pidgin\pidgin.exe')


print '------------DONE------------'

if (len(others) < 2):
	print "Please update the quotes in the file."
	programName = "notepad.exe"
	fileName = "C:\Users\harshs\AppData\Roaming\.purple\\" + fname
	sp.Popen([programName, fileName])

