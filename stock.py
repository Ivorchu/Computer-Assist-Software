import twstock 
class stock: 
	def __init__(self, num):
		x = twstock.realtime.get(num).pop("realtime") 
		self.buy = x["best_ask_price"][0]
		self.bid = x["best_bid_price"][0]
		self.high = x["high"]
		self.low = x["low"] 





