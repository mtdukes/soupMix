from __future__ import unicode_literals

from django.db import models
from django import forms

from django.db.models.signals import post_save
from django.dispatch import receiver
import sm_utils

class Scraper(models.Model):
	#choices for scraper code, just python for now
	code_choices = (
		('py','Python'),
	)
	day_choices = (
        ('sun','Sunday'),
        ('mon','Monday'),
        ('tue','Tuesday'),
        ('wed','Wednesday'),
        ('thu','Thursday'),
        ('fri','Friday'),
        ('sat','Saturday'),
    )
	slug = models.SlugField(
		help_text = 'Short label, no spaces',
		unique=True,
	)
	name = models.CharField(
		max_length=50,
		help_text = 'Name your scraper',
	)
	def __str__(self):
		return self.name
	date_created = models.DateTimeField(
		auto_now_add=True,
	)
	code_type = models.CharField(
		max_length=2,
		choices=code_choices,
		default='py',
		help_text = 'Select your programming language (python only for now)',
	)
	code_block = models.TextField(
		help_text = 'Enter your scraper code above',
	)
	run_schedule = models.CharField(
		max_length=100,
		blank=True,
		null=True,
		default=None,
		help_text = 'Specify what days your scraper should run automatically',
	)
	time_select = models.TimeField(
		blank=True,
		null=True,
		default=None,
		help_text= 'Specify when you want your scraper to run (24 hour format). If not specified, it will default to 6am'
	)
	last_run = models.DateTimeField(
		editable=False,
		blank=True,
		null=True
	)
	next_run = models.DateTimeField(
		editable=False,
		blank=True,
		null=True
	)
	active = models.BooleanField()
	email = models.EmailField(
		blank=True,
		null=True
	)

#when scraper is saved, update the next run time in case day/time changed
@receiver(post_save, sender=Scraper, dispatch_uid="update_rundate")
def update_rundate(sender, instance, **kwargs):
	#check if scraper is active and update next_run accordingly
	if instance.active:
		next_run_on_save = sm_utils.get_next_run(instance)
		Scraper.objects.filter(id=instance.id).update(next_run=next_run_on_save)
	else:
		Scraper.objects.filter(id=instance.id).update(next_run=None)

class DataFile(models.Model):
	name = models.CharField(
		max_length=50,
	)
	def __str__(self):
		return self.name
