from datetime import datetime, timedelta, time
from django.utils import timezone
import ast

#accepts the scraper instance, returns number of days to add
def get_next_run(scraper_instance):
	day_choices = (
        ('sun','Sunday'),
        ('mon','Monday'),
        ('tue','Tuesday'),
        ('wed','Wednesday'),
        ('thu','Thursday'),
        ('fri','Friday'),
        ('sat','Saturday'),
    )
	run_time = scraper_instance.time_select
	#check if sked day is none (brackets are django output)
	if scraper_instance.run_schedule:
		if run_time is None:
			run_time = time(6,0,0)
		now_time = datetime.now().time()
		week = day_choices
		sked_day = ast.literal_eval(scraper_instance.run_schedule)
		#build index of days the scraper should run (by number)
		sked_index = []
		for day in sked_day:
			for wkday in week:
				if day == wkday[0]:
					sked_index.append(week.index(wkday))
		#evaluate if current day and time is < sked day/time
		next_run_day = sked_index[0]
		#make this jibe with python weekday syntax
		today = datetime.now().weekday()+1
		for item in sked_index:
			if today < item:
				next_run_day = item
				break
		if today < next_run_day:
			add_days = next_run_day - today
		else:
			#check the runtime if runday is today
			if today == next_run_day and now_time < run_time:
				print 'today is the run day, but not yet'
				add_days = 0
			else:
				add_days = 7 - today + next_run_day
		return timezone.make_aware(datetime.combine(datetime.now(),run_time) + 
			timedelta(days=add_days), timezone.get_current_timezone())
	else:
		return None