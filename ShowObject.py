class show:

	def __init__(self, title, descrip, imageUrl, show_times, theater, ticket_price_range, uniqueShowTimes, show_time_cal, next_show_time, unique_id):
		self.title = title
		self.descrip = descrip
		self.imageUrl = imageUrl
		self.show_times = show_times
		self.theater = theater
		self.ticketPriceRange = ticket_price_range
		self.uniqueShowTimes = uniqueShowTimes
		self.showTimeCal = show_time_cal
		self.nextShowTime = next_show_time
		self.uniqueId = unique_id

	def show_times_to_str(self):
		full_string = ""
		for show_time in self.show_times:
			full_string += show_time.print_show_time() + ",\n"
		return full_string

	def __eq__(self, other):
		return self.__dict__ == other.__dict__

	def __str__(self):
		return str(self.__dict__)
 
	def print_show(self):
		print "Show Title: " + self.title
		print "Show: " + self.descrip + ", " + self.theater
		print " image: " + self.imageUrl
		print " times: " + self.show_times_to_str()
		print "-------\n"


class show_time:

	def __init__(self, show_day_of_week, show_month, show_day_num, show_time, is_sold_out, buyUrl):
		self.buy_url = buyUrl
		self.show_day_num = show_day_num
		self.show_month = show_month
		self.show_day_of_week = show_day_of_week
		self.show_time = show_time
		self.is_sold_out = is_sold_out

	def __eq__(self, other):
		return self.__dict__ == other.__dict__

	def __str__(self):
		return str(self.__dict__)

	def print_show_time(self):
		return str(self.show_month) + " " + str(self.show_day_num) + "(" + str(self.show_time) + ") Buy At: " + self.buy_url + ", Tickets Available: " + str(self.is_sold_out)