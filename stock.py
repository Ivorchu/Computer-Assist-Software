import twstock 

def stock(num):
	stock = twstock.realtime.get(num).pop("realtime") 
	print("最高買價", stock["best_bid_price"][0]) 
	print("最低賣價", stock["best_ask_price"][0]) 
	print("最高", stock["high"])
	print("最低", stock["low"]) 

num = input("請輸入股票代碼 ") 
stock(num) 