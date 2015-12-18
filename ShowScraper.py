#!/usr/local/bin/python

from lxml import html
import requests
from datetime import date
from datetime import timedelta

def some_weekend_dates(todays_date):
	if(todays_date.isoweekday() == 7):
		return [todays_date, todays_date + timedelta(5), todays_date + timedelta(6), todays_date + timedelta(7)]
	elif(todays_date.isoweekday() == 6):
		return [todays_date, todays_date + timedelta(1), todays_date + timedelta(6),
				todays_date + timedelta(7), todays_date + timedelta(8)]
	elif(todays_date.isoweekday() == 5):
		return [todays_date, todays_date + timedelta(1), todays_date + timedelta(2)]
	else:
		return [todays_date + timedelta(5 - todays_date.isoweekday()), 
				todays_date + timedelta(6 - todays_date.isoweekday()),
				todays_date + timedelta(7 - todays_date.isoweekday())]


month = date.today().month
day = date.today().day
year = date.today().year

page = requests.get('http://www.secondcity.com/tickets/?calday='+str(month)+'/'+str(day)+'/'+str(year))
tree = html.fromstring(page.text)

theatres = tree.xpath('//span[@class="meta"]/text()')
shows = tree.xpath('//h2/a[starts-with(@href, "http://www.secondcity.com/shows/chicago/")]/text()')

print 'Theatres: ', theatres
print 'Shows: ', shows

print some_weekend_dates(date.today())

for weekend_day in some_weekend_dates(date.today()):
	month = date.today().month
	day = date.today().day
	year = date.today().year
	page = requests.get('http://www.secondcity.com/tickets/?calday='+str(month)+'/'+str(day)+'/'+str(year))
	tree = html.fromstring(page.text)
	shows_new = tree.xpath('//h2/a[starts-with(@href, "http://www.secondcity.com/shows/chicago/")]/text()')
	shows += shows_new


print '== Upcoming Shows This Weekend =='
print list(set(shows))
