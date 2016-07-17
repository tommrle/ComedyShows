#!/usr/local/bin/python

from lxml import html
from ShowObject import show
from ShowObject import show_time
import requests
from datetime import datetime
from time import mktime as mktime
import urllib
import os.path 
import jsonpickle
from bs4 import BeautifulSoup
import re
import sys
from scripts.CreateShowtimeCalendar import turnTupleIntoCalendar
import hashlib #for unique id for shows

CUR_PATH = "data/current/current.json"
page = requests.get('http://www.secondcity.com/shows/chicago/')
current_shows_list = []
today = datetime.today()


def download_image_to_img_dir(img_url, show_title):
	print "Logging: Checking url: " + img_url + " and show title " + show_title
	if not os.path.isfile("img/" + show_title):
		print "Logging: Attempting to download from " + img_url
		urllib.urlretrieve(img_url, "img/" + show_title)
		#downloads_count += 1
	return "img/" + show_title

def convert_date_to_proper_year(show_date):
	if (today.month <= show_date.month):
		return datetime(today.year, show_date.month, show_date.day, show_date.hour, show_date.minute)
	else:
		return datetime(today.year + 1, show_date.month, show_date.day, show_date.hour, show_date.minute)

#show_day_of_week, show_month, show_day_num, show_time, is_sold_out, buyUrl
def parse_date(show_time_html):
	new_showobjects = []
	show_times_formatted = []
	show_day_of_week = show_time_html.find(class_="tickets-single-show-date-day").get_text(strip=True)
	show_month = show_time_html.find(class_="tickets-single-show-date-month").get_text(strip=True)
	show_day_num = show_time_html.find(class_="tickets-single-show-date-date").get_text(strip=True)
	show_month_int = datetime.strptime(show_month, "%b").month;

	for data in show_time_html.find_all('a'):
		buy_url = data.get('href')
		time = data.find(class_="tickets-single-show-link-time").get_text(strip=True)
		show_datetime = datetime.strptime("2016 " + show_day_of_week + " " + show_day_num + " " + show_month + " " + time, "%Y %a %d %b %I:%M %p");
		show_times_formatted.append( ( mktime(convert_date_to_proper_year(show_datetime).timetuple()) * 1000, buy_url ));
	return show_times_formatted

def print_data():
	for show in all_shows: 
		show.print_show()
	#print "Images Downloaded: " + str(downloads_count)

def save_cur():
	print "Logging: Initiating save"
	all_shows_current = jsonpickle.encode(all_shows)
	open(CUR_PATH, 'w+').write(all_shows_current)
	print "Logging: Save complete"

def load_cur():
	global current_shows_list
	print "Logging: Loading cur"
	current_shows_json = open(CUR_PATH, 'r').read()
	current_shows_list = jsonpickle.decode(current_shows_json)

def get_price_range(show_times_list):
	if len(show_times_list) > 0:
		buy_page = requests.get(show_times_list[0].buy_url)
		buy_tree = BeautifulSoup(buy_page.content, 'lxml')
		index = 0
		while re.search("Ticket Sales Closed for this show!", str(buy_tree)):
			index += 1
			if index == len(show_times_list):
				return "Sold Out"
			buy_page = requests.get(show_times_list[index].buy_url)
			buy_tree = BeautifulSoup(buy_page.content, 'lxml')
		m = re.search("[$][1-9][0-9][.][0-9]{2}", str(buy_tree))
		if m != None:
			return m.group(0)
	return ""

def parse_show_objects_for_unqiue_show_times(show_times_list):
	unique_shows = []
	for show in show_times_list:
		if not show.show_time in unique_shows:
			unique_shows.append(show.show_time)
	return unique_shows

def get_show_title_hash(show_title):
	return hashlib.md5(show_title.encode('utf-8').strip()).hexdigest()


tree = BeautifulSoup(page.content, "lxml")

all_shows = []
all_articles = tree.find_all('article')

if all_articles == []:
	print "ERROR: Outputting tree"
	print tree
	print "Continuing in Test Mode"
	tree = BeautifulSoup( open("data/test/pagesource.html", "r").read() , "lxml" )
	all_articles = tree.find_all('article')
#else:
	#open("data/test/sample_page.json", 'w+').write(all_articles)

for article in all_articles:
	string_set = [text for text in article.stripped_strings]
	theater = string_set[0]
	show_title = string_set[1]
	show_descrip = string_set[2]
	show_times = []
	show_times_formatted = []
	for show_time_html in article.find_all('ul'):
		show_times_formatted.extend(parse_date(show_time_html))
	img_url = article.img.get('src')
	if not img_url[0] == 'h':
		img_url = 'http:' + img_url
	local_url = download_image_to_img_dir(img_url, show_title)
	ticket_price_range = get_price_range(show_times)
	unqiue_show_times = parse_show_objects_for_unqiue_show_times(show_times)
	show_time_cal = turnTupleIntoCalendar(show_times_formatted)
	unique_id = get_show_title_hash(show_title)
	if len(show_times_formatted) > 0:
		next_show_time = show_times_formatted[0][0];
	all_shows.append(show(show_title, show_descrip, local_url, show_times, 
												theater, ticket_price_range, unqiue_show_times,
												 show_time_cal, next_show_time, unique_id))

#print_data()
load_cur()

if all_shows == current_shows_list:
	print 'Logging: No new shows or show times'
else:
	save_cur()
	print 'New data detected, updating show object'
