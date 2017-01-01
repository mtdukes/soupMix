import csv, ast
from django.shortcuts import render
from django.http import HttpResponse, Http404
from soupmix.models import Scraper
from soupmix.tasks import get_out
from datetime import datetime, timedelta, time
from django.utils import timezone
import sm_utils

#index page for testing, which accepts a url parameter
#if one exists
#one thing to watch: make sure only one of these is running,
#otherwise you will trigger multiple with each reload
def index(request,run_option=''):
	try:
		#testing a method for running code within django
		scraper = Scraper.objects.get(slug=run_option)
		task_id = get_out.delay(scraper.pk)
		context = {
			'soup_code': scraper.code_block,
			'soup_output': '',
			'task_id': task_id,
		}
	except Scraper.DoesNotExist:
		raise Http404('Scraper does not exist. Please check the slug.')
	return render(request,'soupmix/index.html', context, content_type='text/html')

#need to find a way to pass the task id from the output to the ajax view below
def ajax_view(request):
	task_id = request.GET.get('id')
	results = get_out.AsyncResult(task_id)
	while True:
		if results.ready():
			break
	return update_fragment(request)

def update_fragment(request):
	with open('test.log','r') as f:
		results = f.read()
		return render(request,'soupmix/ajax_fragment.html',{'results':results})

#this is a test of csv output, via:
#http://127.0.0.1:8000/admin/soupmix/export_csv
#https://docs.djangoproject.com/en/1.10/howto/outputting-csv/
#url added to soupmix>urls
def export_csv(request):
	# Create the HttpResponse object with the appropriate CSV header.
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

	writer = csv.writer(response)
	writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
	writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
	print 'exporting csv'
	return response

