import os
import time
source = ['"E:\\MyDocuments"','E:\\Code']
target_dir = 'E:\\Backup'
target = target_dir + os.sep + \
		 time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir):
	os.mkdir(target_dir) # make directory
	
zip_command = "winrar a {0} {1}".format(target,' '.join(source))
print "Zip command is:"
print zip_command
print "Running:"
if os.system(zip_command) == 0:
	print 'Successful backup to', target
else:
	print 'Backup FAILED'