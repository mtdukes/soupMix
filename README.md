:stew::stew::stew:
# SoupMix
:stew::stew::stew:

SoupMix is a platform to allow news organizations or anybody else to scrape sites to obtain data with a few simple steps. Really a work in progress.

Guiding principles:

 * updateable
 * aceessible
 * extensible

## The Basics

This application will use a Django framework. The installation will require a few details from an Amazon AWS instance, but otherwise will allow users to start it up very quickly.

This is all aspirational.

After they launch the platform, they will have the ability to build a new scraper using Python, or prebake a scraper using internal elements or submitted ["recipes."](https://github.com/sinker/tacofancy) Along the way, it will demonstrate good practices (sleep for 1 second, etc.). Will include resources on the ethics of scraping.

* Will present prebuilt blocks for using common scraper tactics.
* Will allow the launch of new scrapers
* Logs errors consistently in one accessible place
* permits ability to email updates on scrapers
* data analysis in django?
* will it be easier to install on a raspberry pi?

Will be heavily influenced by the [LA Times' Django for data analysis](https://github.com/datadesk/django-for-data-analysis-nicar-2016) session at NICAR 2016.

## How to start

1. In a terminal window, enter

'''bash
redis-server
'''

2. In a separate terminal window, enter

'''bash
workon soupMix
cd scrapersuite
celery -A scrapersuite worker -l info
'''

3. In a separate terminal window, enter

'''bash
workon soupMix
python manage.py runserver
'''

### Built using

* [Beautiful Soup for scraping](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#)
* [Django for CMS](https://www.djangoproject.com/)
* [CodeMirror for syntax hightlighting](https://codemirror.net)
* [Redis](https://redis.io/)
* [Celery](http://www.celeryproject.org/)

## Preproduction checklist

* Remove all keys
* Set debug to false
* See Daemonization instructions for threading celery/redis
* Heavy documentation
* Code cleanup

### Tutorials I'm using

* [Info from previous legtracker project](/Users/mtdukes/Documents/development/leg_tracker/notes/roadmap.txt)
* [Deploying Django on AWS](http://nickpolet.com/blog/deploying-django-on-aws/1/)
* [Django tutorial](https://docs.djangoproject.com/en/1.10/intro/tutorial01/)
* [Tutorial to add syntax highlighting](https://mr-coffee.net/blog/code-editor-django-admin)
* [Outputting CSVs with Django](https://docs.djangoproject.com/en/1.10/howto/outputting-csv/)
* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
* [Integrating tasks with Django and celery](https://realpython.com/blog/python/asynchronous-tasks-with-django-and-celery/) But needed to add [the init.py file](https://stackoverflow.com/questions/15294938/python-celery-socket-error-errno-61-connection-refused)
* [Async Celery by Example](https://zapier.com/blog/async-celery-example-why-and-how/) and [How to work with ajax and django](https://simpleisbetterthancomplex.com/tutorial/2016/08/29/how-to-work-with-ajax-request-with-django.html)
