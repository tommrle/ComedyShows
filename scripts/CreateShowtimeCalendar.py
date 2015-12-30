#!/usr/local/bin/python

import jsonpickle
from datetime import datetime

#take in a list of unix timestamps, url tuples and sort into a calendar type object for the front to easily
# find multiple show times for a single date

def loadJSONFile(file_path):
   return jsonpickle.decode(open(file_path, 'r').read())

def turnTupleIntoCalendar(show_times_tuples):
  show_time_cal = {}
  for show_time_tuple in show_times_tuples:
    #test code for depickled:
    #tempDate = datetime.fromtimestamp(show_time_tuple["py/tuple"][0] / 1000)
    tempDate = datetime.fromtimestamp(show_time_tuple[0] / 1000)
    if tempDate.year in show_time_cal:
      show_time_cal = addMonthAndDay(tempDate, show_time_cal, show_time_tuple[1])
    else:
      show_time_cal[tempDate.year] = {}
      show_time_cal = addMonthAndDay(tempDate, show_time_cal, show_time_tuple[1])
  return show_time_cal

def addMonthAndDay(tempDate, show_time_cal, show_buy_url):
  if (tempDate.month-1) in show_time_cal[tempDate.year]:
    if tempDate.day in show_time_cal[tempDate.year][tempDate.month-1]:
      show_time_cal[tempDate.year][tempDate.month-1][tempDate.day].append([tempDate.strftime("%I:%M %p"), show_buy_url])
    else:
      show_time_cal[tempDate.year][tempDate.month-1][tempDate.day] = [[tempDate.strftime("%I:%M %p"), show_buy_url]]
  else:
    show_time_cal[tempDate.year][tempDate.month-1] = {}
    show_time_cal[tempDate.year][tempDate.month-1][tempDate.day] = [[tempDate.strftime("%I:%M %p"), show_buy_url]]
  return show_time_cal


#print turnTupleIntoCalendar(loadJSONFile('../data/test/dateme.json')["showTimesFormatted"])