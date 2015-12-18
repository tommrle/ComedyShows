#!/usr/local/bin/python

import jsonpickle

CUR_PATH = "data/current/current.json"

def load():
	global all_shows
	all_shows_json = open(CUR_PATH, 'r').read()
	all_shows = jsonpickle.decode(all_shows_json)

all_shows = []

load()
for show in all_shows:
  print show.uniqueShowTimes[0]
  #for show_time in show.show_times:
  #  print show_time.buy_url + " " + show.ticketPriceRange
#print_data()

