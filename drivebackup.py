#!/usr/bin/python
#before use this scritp you must install google-drive-ocamlfuse to sync your Drive Acc.
import os
import time
import socket
from datetime import datetime
#Complete with the path where the file will be backed up
drivefilepath = 
#Complete with the path where the google drive should be mounted
drivemountpath = 
#Complete with the path where the local file to be backed up is located
localfilepath = 
#Complete  with the path where the log file will be storaged
logfilepath = 
if socket.create_connection(("www.google.com",80)):
	if not os.path.isfile(drivefilepath):
		os.system("google-drive-ocamlfuse "+drivemountpath)
		time.sleep(30)
		os.system("cp "+localfilepath+" "+drivefilepath)
		time.sleep(30)
		os.system("fusermount -u " + drivemountpath)
		stamp = datetime.now().strftime('%Y/%m/%d__%H:%M:%S - ')
		with open(logfilepath, "a") as logfile:
			logfile.write(stamp + '  Successful Backup \n')
else:
	stamp = datetime.now().strftime('%Y/%m/%d__%H:%M:%S - ')
	with open(logfilepath, "a") as logfile:
		logfile.write(stamp + '  No Internet Connection \n')
