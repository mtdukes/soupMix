from celery.decorators import task
from time import sleep
import subprocess
#for logging purposes
from datetime import datetime
from django.utils import timezone
from soupmix.models import Scraper

@task(name='get_output')
def get_out(scraper_id):
	try:
		scraper = Scraper.objects.get(pk=scraper_id)
		code = scraper.code_block
		#update the time last ran
		scraper.last_run = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
		scraper.save()
		p = subprocess.Popen(['python','-u', '-c',code], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		output = _loop_capture(p)
	except Exception, e:
		output = 'Error: ' + str(e)
	return 'Task complete'

#try it with a log
#https://stackoverflow.com/questions/18421757/live-output-from-subprocess-command
def _loop_capture(p):
	stdout = []
	#open a new file to log
	with open('test.log','w') as f:
		f.write(str(datetime.now().time())+' >> Code executed\n')
		f.close()
	while True:
		line = p.stdout.readline()
		stdout.append(line)
		if line == '' and p.poll() != None:
			break
		#append to newly opened file
		with open('test.log','a') as f:
			f.write(str(datetime.now().time()) + ' >> ' + line)
	with open('test.log','a') as f:
			f.write(str(datetime.now().time())+' >> Code complete')
	return ''.join(stdout)

